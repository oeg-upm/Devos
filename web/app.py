from flask import Flask
from flask import render_template, request
from werkzeug.utils import secure_filename
import traceback
import random
import string
import sys
import os
import requests
from datetime import datetime
from devos import gister

UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app = Flask(__name__)
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
TECHNIQUES = {
    'OntMet': 'OntMet (Ontology Metadata)',
    'ClaFreq': 'ClaFreq (Class Frequency)',
    'LabLen': 'LabLen (Labels Length)'
}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_random_text(n=4):
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(n)])

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'GET':
        return render_template('app.html', techniques=TECHNIQUES)
    else:
        dest = ""
        if 'technique' not in request.form:
            return "Error, technique is missing", 400
        technique = request.form['technique']
        if technique not in TECHNIQUES:
            return "Error, invalid technique", 400

        if 'file' in request.files and request.files['file'].filename:
            print("\n\n******FILE\n\n")
            file = request.files['file']
            filename = secure_filename(file.filename)
            dest = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print("in file and dest: %s" % dest)
            file.save(dest)
        elif 'url' in request.form:
            print("\n\n******URL\n\n")
            url = request.form['url'].strip()
            if url == "":
                return "Error, expected URL of the Ontology file", 400
            else:
                try:
                    fname = url.split('/')[-1] + "-" + get_random_text()
                    # fname = url.split('/')[-1]# + "-" + get_random_text()
                    # fname = fname + + "-" + get_random_text() + fname.split('.')[-1]
                    dest = os.path.join(app.config['UPLOAD_FOLDER'], fname)
                    print("in url and dest: %s" % dest)
                    download_file(url, dest)
                except Exception as e:
                    print("Exception: %s" % str(e))
                    traceback.print_exc()
                    return "Internal Error", 500
        else:
            return "Error, expected URL of the Ontology or the file itself", 400

        try:
            diagram_txt, time_txt = get_diagram(dest, technique)
            return render_template('view.html', diagram_txt=diagram_txt, time_txt=time_txt)
        except Exception as e:
            print("Exception: %s" % str(e))
            traceback.print_exc()
            return "Internal Error", 500


def get_diagram(ont_path, tech):
    a = datetime.now()
    out_path = ont_path+".md"
    invalid_tech = False
    if tech=='ClaFreq':
        gister.freq_workflow(input_path=ont_path, out_path=out_path, topn=7, topr=21,
                      only_object_property=True, soft=False)
    elif tech=="LabLen":
        gister.leng_workflow(input_path=ont_path, out_path=out_path, topn=7, topr=21, soft=False)
    elif tech == "OntMet":
        gister.meta_workflow(input_path=ont_path, out_path=out_path, topn=7, topr=21, soft=False, title=True, desc=True,
                      abstract=True, only_object_property=True)
    else:
        invalid_tech = True
        diagram_txt = ""
    if not invalid_tech:
        with open(out_path) as f:
            diagram_txt = f.read()
            diagram_txt = "\n".join(diagram_txt.split('\n')[1:-1])
        os.remove(out_path)
    os.remove(ont_path)
    b = datetime.now()
    time_elapsed_str = "It took: %.1f minutes to generate the summary diagram" % ((b - a).total_seconds() / 60.0)
    return diagram_txt, time_elapsed_str

def download_file(url, dest):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(dest, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return dest


@app.route("/viewer")
def view():
    return render_template('view.html')


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        app.run(debug=True, port=int(sys.argv[1]))
    elif len(sys.argv) == 3 and sys.argv[2].isdigit():
        app.run(debug=True, host=sys.argv[1], port=int(sys.argv[2]))
    else:
        app.run(debug=True)


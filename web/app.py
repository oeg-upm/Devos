from flask import Flask
from flask import render_template, request
from werkzeug.utils import secure_filename
import traceback
import random
import string
import sys
import os
import requests

UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app = Flask(__name__)
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_random_text(n=4):
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(n)])

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'GET':
        return render_template('app.html')
    else:
        # check if the post request has the file part
        dest = ""
        if 'file' in request.files:
            print("\n\nfile is there")
            # return "Error, expected URL of the Ontology file"
            # flash('No file part')
            # return redirect(request.url)
            file = request.files['file']
            # print(random.choices(string.ascii_lowercase))
            if file and file.filename:
                filename = secure_filename(file.filename)
                dest = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(dest)
                # return redirect(url_for('download_file', name=filename))
        elif 'url' in request.form:
            print("\n\nurl is there")
            url = request.form['url'].strip()
            if url == "":
                return "Error, expected URL of the Ontology file", 400
            else:
                try:
                    fname = url.split('/')[-1] + "-" + get_random_text()
                    dest = os.path.join(app.config['UPLOAD_FOLDER'], fname)
                    download_file(url, dest)
                except Exception as e:
                    print("Exception: %s" % str(e))
                    traceback.print_exc()
                    return "Internal Error", 500
        else:
            return "Error, expected URL of the Ontology or the file itself", 400

        return "Success"



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


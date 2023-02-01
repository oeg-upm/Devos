from flask import Flask
from flask import render_template
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('app.html')
    # return "<p>Hello, World!</p>"



if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        app.run(debug=True, port=int(sys.argv[1]))
    elif len(sys.argv) == 3 and sys.argv[2].isdigit():
        app.run(debug=True, host=sys.argv[1], port=int(sys.argv[2]))
    else:
        app.run(debug=True)


#-----------------------------------------------------------------
# Author : SonerSezgin
# Date : 2023-03-11
# Aim : Flask BluePrint Training
#-----------------------------------------------------------------

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('page1.html')

@app.route('/page2')
def sayfa2():
    return render_template('page2.html')


if __name__ == '__main__':
    app.run(debug=True)


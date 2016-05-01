from flask import Flask ,render_template
from flask.ext.mysql import MySQL

app = Flask(__name__)

@app.route("/")
def hello():
    return "database connected"
if __name__=='__main__':
    app.run()

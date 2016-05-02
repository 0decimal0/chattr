from flask import Flask ,render_template
from connector import connect

app = Flask(__name__)

@app.route("/")
def hello():
    db=connect()
    cursor = db.cursor()
    cursor.execute("select username from user")
    uname = cursor.fetchone()
    return uname
if __name__=='__main__':
    app.run()


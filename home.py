from flask import Flask ,render_template
from connector import connect
import hashlib


app = Flask(__name__)

@app.route("/home")
def hello():
    uname='rohit'
    upass = hashlib.sha1('hello').hexdigest()
    db=connect()
    cursor = db.cursor()
    cursor.execute("""select * from user where username='%s' and password='%s' """ % (uname,upass))
    result = cursor.fetchone()
    
    return render_template('home.html',tuples=cursor.rowcount)
if __name__=='__main__':
    app.run()



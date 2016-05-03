from flask import Flask ,render_template
from connector import connect

app = Flask(__name__)

@app.route("/home")
def hello():
    db=connect()
    cursor = db.cursor()
    cursor.execute("select * from user")
    user = [dict(uname=row[1],upass=row[2]) for row in cursor.fetchall()]
    return render_template('home.html',user=user)
if __name__=='__main__':
    app.run()



from flask import Flask,render_template,request,session,g,url_for,redirect,flash,abort
from connector import connect

app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def login():
    error = None
    uname = request.form['username']
    upass = request.form['password']
    db = connect()
    cursor = db.cursor()
    result = cursor.execute("select username,password from user where email=%s and password=%s",uname,upass)
    if result == True:
        return redirect(url_for('home.html'))
    return render_template("login.html")
if __name__=='__main__':
    app.run()

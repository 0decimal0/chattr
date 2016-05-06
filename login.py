from flask import Flask,render_template,request,session,g,url_for,redirect,flash,abort
from connector import connect

app=Flask(__name__)

@app.route("/login",methods=['POST','GET'])
def login():
    return render_template('login.html')

@app.route("/home",methods=['POST','GET'])
def submit():
    error = None
    if request.method =='POST':
        uname = request.form['username']
        upass = request.form['password']
    return render_template("home.html",user=uname,passw=upass)

if __name__=='__main__':
    app.run()

from flask import Flask,Blueprint,render_template,request,session,g,url_for,redirect,flash,abort
from connector import connect
import hashlib
import json

app=Flask(__name__)
'''with open('config.json','r') as f:
            data = json.load(f)'''
app.config.from_json('config.json')
app.secret_key = app.config['SECRET_KEY']
auth = Blueprint('authorization',__name__)

@auth.route("/login",methods=['POST','GET'])
def login():
    return render_template("authorization/login.html")

@auth.route("/home",methods=['POST','GET'])
def home():
    error = None
    if request.method =='POST':
        uname = request.form['username']
        upass = request.form['password']
    passwd = hashlib.sha1(upass).hexdigest()
    
    db = connect()
    cursor = db.cursor()
    cursor.execute("""select * from user where email='%s' and password='%s'""" % (uname,passwd))
    result = cursor.fetchone()
    
    '''the rowcount attribute works only after the row has been fetched that is after fetchone() method '''
    number_of_rows = cursor.rowcount

    if number_of_rows != 1:
        flash('Invalid email or password!')
        return redirect(url_for('authorization.login'))
    else:
        return redirect(url_for('authorization.redirecthome'))

@auth.route("/redirecthome",methods=['POST','GET'])
def redirecthome():
    return render_template("authorization/home.html")

if __name__=='__main__':
    app.run()

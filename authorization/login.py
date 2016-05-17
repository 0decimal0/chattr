from flask import Flask,Blueprint,render_template,request,session,g,url_for,redirect,flash,abort
from connector import connect
import hashlib,json,random,string
import smtplib

app=Flask(__name__)

app.secret_key = app.config['SECRET_KEY']
with open('config.json','r') as f:
    data = json.load(f)
host = data['SMTP_HOST']
user = data['SMTP_USER']
upass = data['SMTP_PASS']
auth = Blueprint('authorization',__name__)

@auth.route("/login",methods=['POST','GET'])
def login():
    return render_template("authorization/login.html")

@auth.route("/home",methods=['POST','GET'])
def home():
    error = None
    if request.method =='POST':
        uname = request.form['email']
        upass = request.form['password']
    passwd = hashlib.sha1(upass).hexdigest()
    
    db = connect()
    cursor = db.cursor()
    cursor.execute("""select * from user where email='%s' and password='%s'""" % (uname,passwd))
    result = cursor.fetchone()
    
    '''the rowcount attribute works only after the row has been fetched that is after fetchone() method '''
    number_of_rows = cursor.rowcount
    db.close()

    if number_of_rows != 1:
        flash('Invalid email or password!')
        return redirect(url_for('authorization.login'))
    else:
        return redirect(url_for('authorization.redirecthome'))

@auth.route("/registered",methods=['POST','GET'])
def registered():
    if request.method == 'POST':
        uname = request.form['username']
        email = request.form['email']
        upass = request.form['password']
    db = connect()
    cursor = db.cursor()
    cursor.execute("select count(*) from user")
    sum_rows = cursor.fetchone()
    uid = sum_rows[0]+1
    cursor.execute("""insert into user(userId,username,password,email) values('%d','%s',sha1('%s'),'%s')""" % (uid,uname,upass,email))
    db.commit()
    result = cursor.fetchone()
    rows = cursor.rowcount
    db.close()
    if rows == 1:
        return redirect(url_for('authorization.redirecthome'))
    else:
        return redirect(url_for('authorization.login'))

@auth.route("/resetpass",methods=['POST','GET'])
def resetpass():
    randomstring = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(8))
    if request.method == 'POST':
        receiver = request.form['receiver']
    db = connect()
    cursor = db.cursor()
    cursor.execute("""update user set password=sha1('%s') where email='%s'""" % (randomstring,receiver))
    db.commit()
    db.close()
    try:
        server = smtplib.SMTP(host,25)
        server.ehlo()
        server.starttls()
        server.login(user,upass)
        server.sendmail(user,receiver,randomstring)
        server.close()
        return render_template("authorization/resetpass.html",tuples=receiver)
    except:
        flash("The reset password didn't go through.Please check!, the email is correct!")
        return redirect(url_for('authorization.redirecthome'))
@auth.route("/redirecthome",methods=['POST','GET'])
def redirecthome():
    return render_template("authorization/home.html")

if __name__=='__main__':
    app.run()

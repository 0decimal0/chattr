from flask import Flask ,render_template
from flask.ext.mysql import MySQL
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='rohit123'
app.config['MYSQL_DATABASE_DB']='chattr'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)

@app.route("/")
def hello():
    return "database connected"
@app.route("/login")
def signin():
    return render_template('login.html')
if __name__=='__main__':
    app.run()

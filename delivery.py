from flask import Flask, redirect,  render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='1234'
app.config['MYSQL_DB']='delivery'

mysql=MySQL(app)

@app.route("/",methods=['POST','GET'])
@app.route("/home",methods=['POST','GET'])
@app.route("/index",methods=['POST','GET'])
def welcome():
    if request.method=='POST':
        details=request.form
        first=details["First"]
        last=details["Last"]
        phone=details["Phone"]
        email=details["Email"]
        password=details["Pass"]
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO register(First,Last,Phone,Email,Password) VALUES(%s,%s,%s,%s,%s)",(first,last,phone,email,password))
        mysql.connection.commit()
        return redirect(url_for('welcome'))
    else:
        return render_template('welcome.html')
    

@app.route("/login",methods = ['POST', 'GET'])
def login():
    msg=''
    if request.method=='POST':
        details=request.form
        email=details["login"]
        password=details["Pass"]
        cur=mysql.connection.cursor()
        result=cur.execute("Select * from register where email='%s'",(email))
        user=result.fetchone()
        if user:
            if email==user['Email']:
                if password==user['Password']:
                    return redirect(url_for('v-nv'))
                else:
                    return render_template('login.html',msg='p')
            else:
                return render_template('login.html',msg='user')
        else:
            return render_template('login.html',msg='err')
    else:
        return render_template('login.html')

@app.route("/v-nv",methods = ['POST', 'GET'])
def v_nv():
            return render_template('v-nv.html')

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/veg")
def veg():
    return render_template("veg.html")

@app.route("/nveg")
def nveg():
    return render_template("nveg.html")

if __name__=="__main__":
    app.run(debug=True,port=8000)
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/v-nv")
def v_nv():
    return render_template("v-nv.html")

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
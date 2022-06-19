from flask import Flask, render_template

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/")
def home():
    return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True,port=8000)
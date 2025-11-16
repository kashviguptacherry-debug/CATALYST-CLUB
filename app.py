from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/achievements")
def achievements():
    return render_template("achievements.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/lost-found")
def lost_found():
    return render_template("lost_found.html")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/index.html")
def hello_world2():
    return render_template('index.html')

@app.route("/first_web_page.html")
def first_web_page():
    return render_template('first_web_page.html')

@app.route("/hobby.html")
def hobby():
    return render_template('hobby.html')

@app.route("/recipes/tea.html")
def tea():
    return render_template('./recipes/tea.html')

@app.route("/recipes/noodles.html")
def noodles():
    return render_template('./recipes/noodles.html')



from flask import Flask, render_template

app = Flask(__name__)
@app.route("/eu")

def main():
    return("Idade: 15\nNome: Davi\nsigno: Leao")

@app.route("/professora")

def second():
    return("Idade: 32\nNome: Amanda\nsigno: Capricornio")

@app.route("/rafael")

def third():
    return("Idade: 108\nNome: Rafael\nsigno: virgem")

app.run()
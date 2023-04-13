from flask import Flask, render_template, request

app = Flask(__name__)

def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

@app.route("/")
def homePage():
    name = "Angel"
    return render_template('myHomepage.html', name=name)

@app.route("/form")
def formPage():
    return render_template('detailsPage.html', bigText=readDetails('static/games.txt'))

## When running this file directly...
if __name__ == "__main__":
    app.run(debug=True)
````
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Aqui vão rolar altos ninja</p>"


if __name__ == '__main__':
    app.run(debug=True)
````

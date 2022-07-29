
from flask import Flask, render_template
import pickle


app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def main():
    return 'goti'

if __name__ == '__main__':
    app.run(debug=True, port=5000)

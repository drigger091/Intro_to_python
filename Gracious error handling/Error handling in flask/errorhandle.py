import flask

from flask import Flask , jsonify,abort
from dbapp import fetch_blog, fetch_blogs

app = Flask(__name__)

@app.route('/')
def hello_worlld():
    return "Hello ,world i am doing my error handling"

@app.route('/blogs')
def all_blogs():
    return jsonify(fetch_blogs())

@app.route('/blogs/<id>')
def get_blog(id):
    return jsonify(fetch_blog(id))


if __name__ == "__main__":
    app.run()
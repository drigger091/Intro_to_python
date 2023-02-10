import flask

from flask import Flask , jsonify,abort
from dbapp2 import fetch_blog, fetch_blogs ,Notauthorizederror, Notfounderror

app = Flask(__name__)

@app.route('/')
def hello_worlld():
    return "Hello ,world i am doing my error handling"

@app.route('/blogs')
def all_blogs():
    return jsonify(fetch_blogs())

@app.route('/blogs/<id>')
def get_blog(id):
    try:
        return jsonify(fetch_blog(id))
    except Notfounderror:
        abort(404,description = "Resource not found")
    except Notauthorizederror:
        abort(403, description = "Acces Denied")
#blocks the third block as it is private

if __name__ == "__main__":
    app.run()
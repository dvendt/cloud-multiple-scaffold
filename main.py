from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello!'
    
@app.route('/echo/<name>')
def echo(name):
    print(f"this was placed in the url: {name}")
    val = {"new-name4": name}
    return jsonify(val)
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

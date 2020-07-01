from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Updated World!"

if __name__ == '_main_':
    app.debug = True
    app.run(host='0.0.0.0', port=22, debug=True)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Updated World!"

if _name_ == '_main_':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=True)

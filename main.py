from flask import Flask, jsonify

app = Flask(_name_)

@app.route('/')
def index():
    return "initial API"

if _name_ =='_main_':
    app.run(debug=True)
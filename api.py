from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({'firstName':'matty', 'lastName': 'o', "test":"a thing", "sub_thing": {"test2":"value2"}})

app.run()

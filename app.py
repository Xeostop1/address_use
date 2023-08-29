from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/get-api-key", methods=["GET"])
def get_api_key():
    return {"api_key": "138657343210935212"}


if __name__ == "__main__":
    app.run(debug=True)

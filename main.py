from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/rotate")
def rotate():
    return "Rotado"

if __name__ == "__main__":
    app.run(debug = True)


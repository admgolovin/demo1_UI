from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['POST'])
def add_message():
    print(request.data)
    content = request.json
    print(content)
    return ""


if __name__ == '__main__':
    app.run(port=5001, debug=True)
from flask import Flask, request, jsonify
import json
app = Flask(__name__)


@app.route('/', methods=['POST'])
def add_message():
	print(request.data)
	test = request.json
	print(test)
	try:
		content = json.loads(request.data.decode())
		print(content)
	except Exception:
		print("Error")
	return ""


if __name__ == '__main__':
	app.run(port=5001, debug=True)
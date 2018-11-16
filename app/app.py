import flask
import requests
import json

POST_SERVICE_URL = ""
VIEW_SERVICE_URL = ""
app = flask.Flask(__name__)
SEND_DATA_FMT = {"Departament":
			{"name": None},
		"Team": {"depart_id": None,
			"name": None,
			"manager_id": None},
		"Employee": {"team_id": None,
			"name": None,
			"sname": None,
			"exp": None,
			"position": None,
			"salary": None,
			"coefficient": None}}


def get_info():
	response = requests.get(VIEW_SERVICE_URL)
	return response.json()


def send_info(info: dict):
	info = json.dumps(info)
	response = requests.post(POST_SERVICE_URL, data=info)


@app.route("/")
def index():
	return flask.render_template("index.html")


@app.route("/give-salary")
def give_salary():
	salaries = get_info()


@app.route("/create-departament")
def create_departament():
	pass


@app.route("/create-team")
def create_team():
	pass


@app.route("/hire-employee")
def hire_employee():
	pass


if __name__ == '__main__':
	app.run(debug=True)

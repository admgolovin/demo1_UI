import flask
import requests
import json

POST_SERVICE_URL = ""
VIEW_SERVICE_URL = ""
app = flask.Flask(__name__)
SEND_DATA_FMT = {"departament":
			{"name": None},
		"team": {"depart_id": None,
			"name": None,
			"manager_id": None},
		"employee": {"team_id": None,
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
	if response.status_code == 200:
		return True
	else:
		return False


@app.route("/")
def index():
	return flask.render_template("index.html")


@app.route("/salaries")
def give_salary():
	# salaries = get_info()
	data = {"id": 1, "name": "Departament 1", "teams": [{"id": 1, "name": "Ludi 1", "employees": [{"id": 1, "name": "Andrew", "sname": "Popov", "exp": 3, "position": "vasia", "salary": 10}, {"id": 2, "name": "Andrew2", "sname": "Popov2", "exp": 3, "position": "v2asia", "salary": 210}]}, {"id": 2, "name": "Assasins", "employees": [{"id": 1, "name": "Dikaya", "sname": "AAAXXX", "exp": 3, "position": "vasia", "salary": 10}, {"id": 2, "name": "Chert", "sname": "ZZZZ", "exp": 3, "position": "v2asia", "salary": 210}]}]}
	return flask.render_template("salaries.html", company=[data, data])


def	parse_form(key, form):
	data2sent = dict(SEND_DATA_FMT)
	for i in SEND_DATA_FMT[key]:
		if i not in form:
			return False
		data2sent[key][i] = form[i]
	for i in data2sent:
		if i != key:
			data2sent[i] = None
	return data2sent


@app.route("/create-departament", methods=['POST'])
def create_departament():
	print(flask.request.form)
	data2sent = parse_form('departament', flask.request.form)
	if data2sent:
		# send_info(data2sent)
		print(data2sent)
		return flask.make_response(("OK", 200))
	return flask.make_response(("ERROR", 200))


@app.route("/create-team", methods=['POST'])
def create_team():

	return flask.make_response(("OK", 200))


@app.route("/hire-employee", methods=['POST'])
def hire_employee():
	return flask.make_response(("OK", 200))


if __name__ == '__main__':
	app.run(debug=True)

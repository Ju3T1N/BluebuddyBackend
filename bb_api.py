import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
	return '''<h1>API</h1>'''


@app.route('/api/all', methods=['GET'])
def api_all():
	"""
	API Requests come in the form of a suburl like this
	"""
	return 1



@app.errorhandler(404)
def page_not_found(e):
	"""
	This one is self explanatory
	"""
	return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
	"""
	query_parameters is the equivilent of commandline args for apis
	"""
	query_parameters = request.args
	return 0

app.run()

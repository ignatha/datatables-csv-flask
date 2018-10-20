from flask import Flask, request, jsonify, render_template, url_for
import csv

app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')

@app.route("/api")
def api():
	data = {}
	csvs = [row for row in csv.reader(open('pencairan-pedesaan.csv', 'r'))]
	data['data'] = csvs
	return jsonify(data)


if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
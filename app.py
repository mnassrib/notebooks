from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/time-series-forecasting')
def timeseriesforecasting():
	return render_template("time-series-forecasting.html")

@app.route('/developing-lstm-models-for-rime-series-forecasting')
def lstmtimeseriesforecasting():
	return render_template("developing-lstm-models-for-rime-series-forecasting.html")

if __name__ == '__main__':
	app.run(debug=True)
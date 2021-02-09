from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/time-series-forecasting')
def timeseriesforecasting():
	return render_template("time-series-forecasting.html")

@app.route('/developing-lstm-models-for-time-series-forecasting')
def lstmtimeseriesforecasting():
	return render_template("developing-lstm-models-for-time-series-forecasting.html")


# @app.route('/developing-lstm-models-for-tsf')
# def lstmtsf():
# 	return render_template("developing-lstm-models-for-tsf.html")

# @app.route('/tsf')
# def tsf():
# 	return render_template("tsf.html")


if __name__ == '__main__':
	app.run(debug=True)
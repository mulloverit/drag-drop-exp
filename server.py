from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def show_index():
	"""Show index page"""

	return render_template("index.html")

@app.route("/draggable")
def draggable_experiments():
	"""Experimenting with Draggable.js library"""

	return render_template("draggable.html")

@app.route("/interactive")
def interactive_experiments():
	"""Experiementing with Interactive.js library"""

	return render_template("interact.html")

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")

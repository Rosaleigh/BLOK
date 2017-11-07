from flask import Flask, render_template, request

app=Flask('Blok_app')
@app.route("/")

def home():
	return render_template("home_test.html")

app.run(debug=True)
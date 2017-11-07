from flask import Flask , render_template,request
from focusapi import  solution
from datetime import datetime
import json

app = Flask("Blok_app")


@app.route("/") 
def default_path():
	return render_template ("index.html") #This 


# 1. From the webpage take DOB as input
# 2. Using the DOB identify Zodiac Sign - The function to calculate sign is in horoscope_api.py to use this fuction we need to import see line 2
# 3. Once Sign is identified, we have a function that call REST API to get horoscope for the sign
# 4. The response from the API is in json format (baically name:value pair e.g {sign:leo, day:today})
# 5. Pass json data to the target HTML page that has logic to read data from the json
@app.route("/exercise", methods=["POST"])
def read_form():
	form_data = request.form["howmuchtime"]
	form_data = json
	#time = raw_input(form_data["howmuchtime"], '%d').time()
	time = raw_input(form_data["howmuchtime"])
	time = int(time)
	print time
	result= solution (time)
	print result
	return render_template ("exercise.html",data=data) 
	#return "All OK"





app.run(debug=True)
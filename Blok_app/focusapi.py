import requests
from datetime import datetime

import json


#Function that takes month and a day and calcuates Zodiac sign
def solution(time):
	



	if time == 10:
		result = '10 minute yoga https://www.youtube.com/watch?v=Nnd5Slo02us'
	elif time== 20:
		result = '20 minute meditation https://www.youtube.com/watch?v=-2zdUXve6fQ'
	elif time== 30:
		result = '30 minute yoga https://www.youtube.com/watch?v=xe3D7vKvtok'
	elif time == 40:
		result = '40 minute meditation https://www.youtube.com/watch?v=_vN3wkatdts'
	elif time == 50:
		result = '50 minute yoga https://www.youtube.com/watch?v=aIMyEoHmeio'
	elif time == 60:
		result = '60 minute meditation https://www.youtube.com/watch?v=dmNJKvF0TEY'

	print("You have %d minutes, clear your head with:" %time ,result)
	print(result)
	return result
	return render_template ("exercise.html",data=data) 

def get_time(time):

	params = ( 
	('time', time))

	# aztro provide free API to get horoscope for a sign - 
	#API takes two param 1.sign (example values cancer, leo etc)  2. day possible values today, tomorrow etc
	response = requests.post("exercise.html", params=params)

	print response.url
	print response.status_code
	print response.headers["content-type"]
	json_data = response.json()
	#json is raw data which contains all the data from the api response
	return json_data




from flask import Flask, redirect, request, render_template
import requests
app = Flask("Blok_app")

REDIRECT_URI="http://localhost:5000/spotifylogin"
CLIENT_ID="daca329ab84b4e2d9a5e1f5ed2157b6e"
CLIENT_SECRET="32b2a9756e22434b8287567023f22e84"

@app.route("/compose")
def hello():
    return render_template('compose.html')
   #return redirect("https://accounts.spotify.com/authorize?client_id=" + CLIENT_ID +"&response_type=code&redirect_uri=" + REDIRECT_URI)

@app.route("/spotifylogin")
def login():
    auth_code = request.args.get('code')
    print auth_code
    auth_body = {'grant_type': 'authorization_code', 'code': auth_code, 'redirect_uri': REDIRECT_URI,'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}
    
    auth_response = requests.post("https://accounts.spotify.com/api/token", data=auth_body)
    # auth=(CLIENT_ID, CLIENT_SECRET))
    print auth_response.json()
    access_token =  auth_response.json()['access_token']
    expires_in = auth_response.json()['expires_in']
    refresh_token =  auth_response.json()['refresh_token']

    authorization_header = {"Authorization": "Bearer " + access_token}


    result = get_artist("shakira", authorization_header)
    print result
    return render_template('compose.html')

@app.route("/searchresults")
def something_sensible():
    
    auth_body = {'grant_type': 'client_credentials','client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}
    auth_response = requests.post("https://accounts.spotify.com/api/token", data=auth_body)
    print auth_response.json()
    access_token =  auth_response.json()['access_token']
    expires_in = auth_response.json()['expires_in']
    

    authorization_header = {"Authorization": "Bearer " + access_token}


    result = get_artist("shakira", authorization_header)
    print result
    return render_template('compose.html')




def get_artist(artist_name, authorization_header):
    api_request = requests.get("https://api.spotify.com/v1/search?type=artist&q="+artist_name, headers = authorization_header)
    return api_request.json()






    
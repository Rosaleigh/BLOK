from flask import Flask, render_template
from random import randint
import requests
import json
import pdb

import tweepy

app=Flask('Blok_app')

def get_tweets():
    auth = tweepy.OAuthHandler("sSkTtevERXGFVL8d4rpBHof9F","ak98dOFuTmIVmBmFkKAU6pjp6rVRqT2RaZyJpICRE7hqOBE009")
    auth.set_access_token ("701757037-V2HnyUMzMKS4BCP5el2S7HvfazRUYeKsJ2www5nO", "lQrIyI7QBtIV3BIeZ2XSF8SKg4967CXqY9nxYYiMge5g6")
    twitter_api = tweepy.API(auth)
    review_tweets = twitter_api.search(q = "guardianreview") #Twitter handle you want to search by
    print review_tweets
    return review_tweets


@app.route('/write')
def print_tweets():
    review_tweets = get_tweets()
    for tweet in review_tweets:
        print tweet.user.name + ": " + tweet.text +"\n"
    return render_template("write.html", review_tweets = review_tweets)


app.run(debug=True)


# wordList1 = ["Enchanting", "Amazing", "Colourful", "Delightful", "Delicate"]
# wordList2 = ["visions", "distance", "conscience", "process", "chaos"]
# wordList3 = ["superstitious", "contrasting", "graceful", "inviting", "contradicting", "overwhelming"]
# wordList4 = ["true", "dark", "cold", "warm", "great"]
# wordList5 = ["scenery","season", "colours","lights","Spring","Winter","Summer","Autumn"]
# wordList6 = ["undeniable", "beautiful", "irreplaceable", "unbelievable", "irrevocable"]
# wordList7 = ["inspiration", "imagination", "wisdom", "thoughts"]
		
# wordIndex1=randint(0, len(wordList1)-1)
# wordIndex2=randint(0, len(wordList2)-1)
# wordIndex3=randint(0, len(wordList3)-1)
# wordIndex4=randint(0, len(wordList4)-1)
# wordIndex5=randint(0, len(wordList5)-1)
# wordIndex6=randint(0, len(wordList6)-1)
# wordIndex7=randint(0, len(wordList7)-1)

# haiku = wordList1[wordIndex1] + " " + wordList2[wordIndex2] + ",\n" 
# haiku = haiku + wordList3[wordIndex3] + " " + wordList4[wordIndex4] + " " + wordList5[wordIndex5]  + ",\n"
# haiku = haiku + wordList6[wordIndex6] + " " + wordList7[wordIndex7] + "."

# print(haiku)

# @app.route("/write/poem")
# def print_haiku():
# 	print haiku
# 	return haiku 
# 	return render_template("write.html", haiku = print_haiku)

# print_haiku()

app.run(debug=True)
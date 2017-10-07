import facebook
import urllib
import requests

token = "EAACEdEose0cBANfFvfniSYtu2sjnoxA5VvPqxZAgi8Gs9F3zGM3p79mDPKxt9XKGGZA86TqyOhaOZBrUfHUNdpKv6GilS8LeEYTSN0q8ecxUMm8GzzL6IOrhGVsePKuZBoR1nUdkg11UNbElKmGHTZBgJosWhMNM6726k2YtFHaMbeLyZBbfBqGoLEY91beSgJaROuukb4fwZDZD"

graph = facebook.GraphAPI(access_token=token)
fields = 'link,images'
post = graph.get_object(id=10154781019457991, fields = fields)
link = post['images'][0]['source']

def get_image_from_url(url):

	resource = urllib.urlopen(url)
	output = open("file01.jpg","wb")
	output.write(resource.read())



img = get_image_from_url(link)





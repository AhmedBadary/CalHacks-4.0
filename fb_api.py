import facebook
import urllib
import requests
import pdb

token = "EAACEdEose0cBAFb8tXvSvwwkpjUZAwhTW6pIIItS8dZBbWHumwykvNjBIoAzn1EcQUn5TPpMUK5QbGranREagcROWGIuft0UZAO8SEKsTScMTdf0bHIFHxEQ06IRZA5LBV9JxZCItICPh0Jg7VAPvQPRBviKPrT0PZAKwZARkBYmQUUY96H1K54xiWhgb4zik4awBvjSDKyFQZDZD"

graph = facebook.GraphAPI(access_token=token)
fields = 'link,images'
# This id is currently hardcoded
post = graph.get_object(id=10154781019457991, fields = fields)
link = post['images'][0]['source']

def save_image_from_url(url, filename="file01.jpg"):

    resource = urllib.urlopen(url)
    output = open(filename,"wb")
    output.write(resource.read())



img = save_image_from_url(link)

fields = 'link'
ian = graph.get_object(id='me', fields=fields)
all_photos = graph.get_connections(id='me', connection_name="photos")
#timeline_url = ian['link']
#timeline = graph.get_object(timeline_url)

def save_all_photos():

    all_photos = graph.get_connections(id='https://www.facebook.com/ian.mcaulay.79', connection_name='photos')
    all_photos = all_photos['data']
    for i, photo in enumerate(all_photos):
        id = photo['id']
        img = graph.get_object(id=id, fields='images')
        link = img['images'][0]['source']
        resource = urllib.urlopen(link)
        filename = "all_ian_photos/photo" + str(i) + ".jpg"
        output = open(filename,"wb")
        output.write(resource.read())
        #pdb.set_trace()




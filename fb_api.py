import facebook
import urllib
import requests
import pdb

# Ian's token
#token = "EAACEdEose0cBAFb8tXvSvwwkpjUZAwhTW6pIIItS8dZBbWHumwykvNjBIoAzn1EcQUn5TPpMUK5QbGranREagcROWGIuft0UZAO8SEKsTScMTdf0bHIFHxEQ06IRZA5LBV9JxZCItICPh0Jg7VAPvQPRBviKPrT0PZAKwZARkBYmQUUY96H1K54xiWhgb4zik4awBvjSDKyFQZDZD"
# Anish's token
token = "EAACEdEose0cBAFkaMJJTBnV6U2aUeUxHBeaalVICJgd61EZCX7HieZCUZB4sgrQfNuJ3x07U2T2L765gUbU9sZC362uZAGc7s8D9dIfaeXc1K82wzIwMXumtESvfxp1f7d2SvehwLeCK5qWc7Iuc62njjXeBz20G9B13reUcZAjhntuBzqZCPs5jPlQE72CQevw7ZBLaYRZB0uQZDZD"

graph = facebook.GraphAPI(access_token=token)


def save_all_photos(folder='all_ian_photos', limit=100):

    all_photos = graph.get_connections(id='me', connection_name='photos')
    all_photos = all_photos['data'][:limit]
    for i, photo in enumerate(all_photos):
        img = get_img_from_fb_photo(photo)
        filename = folder + "/photo" + str(i) + ".jpg"
        output = open(filename,"wb")
        output.write(img)

def get_img_from_fb_photo(photo):
    id = photo['id']
    img = graph.get_object(id=id, fields='images')
    link = img['images'][0]['source']
    resource = urllib.urlopen(link)
    return resource.read()




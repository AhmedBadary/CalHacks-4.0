import facebook
import urllib
import requests
import pdb
import msft_api as msft

# Ian's token
token = "EAACEdEose0cBAPVw3LVFG02zgq98QuLPVmdOlyy9ZCEKVbX6LuHXcVdcZBErcCqPUhHAD4iNxQFWvSExjH5PW1DLBtrB3zuMqKLgf8H3FKlQ3ZBXXfTaSPKbtSCy31BpY87ECmLtVKT6LqYeggkriLX13dHen26sZCtgZCIrPZAtZB79VyxcDWfmyVUU0XtHIvBB5cnKUzZCVEj7aP2mdVKwpTktVbV8NkjbfOkmWiEBpAZDZD"
# Anish's token
#token = "EAACEdEose0cBAFkaMJJTBnV6U2aUeUxHBeaalVICJgd61EZCX7HieZCUZB4sgrQfNuJ3x07U2T2L765gUbU9sZC362uZAGc7s8D9dIfaeXc1K82wzIwMXumtESvfxp1f7d2SvehwLeCK5qWc7Iuc62njjXeBz20G9B13reUcZAjhntuBzqZCPs5jPlQE72CQevw7ZBLaYRZB0uQZDZD"

# oauth
#https://www.facebook.com/v2.10/dialog/oauth?
#  client_id={app-id}
#  &redirect_uri={redirect-uri}


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
    #id = photo['id']
    #img = graph.get_object(id=id, fields='images')
    #link = img['images'][0]['source']
    #pdb.set_trace()
    url = get_url_from_fb_photo(photo)
    resource = urllib.urlopen(url)
    msft.print_data(msft.get_msft_data(url))
    return resource.read()

def get_url_from_fb_photo(photo):
    id = photo['id']
    img = graph.get_object(id=id, fields='images')
    # The first image is the highest res one
    url = img['images'][0]['source']
    return url

all_photos = graph.get_connections(id='me', connection_name='photos')
all_photos = all_photos['data']
p1 = all_photos[0]
url1 = get_url_from_fb_photo(p1)
data1 = msft.get_msft_data(url1)





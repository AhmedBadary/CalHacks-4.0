import facebook
import urllib
import requests
import pdb

# Ian's token
token = "EAACEdEose0cBAPVw3LVFG02zgq98QuLPVmdOlyy9ZCEKVbX6LuHXcVdcZBErcCqPUhHAD4iNxQFWvSExjH5PW1DLBtrB3zuMqKLgf8H3FKlQ3ZBXXfTaSPKbtSCy31BpY87ECmLtVKT6LqYeggkriLX13dHen26sZCtgZCIrPZAtZB79VyxcDWfmyVUU0XtHIvBB5cnKUzZCVEj7aP2mdVKwpTktVbV8NkjbfOkmWiEBpAZDZD"
# Anish's token
#token = "EAACEdEose0cBAFkaMJJTBnV6U2aUeUxHBeaalVICJgd61EZCX7HieZCUZB4sgrQfNuJ3x07U2T2L765gUbU9sZC362uZAGc7s8D9dIfaeXc1K82wzIwMXumtESvfxp1f7d2SvehwLeCK5qWc7Iuc62njjXeBz20G9B13reUcZAjhntuBzqZCPs5jPlQE72CQevw7ZBLaYRZB0uQZDZD"

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
    pdb.set_trace()
    resource = urllib.urlopen(link)
    return resource.read()






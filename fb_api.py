import facebook
import urllib
import requests
import pdb
import msft_api as msft

app_id = 668593746670063
app_secret = "42a9a1eb631e943ee5f9aa340bec51b8"

# Ian's token
token = "EAACEdEose0cBAPVw3LVFG02zgq98QuLPVmdOlyy9ZCEKVbX6LuHXcVdcZBErcCqPUhHAD4iNxQFWvSExjH5PW1DLBtrB3zuMqKLgf8H3FKlQ3ZBXXfTaSPKbtSCy31BpY87ECmLtVKT6LqYeggkriLX13dHen26sZCtgZCIrPZAtZB79VyxcDWfmyVUU0XtHIvBB5cnKUzZCVEj7aP2mdVKwpTktVbV8NkjbfOkmWiEBpAZDZD"
# Anish's token
#token = "EAACEdEose0cBAFkaMJJTBnV6U2aUeUxHBeaalVICJgd61EZCX7HieZCUZB4sgrQfNuJ3x07U2T2L765gUbU9sZC362uZAGc7s8D9dIfaeXc1K82wzIwMXumtESvfxp1f7d2SvehwLeCK5qWc7Iuc62njjXeBz20G9B13reUcZAjhntuBzqZCPs5jPlQE72CQevw7ZBLaYRZB0uQZDZD"

# oauth
#https://www.facebook.com/v2.10/dialog/oauth?
#  client_id={app-id}
#  &redirect_uri={redirect-uri}






def get_fb_token():           
    payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    #print file.text #to test what the FB api responded with    
    result = file.text.split("=")[1]
    #print file.text #to test the TOKEN
    return result


def save_all_photos(token, limit=100):

    graph = facebook.GraphAPI(access_token=token)

    all_photos = graph.get_connections(id='me', connection_name='photos')
    all_photos = all_photos['data'][:limit]
    
    all_imgs = [get_img_from_fb_photo(photo) for photo in all_photos]
    return all_imgs

    # all_imgs = []
    # for i, photo in enumerate(all_photos):
    #     img = get_img_from_fb_photo(photo)
    #     return img
    #     #filename = folder + "/photo" + str(i) + ".jpg"
    #     #output = open(filename,"wb")
    #     #output.write(img)
    # return all_imgs

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


#all_photos = graph.get_connections(id='me', connection_name='photos')
##all_photos = all_photos['data']
#p1 = all_photos[0]
#url1 = get_url_from_fb_photo(p1)
#data1 = msft.get_msft_data(url1)





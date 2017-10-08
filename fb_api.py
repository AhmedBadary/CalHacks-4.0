import facebook
import urllib
import requests
import pdb
import msft_api as msft
from webbrowser import open_new


app_id = "668593746670063"
app_secret = "42a9a1eb631e943ee5f9aa340bec51b8"

# Ian's token
token = "EAACEdEose0cBAIQfZBxzgu78fIgUfnCQWm8kS7W0XaVJAgQ0LKKZAG3mEOA1ZAKcYM8JHAoAYeZAPouhlCJh2VY8Wb3fWOBtdS7ZA81aWefvg2X4XelYQ5Dk97klhqpOkYgsJYHvOk7UVv7l59Rlwmzb7FqcJwbAZCVwByGJnW692vVOILgywa0m89e2DQaOV1e3t9lnD4iQZDZD"
# Anish's token
#token = "EAACEdEose0cBAFkaMJJTBnV6U2aUeUxHBeaalVICJgd61EZCX7HieZCUZB4sgrQfNuJ3x07U2T2L765gUbU9sZC362uZAGc7s8D9dIfaeXc1K82wzIwMXumtESvfxp1f7d2SvehwLeCK5qWc7Iuc62njjXeBz20G9B13reUcZAjhntuBzqZCPs5jPlQE72CQevw7ZBLaYRZB0uQZDZD"

# oauth
#https://www.facebook.com/v2.10/dialog/oauth?
#  client_id={app-id}
#  &redirect_uri={redirect-uri}

def test_login():
    #url = "https://www.facebook.com/v2.10/dialog/oauth?client_id={app-id}
#  &redirect_uri={redirect-uri}
    redirect = "http://localhost:8080/"
    url = ('https://graph.facebook.com/v2.2/oauth/' 
        + 'access_token?client_id=' + app_id + '&redirect_uri=' 
        + redirect + '&client_secret=' + app_secret)
    open_new(url)
    #pdb.set_trace()

# GRAPH_API_AUTH_URI = ('https://graph.facebook.com/v2.2/oauth/' 
# + 'access_token?client_id=' + self.app_id + '&redirect_uri=' 
# + REDIRECT_URL + '&client_secret=' + self.app_secret + '&code=')

    #ET https://graph.facebook.com/oauth/access_token?
    #        client_id=YOUR_APP_ID
    #       &client_secret=YOUR_APP_SECRET
    #       &grant_type=client_credentials


def get_fb_token():           
    payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    #print file.text #to test what the FB api responded with    
    result = file.text.split("=")[1]
    #print file.text #to test the TOKEN
    return result

def get_urls_and_captions(token=token, limit=100):

    graph = facebook.GraphAPI(access_token=token)
    all_photos = graph.get_connections(id='me', connection_name='photos')
    all_photos = all_photos['data'][:limit]
    urls = [get_url_from_photo(graph, photo) for photo in all_photos]
    captions = [msft.get_msft_data(url, face=False) for url in urls]
    pdb.set_trace()
    output = zip(urls, captions)
    return output


def get_all_photos(token=token, limit=100):

    graph = facebook.GraphAPI(access_token=token)

    all_photos = graph.get_connections(id='me', connection_name='photos')
    all_photos = all_photos['data'][:limit]
    
    all_imgs = [get_img_from_fb_photo(graph, photo) for photo in all_photos]
    return all_imgs


def save_imgs(imgs, folder='all_ian_photos'):
    for i, img in enumerate(imgs):
        filename = folder + "/photo" + str(i) + ".jpg"
        output = open(filename,"wb")
        output.write(img)


def get_img_from_fb_photo(graph, photo):
    #id = photo['id']
    #img = graph.get_object(id=id, fields='images')
    #link = img['images'][0]['source']
    #pdb.set_trace()
    url = get_url_from_photo(graph, photo)
    #print(url)
    resource = urllib.urlopen(url)
    #msft.print_data(msft.get_msft_data(url))
    return resource.read()

def get_url_from_photo(graph, photo):
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





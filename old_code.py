
#fields = 'link,images'
# This id is currently hardcoded
#post = graph.get_object(id=10154781019457991, fields = fields)
#link = post['images'][0]['source']

#img = save_image_from_url(link)

#fields = 'link'
#ian = graph.get_object(id='me', fields=fields)
#all_photos = graph.get_connections(id='me', connection_name="photos")
#timeline_url = ian['link']
#timeline = graph.get_object(timeline_url)

#def save_image_from_url(url, filename="file01.jpg"):

#    resource = urllib.urlopen(url)
 #   output = open(filename,"wb")
  #  output.write(resource.read())

    # all_imgs = []
    # for i, photo in enumerate(all_photos):
    #     img = get_img_from_fb_photo(photo)
    #     return img
    #     #filename = folder + "/photo" + str(i) + ".jpg"
    #     #output = open(filename,"wb")
    #     #output.write(img)
    # return all_imgs


    def get_fb_token(code):
    #url = "https://www.facebook.com/v2.10/dialog/oauth?client_id={app-id}
#  &redirect_uri={redirect-uri}
    redirect = "google.com"
    url = ('https://graph.facebook.com/v2.2/oauth/' 
        + 'access_token?client_id=' + app_id + '&redirect_uri=' 
        + redirect + '&client_secret=' + app_secret + '&code=' + code)
    token = get_access_token_from_url(url)
    pdb.set_trace()
    return token


# def get_fb_token2(code):           
#     payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
#     file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
#     pdb.set_trace()
#     #print file.text #to test what the FB api responded with    
#     result = file.text.split("=")[1]
#     #print file.text #to test the TOKEN
#     return result
    
def get_access_token_from_url(url):
    """
    Parse the access token from Facebook's response
    Args:
        uri: the facebook graph api oauth URI containing valid client_id,
             redirect_uri, client_secret, and auth_code arguements
    Returns:
        a string containing the access key 
    """
    #token = str(urlopen(url).read(), 'utf-8')
    token = ""
    return token.split('=')[1].split('&')[0]

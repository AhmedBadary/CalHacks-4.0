import httplib, urllib, base64, json
from time import sleep

face_sub_key = "14ae1355d65940dcb149b368e87d1ab9"
caption_sub_key = "62c50af7ffc34aa5ac021e9cbb05badd"
uri_base = 'westcentralus.api.cognitive.microsoft.com'

# Request headers.
face_headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': face_sub_key,
}
caption_headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': caption_sub_key,
}

# Request parameters.
face_params = urllib.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
})
caption_params = urllib.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Categories,Description,Color',
    'language': 'en',
})


def get_msft_data(url, face=True):
    # If face is true, this will return the face analysis
    # data, otherwise it will return generated caption

    # The URL of a JPEG image to analyze.
    body = "{'url':'" + url + "'}"
    #body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/c/c3/RH_Louise_Lillian_Gish.jpg'}"

    try:
        # Execute the REST API call and get the response.
        conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        
        if face:
            conn.request("POST", "/face/v1.0/detect?%s" % face_params, body, face_headers)
        else:
            conn.request("POST", "/vision/v1.0/analyze?%s" % caption_params, body, caption_headers)
            sleep(1) # Avoid rate limit

        response = conn.getresponse()
        # 'data' contains the JSON data. The following formats the JSON data for display.
        data = response.read()
        conn.close()
        return data 

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def print_data(data):
    parsed = json.loads(data)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))






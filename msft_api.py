import httplib, urllib, base64, json

subscription_key = "14ae1355d65940dcb149b368e87d1ab9"
uri_base = 'westcentralus.api.cognitive.microsoft.com'

# Request headers.
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters.
params = urllib.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
})



def get_msft_data(url):

    # The URL of a JPEG image to analyze.
    body = "{'url':'" + url + "'}"
    #body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/c/c3/RH_Louise_Lillian_Gish.jpg'}"

    try:
        # Execute the REST API call and get the response.
        conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
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





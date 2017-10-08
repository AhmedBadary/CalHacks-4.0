from flask import Flask
import fb_api as fb
import requests

horus = Flask(__name__)


@horus.route('/')
def hello():
	return "Hello World!"

@horus.route('/get_images')
def get_image():
	return fb.save_all_photos()

@horus.route('/login/<code>')
def gen_token(code):
	token = fb.get_fb_token()
	return fb.save_all_photos(token)



if __name__ == "__main__":
	horus.run()







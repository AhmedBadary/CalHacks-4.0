from flask import Flask
horus = Flask(__name__)


@horus.route('/')
def hello():
	return "Hello World!"

if __name__ == "__main__":
	horus.run()








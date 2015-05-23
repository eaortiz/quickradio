from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
	return "Click this link for \
	<a href = '/static/04NoCreo.m4a'> \
	the Shakira song. </a>"

if __name__ == '__main__':
	app.run()
	url_for('static', filename='04NoCreo.m4a')


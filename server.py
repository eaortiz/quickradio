from flask import Flask, url_for, render_template
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
	return render_template('ligths.html')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
	url_for('static', filename='binary')
	url_for('static', filename='binarytiny')

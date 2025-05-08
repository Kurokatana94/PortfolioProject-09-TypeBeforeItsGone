from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap5
import datetime as dt
import requests
from wonderwords import RandomSentence
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap5(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get-sentence')
def get_sentence():
    result = requests.get('https://thequoteshub.com/api/random-quote').json()
    text = result['text']
    author = result['author']
    return jsonify({'text': text, 'author': author})
if __name__ == '__main__':
    app.run(debug=True)
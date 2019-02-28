from flask import Flask, request, jsonify
import random
import requests

app = Flask(__name__)

cat_api = "https://api.thecatapi.com/v1/images/search?mime_types=jpg"
dog_api = "https://dog.ceo/api/breeds/image/random"

@app.route('/')
def index():
    cat_url = requests.get(cat_api).json()[0]['url']
    dog_url = requests.get(dog_api).json()['message']
    dog_json = jsonify({"species": "dog", "url": dog_url})
    cat_json = jsonify({"species": "cat", "url": cat_url})
    random_url = random.choice([dog_json, cat_json])
    return random_url

@app.route('/cat')
def cat():
    cat_url = requests.get(cat_api).json()[0]['url']
    return jsonify({"url": cat_url})

@app.route('/dog')
def dog():
    dog_url = requests.get(dog_api).json()['message']
    return jsonify({"url": dog_url})

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)

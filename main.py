import os
from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://www.epochconverter.com/')
    soup = BeautifulSoup(response.content, "html.parser")
    quotes = soup.find_all("div", id="ecclock", class_="ecclock")
    return "Current Epoch Time is: {}".format(quotes[0].getText())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

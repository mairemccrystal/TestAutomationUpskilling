import os
from http import client
import http.client, urllib.request, urllib.parse, urllib.error, base64

from flask import Flask, render_template, send_file
import selenium.webdriver as webdriver
import main
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/results',  methods=['POST', 'GET', 'PUT'])
def searchForImages():
    url = "https://www.ebay.co.uk/"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    # browser = webdriver.Chrome(chrome_options=chrome_options)
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)

    search_box = browser.find_element_by_xpath("//input[@type='text']")
    search_box.clear()
    search_box.send_keys("pastel blue dress")
    search_box.submit()
   # return main.get_results("pink dress")

    arr = []
    x = -1
    for i in range(9, 34):
        img = browser.find_element_by_xpath("(//img[@class='s-item__image-img'])[" + str(i) + "]")
        src = img.get_attribute("src")

        import urllib.request
        urllib.request.urlretrieve(src, "static/images/" + str(i) + ".png")

        arr.append(str(i))
        x = x + 1
 #   return str(arr)

    return render_template('imageresults.html', search_results=arr)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)

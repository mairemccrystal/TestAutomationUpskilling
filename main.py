from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_results(search_term):
    url = "https://www.ebay.co.uk/"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
   # browser = webdriver.Chrome(chrome_options=chrome_options)
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)

    search_box = browser.find_element_by_xpath("//input[@type='text']")
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.submit()

    newImages = []
    for x in range(9, 12):
        newImages.append(x)
    return str(newImages(x))

    # return urltext
   # return results

get_results("vintage toys")
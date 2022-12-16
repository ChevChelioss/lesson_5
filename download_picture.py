import os.path
import time

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 2 with abs path
current_dir = os.path.dirname(os.path.abspath(__file__))

picture_test_dir = os.path.join(current_dir, 'picture_test')

options = webdriver.ChromeOptions()
prefs = {
    'download.default_directory': picture_test_dir,
    'download.prompt_for_download': False
}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver

browser.open('https://demoqa.com/upload-download')
browser.element('#downloadButton').click()
time.sleep(2)
samplefile = os.path.join(picture_test_dir, 'sampleFile.jpeg')

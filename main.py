# https://faun.pub/how-to-install-selenium-in-linux-e8928b2b709
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime

# Set path Selenium
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
s = Service(CHROMEDRIVER_PATH)
WINDOW_SIZE = "1920,1080"

# Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get("https://iam-py-test.github.io/malware/")
malware = driver.find_element(By.LINK_TEXT, "malware")
webdriver.ActionChains(driver).click_and_hold(malware).perform()
driver.save_screenshot("test.png")
driver.close()

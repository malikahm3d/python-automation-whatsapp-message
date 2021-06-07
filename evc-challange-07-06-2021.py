#Python automation with selenium.
#open browser, go to whatsapp, find contact, click on them, punch in and send message.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#imports from docs and tutoroials

driver = webdriver.Chrome('/home/malikahm3d/chromedriver')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
#setting up browser

target = '"contact\'s name"'
#contact

string = "message"
#message
  
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
#look through HTML elements for a span
#with title of equals to our contact's name
#when found, assign it to veriable and click it

inp_xpath = '//div[@data-tab="6"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
input_box.send_keys(string + Keys.ENTER)
#look through HTML elements for a div
#that has attribute of data-tab equals to 6
#when found, feed the message to it and press enter
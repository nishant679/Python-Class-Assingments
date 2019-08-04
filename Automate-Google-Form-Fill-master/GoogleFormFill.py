from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
import time

name = "NISHANT KUMAR"
user_details = "I am a computer science student at NIT Trichy"

#BROWSER : FIREFOX
driver = webdriver.Firefox()
driver.get("https://forms.gle/Y8HhaedsevFm9fww5")
time.sleep(2)


#facebook login
username = driver.find_element_by_name("entry.1996697983")
username.send_keys(name)
time.sleep(2)
details = driver.find_element_by_name("entry.707845717")
details.send_keys(user_details)
time.sleep(2)

login = driver.find_element_by_tag_name("span")
login.click()

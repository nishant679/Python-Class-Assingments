from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://webmail.nitt.edu/hordenew/login.php")
time.sleep(2)

email = '216218013'
passw = "Roomnumber129"
sender = 'mithil panchal'
username = driver.find_element_by_id("horde_user")
username.send_keys(email)
time.sleep(3)

username = driver.find_element_by_id("horde_pass")
username.send_keys(passw)
time.sleep(3)

login = driver.find_element_by_id("login-button")
login.click()

inbox_link = driver.find_element_by_link_text("Inbox")
inbox_link.click()
 
#SEARCHING THE INBOX
search_box = driver.find_element_by_id("horde-search-input")
search_box.send_keys(sender)
time.sleep(2)

search = driver.find_element_by_id("horde-search-icon")
search.click()
time.sleep(3)

check = driver.find_element_by_id("horiz_opts")
check.click()
time.sleep(3)

#deleting the mail
delete_btn = driver.find_element_by_id("button_delete")
delete_btn.click()
time.sleep(4)


#LOGOUT
logout = driver.find_element_by_id("horde-logout")
logout.click()
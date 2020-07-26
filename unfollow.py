from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import selenium

import time
#
#   Username
#   Password
#
username = "Username"
password = "Password"
#windows
browser = webdriver.Chrome("chromedriver.exe")


def WaitForObject(type, string):
    try:
        return selenium.webdriver.support.ui.WebDriverWait(browser, 5).until(EC.presence_of_element_located((type, string)))
    except Exception as error:
        return False

def WaitForObjects(type, string):
    try:
        return selenium.webdriver.support.ui.WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((type, string)))
    except Exception as error:
        return False




#login
browser.get("https://www.instagram.com/accounts/login")
login_objects = WaitForObjects(By.CSS_SELECTOR, "input._2hvTZ.pexuQ.zyHYP")
if login_objects != False:
    login_objects[0].send_keys(username)
    login_objects[1].send_keys(password)
    login_objects[1].send_keys(Keys.ENTER)

    time.sleep(3)

#open Profile and unfollow
browser.get(f"https://www.instagram.com/{username}/")
stats_buttons = WaitForObjects(By.CLASS_NAME,"-nal3")
if stats_buttons != False:
    stats_buttons[2].click()
    time.sleep(2)

    unfollow_buttons = WaitForObjects(By.CLASS_NAME,"sqdOP.L3NKy._8A5w5")
    if unfollow_buttons != False:
        for button_ in unfollow_buttons:
            if button_.text == "Abonniert":
                button_.click()
                button_2 = WaitForObject(By.CLASS_NAME,"aOOlW.-Cab_")
                if button_2 != False:
                    button_2.click()
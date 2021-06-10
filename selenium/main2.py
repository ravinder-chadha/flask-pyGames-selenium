import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(
    ChromeDriverManager().install())
driver.get("https://linkedin.com/login")

try:
    driver.maximize_window()
    sleep(2)
    usernme = driver.find_element_by_id("username")
    usernme.send_keys("Enter Your Email Here")      #Enter Your Email Before Running
    password = driver.find_element_by_id("password")
    password.send_keys("Enter Your Password Here")  #Enter Your Password Before Runnning
    submit_btn = driver.find_element_by_class_name("btn__primary--large")
    submit_btn.click()
    driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")
    sleep(2)
    accept = driver.find_elements_by_class_name("invitation-card__action-btn")
    for button in accept:
        a = button.get_attribute("aria-label")
        if a[0:6] == "Accept":
            button.click()
            print("clicked")
        else:
            print("not clicked")
except Exception as e:
    print("error processing link\nlink: \nerror",  e)
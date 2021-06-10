import os 
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
options=webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
 
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
 
driver.get("https://linkedin.com/login")
try:
    driver.maximize_window()
    sleep(2)
    if(driver.current_url == "https://www.linkedin.com/login"):
        username=driver.find_element_by_id("username")
        username.send_keys("ravinderchadha1233@gmail.com")     #Enter Your Email Before Running
        password=driver.find_element_by_id("password")
        password.send_keys(os.environ.get("PASSWORD"))  #Enter Your Password Before Runnning
        submit_btn=driver.find_element_by_class_name("btn__primary--large")
        submit_btn.click()

    driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")
    sleep(5)
    list_btn=driver.find_elements_by_class_name("invitation-card__action-btn")
    for btn in list_btn:
        btn_click=btn.get_attribute("aria-label")
        if btn_click[0:6]=="Accept":
            btn.click()    

except Exception as e:
    print(e)
    
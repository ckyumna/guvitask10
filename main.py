import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

#login
def login():
    driver.find_element(By.ID,value="user-name").send_keys("standard_user")
    driver.find_element(By.ID,value="password").send_keys("secret_sauce")
    driver.find_element(By.ID, value="login-button").click()
    time.sleep(10)

def fetch_details():
    title=driver.title
    print("Title of the page : ",title)

    current_url=driver.current_url
    print("Current url : ",current_url)

    page_content=driver.page_source
    with open("Webpage_task_11.txt","w",encoding="utf-8") as file:
        file.write(page_content)

    print("page content saved")

login()
fetch_details()


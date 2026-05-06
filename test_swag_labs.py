from selenium.webdriver.common.by import By


#test homepage title
def test_homepage_title(get_driver):
    driver=get_driver
    driver.get("https://www.saucedemo.com/")
    expected_title = "Swag Labs"
    assert driver.title == expected_title

def test_homepage_url(get_driver):
    driver=get_driver
    driver.get("https://www.saucedemo.com/")
    expected_url = "https://www.saucedemo.com/"
    assert driver.current_url == expected_url

def test_dashboard_url(get_driver):
    driver=get_driver
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, value="user-name").send_keys("standard_user")
    driver.find_element(By.ID, value="password").send_keys("secret_sauce")
    driver.find_element(By.ID, value="login-button").click()
    expected_url = "https://www.saucedemo.com/inventory.html"
    assert driver.current_url == expected_url





from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

def test_relative_selector(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/docs/index.html")
    form = driver.find_element(By.ID, "name-form")

    input:WebElement = form.find_element(By.CSS_SELECTOR, "[name='name']")
    button:WebElement = form.find_element(By.CSS_SELECTOR, "[value = 'Say welcome']")

    input.send_keys("John Doe")
    button.click()
    print("End")

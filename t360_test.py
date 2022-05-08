from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def test_tr360(driver: WebDriver):
    driver.get("https://training360.com")
    driver.save_screenshot("main.png")

    newsletter_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "NewsletterModalCloseButton"))
    )
    newsletter_button.click()
    
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "NewsletterModalCloseButton"))
    )

    cookie__button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".cookie__button"))
    )
    cookie__button.click()
    
    element = driver.find_element(By.CSS_SELECTOR, "[data-href='/irodai-informatika']")
    element.screenshot("informatika.png")
    
    driver.implicitly_wait(100)

    assert "Informatikai tanfolyamok" in driver.title
    

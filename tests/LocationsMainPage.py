import pytest
from urllib.parse import urljoin
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


'''

    Osztály definiálja a böngészőben megjelenítendő weblapot, funkcióin 
    keresztül kommunikálunk a webelemekkel.

    Első lépésben konstruktorát definiáljuk, mely a fixture-rel egyszerűsített 
    webdriver elérést biztosítja példányosításkor.

    Az open() funkción keresztül fogjuk elérni a weboldalt.

    Ezek definiálása után következnek az interakciókat leíró funkciók, ilyen 
    interakciók a gombokra, linkekre történő kattintások, a beviteli mezők, 
    űrlapok kitöltése, a felület üzeneteinek, feliratainak beolvasása.

'''
class LocationsMainPage:

    def __init__(self, driver) -> None:
        self.driver = driver


    def open(self):
        self.driver.get("http://localhost:8080")
        return self

    
    def click_create_location_link(self):

        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.LINK_TEXT, "Create location")))

        link = self.driver.find_element(By.LINK_TEXT, "Create location")
        link.click()
        return self

    
    def fill_form(self, name: str = "Home", coords: str = "1,1", interesting_at: str = "", 
            tags: str = ""):
        """Kitölti az űrlapot névvel, koordinátákkal, stb."""
        name_input = self.driver.find_element(By.ID, "location-name")
        name_input.send_keys(name)

        coord_input = self.driver.find_element(By.ID, "location-coords")
        coord_input.send_keys(coords)

        interesting_at_input = self.driver.find_element(By.ID, "location-interesting-at")
        interesting_at_input.send_keys(interesting_at)

        tags_input = self.driver.find_element(By.ID, "location-tags")
        tags_input.send_keys(tags)
        return self

    
    def click_on_create_location_button(self):
        create_location_button = self.driver.find_element(By.CSS_SELECTOR, "[value='Create location']")
        create_location_button.click()
        return self
        
    
    def get_text_on_message_panel(self):
        message_div = self.driver.find_element(By.ID, "message-div")
        return message_div.text

    
    def get_error_message(self):
        message_div = self.driver.find_element(By.CSS_SELECTOR, ".invalid-feedback:not([hidden = 'hidden'])")
        return message_div.text
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestBucket:
    def test_of_different_language(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        assert WebDriverWait(browser, 30).until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket"))), "кнопки добавить в корзину нет на странице"

        button = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
        button.click()
        message = browser.find_element(By.CLASS_NAME, "alertinner").text
        assert "Coders at Work" in message, True
        #time.sleep(30)


from selenium.webdriver.common.by import By
import time

class TestBucket:
    def test_of_different_language(self, browser):
        button = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
        assert button, False
        button.click()
        message = browser.find_element(By.CLASS_NAME, "alertinner").text
        assert "Coders at Work" in message, True
        time.sleep(30)

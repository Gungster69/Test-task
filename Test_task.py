import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class URLS:
    url = "https://koshelek.ru/authorization/signup"


def shadow_root_reader():  #
    driver = webdriver.Chrome()
    driver.get(URLS.url)
    shadow_host = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class = 'remoteComponent']"))
    )
    shadow_root = shadow_host.shadow_root

    return shadow_root


read = shadow_root_reader()

we = read.find_element(By.CSS_SELECTOR, "label[inertText = 'Реферальный код']")
# parent = we.findElement(By.XPATH(".."))


class Locators:  # Класс со всеми найденными локаторами для поиска окон ввода
    LOCATOR_USERNAME = read.find_element(By.CSS_SELECTOR, "input[id^= 'input-']")
    LOCATOR_EMAIL = read.find_element(By.CSS_SELECTOR, "input[id = 'username']")
    LOCATOR_PASSWORD = read.find_element(By.CSS_SELECTOR, "input[id = 'new-password']")
    LOCATOR_REFERAL = read.find_element(
        By.CSS_SELECTOR, "label[inertText = 'Реферальный код']"
    )


# Locators.LOCATOR_USERNAME.send_keys("Юрий")
# Locators.LOCATOR_EMAIL.send_keys("Androsov.2002@mail.ru")
# Locators.LOCATOR_PASSWORD.send_keys("12345678")
we.send_keys("11110000")


class auto_test:

    def check_len_name_less_then_6(self, name_to_check):
        input_name = self.Locators.LOCATOR_USERNAME.send_keys(name_to_check)
        assert len(name_to_check) > 6

    def check_len_name_more_then_32(self, name_to_check):
        input_name = self.Locators.LOCATOR_USERNAME.send_keys(name_to_check)
        assert len(name_to_check) < 32


a = input()

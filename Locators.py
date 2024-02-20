from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class URLS:
    url = "https://koshelek.ru/authorization/signup"


driver = webdriver.Chrome()
driver.get(URLS.url)
shadow_host = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[class = 'remoteComponent']"))
)
read = shadow_host.shadow_root
CUT_HTML = read.find_element(By.CSS_SELECTOR, "div[data-wi='referral']")


class Locators:
    LOCATOR_USERNAME = read.find_element(By.CSS_SELECTOR, "input[id*= 'input-']")
    LOCATOR_EMAIL = read.find_element(By.CSS_SELECTOR, "input[id = 'username']")
    LOCATOR_PASSWORD = read.find_element(By.CSS_SELECTOR, "input[id = 'new-password']")
    LOCATOR_REFERRAL = CUT_HTML.find_element(By.CSS_SELECTOR, "input[id*='input-']")
    LOCATOR_BUTTON = read.find_element(By.CSS_SELECTOR, "button[type= 'submit']")


Locators.LOCATOR_USERNAME.send_keys("Юрий")
Locators.LOCATOR_BUTTON.click()
a = input()
# Locators.LOCATOR_EMAIL.send_keys("Androsov.2002@mail.ru")
# Locators.LOCATOR_PASSWORD.send_keys("12345678")
# Locators.LOCATOR_REFERRAL.send_keys("11110000")

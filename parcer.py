import time

import requests
from bs4 import BeautifulSoup


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.execute("get", {"url": "https://koshelek.ru/authorization/signup"})
shadow_host = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[class = 'remoteComponent']"))
)
shadow_roote = shadow_host.shadow_root
CUT_HTML = shadow_roote.find_element(By.CSS_SELECTOR, "div[data-wi='referral']")
LOCATOR_REFERRAL = CUT_HTML.find_element(By.CSS_SELECTOR, "input[id*='input-']")


# shadow_child = shadow_root.find_element(By.CSS_SELECTOR, 'doc-content')
# shadow_grand_child = shadow_child.shadow_root
# element = shadow_grand_child.find_element(By.CSS_SELECTOR, 'table.featureTable')
print(LOCATOR_REFERRAL.get_attribute("outerHTML"))
driver.quit()

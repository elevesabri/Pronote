from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

username = ""
password = ""

driver.get("https://ent.iledefrance.fr/auth/login?callback=https%3A%2F%2Fent.iledefrance.fr%2F#/")
try:
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
finally:
    pass
driver.find_element("name", "email").send_keys(username)
driver.find_element("id", "password").send_keys(password)
driver.find_element(By.CLASS_NAME, "flex-magnet-bottom-right").click()
driver.get("https://0920136y.index-education.net/pronote")
while True:
    time.sleep(1)
    try:
        driver.window_handles
    except:
        driver.quit()
        break
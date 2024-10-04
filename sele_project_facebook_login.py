from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options_ = Options()
options_.add_argument("--disable-notifications")
options_.add_argument("--maximumscreen")

prefs = {"profile.default_content_setting_values.notifications": 2,  # Disable notifications
        "profile.default_content_setting_values.popups": 2}          # Disable pop-ups
options_.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options = options_)
# action = ActionChains(driver)
#driver = webdriver.Chrome(options=options_)
wait = WebDriverWait(driver, 90)
options_.add_argument("--incognito")
driver.maximize_window()
url = "https://www.facebook.com/"
driver.get(url)

with open("C:\\Users\\n50044902\\Desktop\\log_credentials\\credentials.txt",'r')as credentials:                              
        details = credentials.readlines()
        username,password = details[0].strip(),details[1].strip()

log_in_1 = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
log_in_1.send_keys(username)
log_in_2 = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pass"]')))
log_in_2.send_keys(password, Keys.ENTER)

search_text = "Valorgi"
type_in_search_text = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Search Facebook"]')))                                                                                   
type_in_search_text.send_keys(search_text, Keys.ENTER)
#click on the first result that matches search_text

time.sleep(7)

link = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Valorgi")))
link.click()

time.sleep(14)

click = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="mount_0_0_Ie"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div[2]'))).click()

print(3)

driver.quit()
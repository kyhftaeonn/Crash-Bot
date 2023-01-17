from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, threading

#define
chrome_options = Options()
driver  = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get('https://pejuangkasino02.com/game/crash')
thread = threading.Thread()

hp = "83193733233"
password = "pass"
set = "1,05"

driver.maximize_window()

#Login Session
driver.find_element(By.ID,'head_login').click();
driver.find_element(By.NAME,'phone').send_keys(hp)
time.sleep(5)
driver.find_element(By.NAME,'password').send_keys(password)
driver.find_element(By.ID,'login_login').click()
time.sleep(10)

#Excecute
driver.find_element(By.XPATH,'//*[contains(@type, "number")]').send_keys(Keys.CONTROL + "a")
driver.find_element(By.XPATH,'//*[contains(@type, "number")]').send_keys(Keys.BACKSPACE)
driver.find_element(By.XPATH,'//*[contains(@type, "number")]').send_keys(set)
time.sleep(1)
driver.find_element(By.ID,'game_bet:double').click()
time.sleep(1)

def putaran():
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="crash-guide2"]'))
        ).click()
   #driver.find_element(By.ID,'crash-guide2').click();

count = 0
while count < 99999999999999999999999999999999999999999:
     putaran()
     count+=1
     time.sleep(8)
     
for entry in driver.get_log('browser'):
    print(entry)

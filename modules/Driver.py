import time
import pyperclip as pc 
import undetected_chromedriver as uc
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from modules.CookieManager import correct_cookie
from modules.UploadManager import get_videos, get_video, randomly_video
from fake_useragent import UserAgent

useragent = UserAgent()

delay_after_upload = 7
delay_before_upload = 10


def client_setup(cookie):
    uc.install()
    opt = ChromeOptions()
    opt.add_argument('--log-level=3')
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    opt.add_argument(f"user-agent={useragent.random}")
    driver = Chrome(chrome_options = opt)
    driver.get('https://www.tiktok.com/messages/')
    driver.delete_all_cookies()
    for line in cookie:
        driver.add_cookie(correct_cookie(line))
    driver.get("https://www.tiktok.com/upload")
    video = randomly_video()
    delay = 5
    ep = EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[2]/div/iframe'))
    WebDriverWait(driver, delay).until(ep)
    driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/iframe'))
    ep = EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/div[2]/div/div/input'))
    WebDriverWait(driver, delay).until(ep)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/div[2]/div/div/input').send_keys(video[0]['vid'])
    cap = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/div/div')
    cap.send_keys(Keys.CONTROL + 'a')
    cap.send_keys(Keys.DELETE)
    text = "{} {}".format(video[0]['cap'], video[0]['tag'])
    pc.copy(text)
    cap.send_keys(Keys.CONTROL + 'v')
    time.sleep(delay_after_upload)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/div[3]/div[8]/button[2]').click()
    time.sleep(delay_before_upload)
    driver.quit()
    driver.close()
    

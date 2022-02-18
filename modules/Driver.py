import time
import undetected_chromedriver as uc
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from modules.CookieManager import correct_cookie
from modules.UploadManager import get_videos, get_video, randomly_video
from fake_useragent import UserAgent

useragent = UserAgent()


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
    time.sleep(5)
    # driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/div[2]/div/div/div/button').click()
    a = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/div[2]/div/div/div/button')
    print(a)
    element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[3]/div[2]/div/div/div/button'))
    print(element_present)
    elem = WebDriverWait(driver, delay).until(element_present)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[3]/div[2]/div/div/input').send_keys(video['vid'])
    
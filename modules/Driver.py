import time
import undetected_chromedriver as uc
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from modules.CookieManager import correct_cookie
from modules.UploadManager import get_videos, get_video, randomly_video
from fake_useragent import UserAgent

useragent = UserAgent()


class TikTokDriver:

    def __init__(self, cookie):
        uc.install()
        opt = ChromeOptions()
        opt.add_argument('--log-level=3')
        opt.add_experimental_option('excludeSwitches', ['enable-logging'])
        opt.add_argument(f"user-agent={useragent.random}")
        self.driver = Chrome(chrome_options = opt)
        self.driver.get('https://www.tiktok.com/messages/')
        self.driver.delete_all_cookies()
        for line in cookie:
            self.driver.add_cookie(correct_cookie(line))
        self.driver.get("https://www.tiktok.com/upload")
        video = randomly_video()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[3]/div[2]/div/div/input').send_keys(video['vid'])


    
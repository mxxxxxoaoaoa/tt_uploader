from modules.Driver import TikTokDriver
from modules.CookieManager import get_cookies

cookies = get_cookies()
for cookie in cookies:
    bot = TikTokDriver(cookie)
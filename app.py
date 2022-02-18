from modules.Driver import client_setup
from modules.CookieManager import get_cookies


cookies = get_cookies()
for cookie in cookies:
    bot = client_setup(cookie)
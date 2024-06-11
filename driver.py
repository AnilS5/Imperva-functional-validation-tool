"""
    Function to set default browser.
"""

import modules as md
from selenium.webdriver.chrome.service import Service


def driver_call(domain):
    options = md.wd.ChromeOptions()

    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-notifications")
    options.add_argument('--disable-infobars')

    options.accept_insecure_certs = True

    driver = md.wd.Chrome(options=options)
    driver.maximize_window()
    driver.execute_cdp_cmd("Network.setCacheDisabled", {"cacheDisabled": True})
    driver.get(domain)
    return driver

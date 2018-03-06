import random
import time
from selenium import webdriver

class SessionManager:
    def __init__(self, request_maker, login_url=[], sleep_interval=(2, 10)):
        self.driver = webdriver.Firefox()
        if isinstance(login_url, list):
            for url in login_url:
                self.driver.get(login_url)
        else:
            self.driver.get(login_url)
        self.request_maker = request_maker
        self.min_sleep_interval = sleep_interval[0]
        self.sleep_interval_range = sleep_interval[1] - sleep_interval[0]
        input("Press enter when you've logged in")

    def go(self):
        while True:
            browser_cookies = driver.get_cookies()
            cookies = {
                cookie['name']: cookie['value']
                for cookie in browser_cookies
            }
            self.request_maker(cookies)
            if self.request_maker.finished:
                break
            time.sleep(self.min_sleep_interval + random.random() * self.sleep_interval_range)

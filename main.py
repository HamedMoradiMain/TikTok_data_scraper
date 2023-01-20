try:    
    import os # os module 
    import sys # sys module
    from bs4 import BeautifulSoup
    from selenium import webdriver # webdriver
    from selenium.webdriver import Chrome # chrome 
    from selenium.webdriver.common.keys import Keys # keys
    from selenium.webdriver.common.by import By # by
    from selenium.webdriver.support.ui import WebDriverWait # webdriverwait
    from selenium.webdriver.support import expected_conditions # expected conditions
    from selenium.common.exceptions import TimeoutException # time out exception
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC # options
    from selenium.webdriver.common.proxy import Proxy, ProxyType
    import time # time module 
    import re
    import json
    import random
    import requests # request img from web  
    from pathlib import Path
    import pickle 
    import os
    print("all modules are loaded!")
except Exception as e:
    print(e)
class TikTok:
    BASE_DIR = Path(".").resolve()       
    def __init__(self):
        self.link = input("")
        self.options = Options()
        self.options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
        self.driver = webdriver.Chrome(executable_path=f"{self.BASE_DIR}/resources/chromedriver.exe",options=self.options)
        self.driver.set_window_size(500,700)
        '''for path in Path(f"{self.BASE_DIR}/resources/").iterdir():
            if "cookies" in path.name:
                print("yup")
            else:
                self.options.add_argument('--no-sandbox')
                self.options.add_argument('--start-maximized')
                self.options.add_argument('--start-fullscreen')
                self.options.add_argument('--single-process')
                self.options.add_argument('--disable-dev-shm-usage')
                self.options.add_argument("--incognito")
                self.options.add_argument('--disable-blink-features=AutomationControlled')
                self.options.add_argument('--disable-blink-features=AutomationControlled')
                self.options.add_experimental_option('useAutomationExtension', False)
                self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
                self.options.add_argument("disable-infobars")
                self.driver.get("https://www.tiktok.com/foryou?lang=en")
                change = str(input("did you change it").strip().lower())
                if change == 'yes':
                    print("saving cookies!")
                    pickle.dump(self.driver.get_cookies(),open(f"{self.BASE_DIR}/resources/cookies.pkl",'wb'))'''
    def scraper(self):
        self.driver.get("")
    def exportar(self):
        pass
    def run(self):
        pass
if __name__ == "__main__":
    bot = TikTok()
    bot.run()
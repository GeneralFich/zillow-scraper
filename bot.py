import os
from selenium import webdriver


class Bot:

    def __init__(self):
        if os.name == "nt":
            self.driver = webdriver.Edge("msedgedriver.exe")
        elif os.name == "posix":
            self.driver = webdriver.Chrome("chromedriver")
        self.driver.implicitly_wait(3)
        self.driver.set_window_size(900, 900)

    def quit(self):
        self.driver.quit()

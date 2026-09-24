from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BrowserController:

    def __init__(self):

        options = webdriver.ChromeOptions()

        options.add_argument(
            "--start-maximized"
        )

        self.driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=options
        )

    def open(self, url):

        self.driver.get(url)
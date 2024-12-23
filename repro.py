import logging
import os
import unittest

from selenium.webdriver.common import selenium_manager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver, Service


class ReproTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Make sure we see Selenium Manager logs as they are important for debugging
        logging.basicConfig()
        logging.getLogger(selenium_manager.__name__).setLevel(logging.DEBUG)
        chrome_opts = ChromeOptions()
        chrome_binary = os.getenv('CHROMIUM_BIN')
        chromedriver_binary = os.getenv('CHROMEDRIVER_BIN')
        if chrome_binary:
            # Set Chrome options suitable for the continuous build
            chrome_opts.binary_location = chrome_binary
            chrome_opts.add_argument('--headless')
            chrome_opts.add_argument('--disable-gpu')
            chrome_opts.add_argument('--verbose')
            chrome_opts.add_experimental_option('browserStartupTimeout', 1000000)
        cls.selenium = WebDriver(options=chrome_opts, service=Service(executable_path=chromedriver_binary, service_args=['--verbose']))
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_repro(self):
        self.selenium.get('https://www.google.com/')


if __name__ == '__main__':
    unittest.main()

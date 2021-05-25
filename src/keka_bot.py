import os
import time

from dotenv import load_dotenv
from selenium import webdriver

from .actions import actions

load_dotenv()


class KekaBot:
    def __init__(self, config):
        self.config = config
        options = webdriver.FirefoxOptions()

        # Set coordinates
        options.set_preference('geo.prompt.testing', True)
        options.set_preference('geo.prompt.testing.allow', True)
        location_header_string = 'data:application/json,' + str({
            "location": {
                "lat": float(os.environ['LATITUDE']),
                "lng": float(os.environ['LONGITUDE'])},
            "accuracy": 100.0}).replace("'", '"')
        options.set_preference('geo.provider.network.url', location_header_string)

        # Set Headless mode
        options.headless = config['run']['headless']

        self.driver = webdriver.Firefox(options=options, executable_path=config['setup']['geckodriver_path'])
        self.driver.maximize_window()

    def login(self, sleep_time=3):
        """Login to Keka through MS office.

        Args:
            driver (webdriver): Selenium webdriver object.

        Returns:
            bool: Return True if the action succeeds.
        """
        # Open keka login page
        actions.open_url(self.driver, self.config['urls']['keka_attendance'])

        # Click outlook login
        actions.find_button_and_click(self.driver, self.config['xpaths']['keka_login_type_botton'])

        # Click email address input, enter email address and press Enter
        actions.find_text_and_submit(self.driver, self.config['xpaths']['sign_in_email_input'], os.environ['EMAIL'])

        # Click password input, enter password and press Enter
        actions.find_text_and_submit(self.driver, self.config['xpaths']['sign_in_password_input'], os.environ['PASSWORD'])

        # Click yes button for "Stay Signedin" dialog box
        actions.find_button_and_click(self.driver, self.config['xpaths']['stay_signed_in_botton'])

        time.sleep(sleep_time)
        return True

    def clock_in(self, sleep_time=3, silent=False):
        """Clock into Keka

        Args:
            driver (webdriver): Selenium webdriver object

        Returns:
            bool: Return True if the action succeeds else False
        """
        # Open the attendence page url in browser
        actions.open_url(self.driver, self.config['urls']['keka_attendance'])

        # Click the web clock in button
        actions.find_button_and_click(self.driver, self.config['xpaths']['web_clock_in_button'])

        if not self.config['run']['silent']:
            print("You are now clocked in! Don't tell your manager how you did it!")

        time.sleep(sleep_time)
        return True

    def clock_out(self, sleep_time=3, silent=False):
        """Clock out of Keka

        Args:
            driver (webdriver): Selenium webdriver object

        Returns:
            bool: Return True if the action succeeds else False
        """
        # Open the attendence page url in browser
        actions.open_url(self.driver, self.config['urls']['keka_attendance'])

        # Click the web clock out button
        actions.find_button_and_click(self.driver, self.config['xpaths']['web_clock_out_button'])

        # Click the confirm web clock out button
        actions.find_button_and_click(self.driver, self.config['xpaths']['clock_out_confirmation_button'])

        if not self.config['run']['silent']:
            print("You are now clocked out! Good night.")

        time.sleep(sleep_time)
        return True

    def close(self):
        """ Close current session """
        self.driver.close()

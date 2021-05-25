import time

from selenium.webdriver.common.keys import Keys as webdriver_keys


def open_url(driver, url, sleep_time=3):
    """Open the url in browser.

    Args:
        driver (webdriver): Selenium webdriver object.
        url (str): URL to open in browser.
        sleep_time (int, optional): Sleep time period after running the action. Defaults to 3.

    Returns:
        bool: Returns True if the action was successful
    """
    driver.get(url)

    time.sleep(sleep_time)
    return True


def find_button_and_click(driver, xpath, sleep_time=3):
    """Find the botton from xpath and click

    Args:
        driver (webdriver): Selenium webdriver object.
        xpath (str): xpath of the html element to click.
        sleep_time (int, optional): Sleep time period after running the action. Defaults to 3.

    Returns:
        bool: Returns True if the action was successful
    """
    button = driver.find_element_by_xpath(xpath)
    button.click()

    time.sleep(sleep_time)
    return True


def find_text_and_submit(driver, xpath, input_text, sleep_time=3):
    """Find a single text field and press enter to submit

    Args:
        driver (webdriver): Selenium webdriver object.
        xpath (str): xpath of the html element to click.
        input_text (str): Text to enter into the field
        sleep_time (int, optional): Sleep time period after running the action. Defaults to 3.

    Returns:
        bool: Returns True if the action was successful
    """
    input_field = driver.find_element_by_xpath(xpath)
    input_field.send_keys(input_text)
    input_field.send_keys(webdriver_keys.ENTER)

    time.sleep(sleep_time)
    return True

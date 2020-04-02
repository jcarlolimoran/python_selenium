from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def verify_if_element_visible(driver, locator, element):
    driver.implicitly_wait(30)
    if locator == "name":
        if driver.find_element_by_name(element).is_displayed():
            return True
        else:
            return False

    elif locator == "xpath":
        if driver.find_element_by_xpath(element).is_displayed():
            return True
        else:
            return False


def keypress(driver, element, content):
    driver.find_element_by_xpath(element).send_keys(content)
    time.sleep(0.5)


def keypress_email(driver, element):
    content = 'jun_qa_' + str(random.randrange(0, 1000000)) + '@mailinator.com'
    driver.find_element_by_xpath(element).send_keys(content)
    time.sleep(0.5)


def click(driver, element):
    driver.find_element_by_xpath(element).click()
    driver.implicitly_wait(30)


def wait_for_element(driver, element, secs):
    driver.implicitly_wait(30)
    wait = WebDriverWait(driver, secs)
    return wait.until(EC.presence_of_element_located((By.XPATH, element)))

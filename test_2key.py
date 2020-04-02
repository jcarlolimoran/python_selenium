from selenium import webdriver
from sources import fileParser
from sources import Actions
from selenium import webdriver
import time





def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="E:/automation/MySelenium_New/drivers/chromedriver.exe")
    driver.set_page_load_timeout(20)
    driver.get("https://test.app.2key.network/")
    driver.maximize_window()

    assert Actions.verify_if_element_visible(driver, "xpath", fileParser.getloc("Label_Re-Inventing_The_Link"))


def test_signup():
    Actions.click(driver, fileParser.getloc("button_signup"))
    Actions.click(driver, fileParser.getloc("button_signup_with_email"))
    Actions.keypress(driver, fileParser.getloc("input_first_name"), "Auto")
    Actions.keypress(driver, fileParser.getloc("input_last_name"), "QA")
    Actions.keypress_email(driver, fileParser.getloc("input_email"))
    Actions.keypress(driver, fileParser.getloc("input_password"), "_0988Hddd")
    Actions.click(driver, fileParser.getloc("button_login_continue"))
    Actions.wait_for_element(driver, fileParser.getloc("label_thank_you"), 10)
    time.sleep(3)
    Actions.click(driver, fileParser.getloc("button_login_continue"))
    assert Actions.verify_if_element_visible(driver, "xpath", fileParser.getloc("label_welcome"))






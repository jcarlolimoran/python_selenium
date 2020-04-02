from selenium import webdriver
from sources import fileParser
from sources import Actions


def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path = "E:/automation/MySelenium_New/drivers/chromedriver.exe")
    driver.set_page_load_timeout(20)
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()
    #verify if logo is loaded
    assert Actions.verify_if_element_visible(driver, "xpath", fileParser.getloc("Image_MainPage_Logo"))


def test_load_page():
    assert Actions.verify_if_element_visible(driver, "xpath", fileParser.getloc("Input_MainPage_Search"))


def test_search_an_item():
    Actions.keypress(driver,fileParser.getloc("Input_MainPage_Search"), "Cellphone")









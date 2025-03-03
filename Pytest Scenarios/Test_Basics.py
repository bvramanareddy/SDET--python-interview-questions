import time

import pytest
from selenium import webdriver

url= "https:www.google.com/"
def test_google_landing():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    title = driver.title
    print("Grabbed Title from the Google is: ", title)
    driver.quit()

def test_facebook_landing():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    title = driver.title
    print("Grabbed Title from the Facebook is: ", title)
    driver.quit()

def test_google2_Landing():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    title = driver.title
    print("Grabbed Title from the Google2", title)
    driver.quit()

def test_swTesting_landing():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.softwaretestinghelp.com/")
    title = driver.title
    print("Grabbed Title from the SoftwarePAge is", title)
    driver.quit()





from selenium import  webdriver


def test_JC_Landing():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.jcrew.com/ca")
    titleOfJC = driver.title
    print(titleOfJC)

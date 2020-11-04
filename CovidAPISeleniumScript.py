from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Testing123:
    def testcase():
        driver = webdriver.Chrome()
        driver.get("https://covid19api.com")
        driver.maximize_window()
        print(driver.current_url)
        time.sleep(5)
        driver.get_screenshot_as_file("COVID19APIChrome1.png")
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/section[1]/div[2]/a/img").click()
        driver.maximize_window()
        time.sleep(5)
        driver.get_screenshot_as_file("DigitalOceanChromeReferral1.png")
        driver.close()

Testing123.testcase()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Testing123:
    def testcase():
        driver = webdriver.Chrome()
        driver.get("https://covid19api.com")
        print(driver.current_url)
        driver.get_screenshot_as_file("COVID19APIChrome.png")
        time.sleep(15)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/section[1]/div[2]/a/img").click()
        time.sleep(15)
        driver.get_screenshot_as_file("DigitalOceanChromeReferral.png")
        driver.close()

Testing123.testcase()

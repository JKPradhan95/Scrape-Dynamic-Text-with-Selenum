from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/")
    return driver

def main():
    driver = get_driver()
    try:
        element = driver.find_element(by="xpath", value='/html/body/div[1]/div/h1[2]')
        return element.text
    except NoSuchElementException:
        return "Element not found"
    finally:
        driver.quit()

print(main())


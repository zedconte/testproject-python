from src.testproject.sdk.drivers import webdriver
from src.testproject.decorator import report
import os

@report(project="Python Test Project", job="Python Job")
def simple_test():
    driver = webdriver.Chrome(token=os.getenv('TP_DEV_TOKEN'))
    #driver = webdriver.Chrome()
    driver.report().disable_auto_test_reports(disabled=True)

    driver.get("https://example.testproject.io/web/")
    driver.find_element_by_css_selector("#name").send_keys("John Smith")
    driver.find_element_by_css_selector("#password").send_keys("12345")
    driver.find_element_by_css_selector("#login").click()
    passed = driver.find_element_by_css_selector("#logout").is_displayed()
    print("Test passed") if passed else print("Test failed")

    driver.report().test(name="My self reported test", message="A message", passed=True)
    driver.quit()
if __name__ == "__main__":
    simple_test()
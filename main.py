from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as aChain
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# A set of Selenium examples which meets the basic needs of trainees doing the flash python/devops project!


def app():
    nav_actions()


def setup_basic(url):
    new_driver = webdriver.Firefox()
    new_driver.get(url)
    assert "Google" in new_driver.title
    new_driver.close()


def setup_options():
    options = webdriver.FirefoxOptions()
    options.set_preference("profile.default_content_setting_values.cookies", 2);
    options.set_preference("network.cookie.cookieBehavior", 2);
    options.set_preference("profile.block_third_party_cookies", 2);
    options.add_argument('--headless')
    option_driver = webdriver.Firefox(options=options)
    return option_driver


def navigate(url):
    try:
        option_driver = setup_options()
        option_driver.get(url)
        option_driver.close()
        print("completed")
    finally:
        option_driver.close()


driver = webdriver.Firefox()


def nav_actions():
    # Community Task as example:
    url = "https://www.youidraw.com/apps/painter/"
    # Go to the YouIDraw Web site
    driver.get(url)
    # identify necessary selectors
    brush = driver.find_element_by_id("brush")
    canvas = driver.find_element_by_id("catch")
    # set up actions
    ac = aChain(driver)
    # Automate this task using actions
    brush.click()
    try:
        ac.move_to_element(canvas).click_and_hold().move_by_offset(0, -200).move_by_offset(100,
                                                                                           0).click().move_to_element(
            canvas).click_and_hold().move_by_offset(100, 0).click().move_to_element(
            canvas).click_and_hold().move_by_offset(
            0, -100).move_by_offset(100, 0).click().move_to_element(canvas).perform()

        ac.move_by_offset(200, 0).click_and_hold().move_by_offset(0, -200).move_by_offset(100, 0).move_by_offset(0, 100)\
            .move_by_offset(-100, 0).move_by_offset(100, 100).perform()

    finally:
        driver.close()


def nav_implicit_wait():
    driver.implicitly_wait(10)  # seconds
    ele = driver.find_element_by_id("something")


def nav_explicit_wait():
    wait = WebDriverWait(driver, 5)
    ele = driver.find_element_by_class_name("q")

    try:
        search = wait.until(ec.element_to_be_clickable(ele))
        # assert(search, )
    finally:
        driver.close()


if __name__ == '__main__':
    app()

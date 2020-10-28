# SCRAPER FILE
# This one is honestly going to get super long, so I suggest we go through it together!

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

def run_Scraper(username, password):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    url = "https://elearn.sunway.edu.my"

    driver.get(url)
    
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_id("agree_button")).click()
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath("//button[text()='Sunway ID']")).click()
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_id("userNameInput")).send_keys(username)
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_id("passwordInput")).send_keys(password)
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_id("submitButton")).click()
    
    
def enter_courses():
    file = open("subjects.txt", "r")
    subjects = file.readline()
    subject_list = subjects.split(",")
    
    for subject in subject_list:
        actions = ActionChains(driver)
        courses_button = WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath("//span[text()='Courses']"))
        actions.key_down(Keys.CONTROL).click(courses_button).key_up(Keys.CONTROL).perform()
        driver.switch_to.window(driver.window_handles[-1])

    for index in range(len(subject_list)):
        driver.switch_to.window(driver.window_handles[index+1])
        WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath("//span[contains(text(),'" + subject_list[index] + "')]")).click()

def get_announcements():
    today_section = WebDriverWait(driver, 30).until(lambda x: x.find_element_by_class_name("js-todayStreamEntries"))
    announcement_list = today_section.find_element_by_tag_name("li")

    file = open("announcements.txt", "w")

    file.write("Today's announcement!" + "\n\n")

    for announcement in announcement_list:
        title = announcement.find_element_by_tag_name("a").text
        content = announcement.find_element_by_class_name("name").text
        file.write(title + "\n")
        file.write(content + "\n\n")

    file.close()
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains

from genName import generate_random_name, generate_random_email

import time

URL = "https://elka-tech.fut.ru/?utm_campaign=friends&utm_content=almtara550@gmail.com"

# Замените путь к драйверу на ваш
driver_path = "/Users/aatara57/PycharmProjects/regReferGazpromMeetup/chromedriver"

# Init web driver
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")  # Опционально: чтобы браузер не отображался на экране
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options)

# Open web-site
driver.get(URL)

try:
    # Find HTML button with text "Зарегистрироваться"
    register_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Зарегистрироваться!"))
    )
    # Pick button
    register_button.click()

    # First and second name
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    )
    name_input.send_keys(generate_random_name())

    # EMAIL
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )

    email_input.send_keys(generate_random_email())

    # PHONE
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "tildaspec-phone-part[]"))
    )

    # Заполняем поле ввода маской телефона
    phone_input.send_keys("9".join([str(random.randint(0,9 )) for _ in range(8)]))  # Замените на реальный телефон

    # VUZ
    vuz_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "vuz"))
    )
    russian_universities = [
        "МГУ",
        "ВШЭ",
        "МИЭТ",
        "МИФИ",
        "МФТИ",
        "МГТУ им. Баумана",
        "Финансовый университет",
        "МАДИ",
        "МПГУ",
        "МЭИ",
        "МГСУ"
    ]

    vuz_input.send_keys(russian_universities[random.randint(0, 10)])


    course_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sb-1699977280690"))
    )

    select = Select(course_dropdown)

    select.select_by_value("2 курс бакалавриата/специалитета")

    sphere_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sb-1699977310979"))
    )

    select = Select(sphere_dropdown)

    select.select_by_value("Backend разработка")

    agreement_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "agreement"))
    )

    actions = ActionChains(driver)
    actions.move_to_element(agreement_checkbox).click().perform()

    register_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Зарегистрироваться']"))
    )

    # actions = ActionChains(driver)
    # actions.move_to_element(register_button).click().perform()

    time.sleep(30)



finally:
    # Закрытие браузера
    driver.quit()

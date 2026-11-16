import pytest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WW

from helpers import generate_email
from locators import RegistrationLocators, MainPageLocators, LoginLocators


@pytest.fixture
def driver():
    browser = webdriver.Chrome()

    try:
        browser.set_window_size(1280, 900)
        browser.get("https://qa-desk.education-services.ru")
        yield browser
    finally:
        browser.quit()


@pytest.fixture
def existing_user(driver):
    wait = WW(driver, 10)

    email = generate_email()
    password = "QwertY321"

    wait.until(
        EC.element_to_be_clickable(
            RegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            RegistrationLocators.NO_ACCOUNT_BUTTON
        )
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            RegistrationLocators.EMAIL_INPUT_FIELD
        )
    ).send_keys(email)

    wait.until(
        EC.visibility_of_element_located(
            RegistrationLocators.PASSWORD_INPUT_FIELD
        )
    ).send_keys(password)

    wait.until(
        EC.visibility_of_element_located(
            RegistrationLocators.CONFIRM_PASSWORD_INPUT_FIELD
        )
    ).send_keys(password)

    wait.until(
        EC.element_to_be_clickable(
            RegistrationLocators.CREATE_ACCOUNT_BUTTON
        )
    ).click()

    wait.until(
        EC.invisibility_of_element_located(
            RegistrationLocators.EMAIL_INPUT_FIELD
        )
    )

    wait.until(
        EC.element_to_be_clickable(
            MainPageLocators.LOGOUT_BUTTON
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            RegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON
        )
    )

    return {
        "email": email,
        "password": password,
    }


@pytest.fixture
def authorized_driver(driver, existing_user):
    wait = WW(driver, 10)

    wait.until(
        EC.element_to_be_clickable(
            RegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON
        )
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            LoginLocators.EMAIL_INPUT_FIELD
        )
    ).send_keys(existing_user["email"])

    wait.until(
        EC.visibility_of_element_located(
            LoginLocators.PASSWORD_INPUT_FIELD
        )
    ).send_keys(existing_user["password"])

    wait.until(
        EC.element_to_be_clickable(
            LoginLocators.LOGIN_BUTTON
        )
    ).click()

    wait.until(
        EC.invisibility_of_element_located(
            LoginLocators.EMAIL_INPUT_FIELD
        )
    )

    wait.until(
        EC.visibility_of_element_located(
            MainPageLocators.USER_AVATAR
        )
    )

    wait.until(
        EC.visibility_of_element_located(
            MainPageLocators.USER_NAME
        )
    )

    return driver

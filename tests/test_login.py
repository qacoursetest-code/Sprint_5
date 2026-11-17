from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WW

from constants import SITE_URL
from locators import (
    RegistrationLocators,
    LoginLocators,
    MainPageLocators,
)


class TestLogin:
    def test_login_existing_user(self, driver, existing_user):
        wait = WW(driver, 10)

        email = existing_user["email"]
        password = existing_user["password"]

        wait.until(
            EC.element_to_be_clickable(
                RegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON
            )
        ).click()

        wait.until(
            EC.visibility_of_element_located(
                LoginLocators.EMAIL_INPUT_FIELD
            )
        ).send_keys(email)

        wait.until(
            EC.visibility_of_element_located(
                LoginLocators.PASSWORD_INPUT_FIELD
            )
        ).send_keys(password)

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

        search_input = wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.SEARCH_INPUT
            )
        )

        user_avatar = wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.USER_AVATAR
            )
        )

        user_name = wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.USER_NAME
            )
        )

        actual = (
            driver.current_url,
            search_input.is_displayed(),
            user_avatar.is_displayed(),
            user_name.text,
        )

        expected = (
            SITE_URL,
            True,
            True,
            "User",
        )

        assert actual == expected
        
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WW

from locators import RegistrationLocators, MainPageLocators


class TestLogout:
    def test_logout_hides_user_and_shows_login(self, authorized_driver):
        driver = authorized_driver
        wait = WW(driver, 10)

        wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.LOGOUT_BUTTON
            )
        ).click()

        avatar_hidden = wait.until(
            EC.invisibility_of_element_located(
                MainPageLocators.USER_AVATAR
            )
        )

        name_hidden = wait.until(
            EC.invisibility_of_element_located(
                MainPageLocators.USER_NAME
            )
        )

        login_button = wait.until(
            EC.visibility_of_element_located(
                RegistrationLocators.LOGIN_AND_REGISTRATION_BUTTON
            )
        )

        actual = (
            bool(avatar_hidden),
            bool(name_hidden),
            login_button.is_displayed(),
        )

        expected = (True, True, True)

        assert actual == expected
        
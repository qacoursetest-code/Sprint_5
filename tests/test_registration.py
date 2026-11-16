from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WW

from locators import RegistrationLocators, MainPageLocators
from helpers import generate_email


class TestRegistration:

    def test_new_user_registration(self, driver):
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
                RegistrationLocators.CREATE_ACCOUNT_BUTTON
            )
        )

        email_input = wait.until(
            EC.visibility_of_element_located(
                RegistrationLocators.EMAIL_INPUT_FIELD
            )
        )
        email_input.send_keys(email)

        password_input = wait.until(
            EC.visibility_of_element_located(
                RegistrationLocators.PASSWORD_INPUT_FIELD
            )
        )
        password_input.send_keys(password)

        password_input_confirm = wait.until(
            EC.visibility_of_element_located(
                RegistrationLocators.CONFIRM_PASSWORD_INPUT_FIELD
            )
        )
        password_input_confirm.send_keys(password)

        wait.until(
            EC.element_to_be_clickable(
                RegistrationLocators.CREATE_ACCOUNT_BUTTON
            )
        ).click()

        # Ждём закрытия формы регистрации.
        wait.until(
            EC.invisibility_of_element_located(
                RegistrationLocators.EMAIL_INPUT_FIELD
            )
        )

        # Ждём элементы главной страницы и авторизованного пользователя.
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

        login_check = (
            driver.current_url,
            search_input.is_displayed(),
            user_avatar.is_displayed(),
            user_name.text,
        )
        expected = (
            "https://qa-desk.education-services.ru/",
            True,
            True,
            "User"
        ) 

        assert login_check == expected 
        # В требованиях написано User, фактически же User. Также после регистрации не происходит переход на главную страницу


    def test_registration_with_invalid_email(self, driver):
        wait = WW(driver, 10)

        invalid_email = generate_email().replace("@", "")

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

        email_input = wait.until(
            EC.visibility_of_element_located(
                RegistrationLocators.EMAIL_INPUT_FIELD
            )
        )
        email_input.send_keys(invalid_email)

        wait.until(
            EC.element_to_be_clickable(
                RegistrationLocators.CREATE_ACCOUNT_BUTTON
            )
        ).click()

        error_message = wait.until(
            EC.visibility_of_element_located(
                RegistrationLocators.EMAIL_ERROR_MESSAGE
            )
        )

        email_border_color = driver.find_element(
            *RegistrationLocators.EMAIL_BORDER
        ).value_of_css_property("border-bottom-color")

        password_border_color = driver.find_element(
            *RegistrationLocators.PASSWORD_BORDER
        ).value_of_css_property("border-bottom-color")

        confirm_password_border_color = driver.find_element(
            *RegistrationLocators.CONFIRM_PASSWORD_BORDER
        ).value_of_css_property("border-bottom-color")

        actual = (
            error_message.text,
            email_border_color,
            password_border_color,
            confirm_password_border_color,
        )

        expected = (
            "Ошибка",
            "rgba(255, 105, 114, 1)",
            "rgba(255, 105, 114, 1)",
            "rgba(255, 105, 114, 1)",
        )

        assert actual == expected


    def test_registration_with_existing_email(self, driver, existing_user):
        wait = WW(driver, 10)

        email = existing_user["email"]
        password = existing_user["password"]

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

        error_message = wait.until(
            EC.visibility_of_element_located(
                RegistrationLocators.EMAIL_ERROR_MESSAGE
            )
        )

        email_border_color = driver.find_element(
            *RegistrationLocators.EMAIL_BORDER
        ).value_of_css_property("border-bottom-color")

        password_border_color = driver.find_element(
            *RegistrationLocators.PASSWORD_BORDER
        ).value_of_css_property("border-bottom-color")

        confirm_password_border_color = driver.find_element(
            *RegistrationLocators.CONFIRM_PASSWORD_BORDER
        ).value_of_css_property("border-bottom-color")

        actual = (
            error_message.text,
            email_border_color,
            password_border_color,
            confirm_password_border_color,
        )

        expected = (
            "Ошибка",
            "rgba(255, 105, 114, 1)",
            "rgba(255, 105, 114, 1)",
            "rgba(255, 105, 114, 1)",
        )

        assert actual == expected

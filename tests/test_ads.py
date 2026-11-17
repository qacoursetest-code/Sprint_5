from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WW

from locators import MainPageLocators, AdLocators, ProfileLocators


class TestAds:

    def test_guest_sees_authorization_dialog(self, driver):
        wait = WW(driver, 10)

        wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.CREATE_AD_BUTTON
            )
        ).click()

        authorization_title = wait.until(
            EC.visibility_of_element_located(
                AdLocators.AUTHORIZATION_TITLE
            )
        )

        actual = authorization_title.text
        expected = "Чтобы разместить объявление, авторизуйтесь"

        assert actual == expected


    def test_authorized_user_publishes_ad(self, authorized_driver):
        driver = authorized_driver
        wait = WW(driver, 10)

        title = "Очень важная книга!"
        description = "Описывает самое важное"
        price = "750"

        wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.CREATE_AD_BUTTON
            )
        ).click()

        wait.until(
            EC.visibility_of_element_located(
                AdLocators.TITLE_INPUT
            )
        ).send_keys(title)

        wait.until(
            EC.visibility_of_element_located(
                AdLocators.DESCRIPTION_INPUT
            )
        ).send_keys(description)

        wait.until(
            EC.visibility_of_element_located(
                AdLocators.PRICE_INPUT
            )
        ).send_keys(price)

        wait.until(
            EC.element_to_be_clickable(
                AdLocators.CATEGORY_BUTTON
            )
        ).click()

        wait.until(
            EC.element_to_be_clickable(
                AdLocators.BOOKS_OPTION
            )
        ).click()

        wait.until(
            EC.element_to_be_clickable(
                AdLocators.CITY_BUTTON
            )
        ).click()

        wait.until(
            EC.element_to_be_clickable(
                AdLocators.KAZAN_OPTION
            )
        ).click()

        wait.until(
            EC.element_to_be_clickable(
                AdLocators.USED_CONDITION_BUTTON
            )
        ).click()

        wait.until(
            EC.visibility_of_element_located(
                AdLocators.USED_CONDITION_ACTIVE
            )
        )

        wait.until(
            EC.element_to_be_clickable(
                AdLocators.PUBLISH_BUTTON
            )
        ).click()

        wait.until(
            EC.invisibility_of_element_located(
                AdLocators.TITLE_INPUT
            )
        )

        wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.PROFILE_BUTTON
            )
        ).click()

        wait.until(
            EC.visibility_of_element_located(
                ProfileLocators.MY_ADS_TITLE
            )
        )

        ad_title = wait.until(
            EC.visibility_of_element_located(
                ProfileLocators.MY_AD_TITLES
            )
        )

        actual = ad_title.text
        expected = title

        assert actual == expected
        
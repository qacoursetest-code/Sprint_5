from selenium.webdriver.common.by import By


class RegistrationLocators:

    LOGIN_AND_REGISTRATION_BUTTON = (
        By.XPATH,
        "//button[text()='Вход и регистрация']"
    )

    NO_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[text()='Нет аккаунта']"
    )

    EMAIL_INPUT_FIELD = (By.NAME, "email")

    PASSWORD_INPUT_FIELD = (By.NAME, "password")

    CONFIRM_PASSWORD_INPUT_FIELD = (By.NAME, "submitPassword")

    CREATE_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[text()='Создать аккаунт']"
    )

    EMAIL_ERROR_MESSAGE = (
        By.XPATH,
        "//span[@class='input_span__yWPqB' and normalize-space(.)='Ошибка']"
    )

    EMAIL_BORDER = (
        By.XPATH,
        "//input[@name='email']/parent::div"
    )

    PASSWORD_BORDER = (
        By.XPATH,
        "//input[@name='password']/parent::div"
    )

    CONFIRM_PASSWORD_BORDER = (
        By.XPATH,
        "//input[@name='submitPassword']/parent::div"
    )


class MainPageLocators:

    USER_NAME = (
        By.CSS_SELECTOR,
        "h3.profileText.name"
    )

    USER_AVATAR = (
        By.CSS_SELECTOR,
        "button.circleSmall svg"
    )

    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='Я хочу купить...']"
    )

    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[text()='Выйти']"
    )

    CREATE_AD_BUTTON = (
        By.XPATH,
        "//button[text()='Разместить объявление']"
    )

    PROFILE_BUTTON = (
        By.CSS_SELECTOR,
        "button.circleSmall",
    )


class LoginLocators:

    EMAIL_INPUT_FIELD = (By.NAME, "email")

    PASSWORD_INPUT_FIELD = (By.NAME, "password")

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Войти']"
    )


class AdLocators:

    AUTHORIZATION_TITLE = (
        By.XPATH,
        "//h1[normalize-space(.)='Чтобы разместить объявление, авторизуйтесь']",
    )

    TITLE_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='Название']",
    )

    DESCRIPTION_INPUT = (
        By.CSS_SELECTOR,
        "textarea[placeholder='Описание товара']",
    )

    PRICE_INPUT = (By.NAME, "price")

    CATEGORY_BUTTON = (
        By.XPATH,
        "//input[@name='category']/following-sibling::button",
    )

    BOOKS_OPTION = (
        By.XPATH,
        "//button[normalize-space(.)='Книги']",
    )

    CITY_BUTTON = (
        By.XPATH,
        "//input[@name='city']/following-sibling::button",
    )

    KAZAN_OPTION = (
        By.XPATH,
        "//button[normalize-space(.)='Казань']",
    )

    USED_CONDITION_BUTTON = (
        By.XPATH,
        "//input[@name='condition' and @value='Б/У']/following-sibling::div",
    )

    USED_CONDITION_ACTIVE = (
        By.XPATH,
        "//input[@name='condition' and @value='Б/У']"
        "/following-sibling::div"
        "[contains(@class, 'radioUnput_inputActive')]",
    )

    PUBLISH_BUTTON = (
        By.XPATH,
        "//button[text()='Опубликовать']",
    )


class ProfileLocators:
    MY_ADS_TITLE = (
        By.XPATH,
        "//h1[text()='Мои объявления']",
    )

    MY_AD_TITLES = (
        By.XPATH,
        "//h1[text()='Мои объявления']/parent::div//div[@class='about']/h2",
    )

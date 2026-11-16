# Sprint_5

Тесты сервиса «Доска» https://qa-desk.education-services.ru/.

Инструменты: Python, Selenium, pytest.

Реализованные проверки:
- Регистрация пользователя.
- Вход и выход пользователя.
- Создание объявления.

5 passed, 2 failed

test_new_user_registration и test_login_existing_user падают ожидаемо из-за разницы в User (по требованиям тест-кейса) и User. фактического на сайте + разницы в ссылке (в момент итоговой проверки URL остаётся /regiatration или /login, хотя отображаются поиск и аватар) 

  Full diff: (-: missing in left side, +: extra in left side)
    (
  -     'https://qa-desk.education-services.ru/',
  +     'https://qa-desk.education-services.ru/regiatration',
  ?                                            ++++++++++++
        True,
        True,
  -     'User',
  +     'User.',
  ?          +
    )

Для запуска из корня проекта:

python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest tests -vv --tb=short
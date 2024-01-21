import pytest

from framework.cred import Credentials


def test_user_login_positive(user_login_fixture):
    """
    0. Логінимся з коректними кредами
    1. Перевіряємо що зайшли на головну сторінку з menuDrawer
    """
    user_login_fixture.press_login_base_button()
    user_login_fixture.login(Credentials.email, Credentials.password)
    menu = user_login_fixture.find_menu_drawer()

    assert menu


@pytest.mark.parametrize("email, password",
                         [(Credentials.email, "000000"),
                          ("adnim@adnim.com", Credentials.password)]
                         )
def test_user_login_negative(user_login_fixture, email, password):
    """
    0. Логінимся з невірними кредами
    1. Перевіряємо з'являється LinearLayout
    """
    user_login_fixture.press_login_base_button()
    user_login_fixture.login(email, password)
    login_wrong = user_login_fixture.find_login_wrong()

    assert login_wrong

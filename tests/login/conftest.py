import pytest

from framework.login_page import LoginPage

# Додав бо небачил drive в області імен. Чи переприсвоювало, так і не зрозумів чому.
pytest_plugins = ["tests.conftest"]

@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield LoginPage(driver)


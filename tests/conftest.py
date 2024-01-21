import subprocess
from time import sleep

import pytest
from appium import webdriver

from utils.android_utils import android_get_desired_capabilities

from framework.login_page import LoginPage

@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    sleep(5)


@pytest.fixture(scope='function')
def driver(run_appium_server):
    """
    змінив скоуп на function

    driver.quit() Вбиває ссесія. працює як дізлогін.
    так робити не треба, бо тести будуть довго проходити.
    Але точно будемо знати що тести один на одного не будеть впливати
    """
    driver = webdriver.Remote("http://localhost:4723", options=android_get_desired_capabilities)
    yield driver
    driver.quit()


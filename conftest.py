from selene import browser, be, have
import pytest




@pytest.fixture()
def browser_size():

    browser.config.window_width = 430
    browser.config.window_height = 932


@pytest.fixture(scope='function')
def open_yandex_browser(browser_size):

    browser.open("https://ya.ru")

    yield browser
    browser.quit()
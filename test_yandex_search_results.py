from selene import browser, be, have
import pytest


def test_search_no_results(open_yandex_browser):
    browser.element('[name="text"]').should(be.blank).type('qa.guru').press_enter()
    (browser.element('//*[text()="Курсы тестировщиков — обучение... | "]')
     .should(have.text('Курсы тестировщиков — обучение')))

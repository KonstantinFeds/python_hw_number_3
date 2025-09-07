from selene import browser, be, have
import pytest


def test_search_no_results(open_yandex_browser):
    browser.element('[name="text"]').should(be.blank).type('аиоарраавпвпрпаооокап').press_enter()
    browser.element('[class = EmptySearchResults-Title]').should(have.text('Ничего не нашли'))

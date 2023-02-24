import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en, ru, etc")

    
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    print(f"\nlanguage is: {user_language}")

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = ChOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=chrome_options)
        browser.implicitly_wait(10)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")

        options = FFOptions()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

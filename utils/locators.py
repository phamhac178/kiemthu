from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocators(object):
    LOGO = (By.XPATH, '/html/head/title')
    ACCOUNT = (By.ID, 'nav-link-accountList')
    SIGNUP = (By.CSS_SELECTOR, '#nav-signin-tooltip > div > a')
    LOGIN = (By.CSS_SELECTOR, '#nav-signin-tooltip > a')
    SEARCH = (By.ID, 'twotabsearchtextbox')
    SEARCH_LIST = (By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')
    HELP_LINK = (By.XPATH, '//a[text()=\'Help\']')
    User = (By.XPATH, '//*[@id="User"]')
    Pass = (By.XPATH, '//*[@id="Password"]')
    Login = (By.XPATH, '//*[@id="Lnew1"]')
    SYS = (By.XPATH, '//*[@id="form1"]/div[3]/div/div[2]/ul/li[5]/a')
    Logout = (By.XPATH, '//*[@id="form1"]/div[3]/div/div[2]/ul/li[5]/ul/li[1]/a')


class LoginPageLocators(object):
    EMAIL = (By.ID, 'ap_email')
    PASSWORD = (By.ID, 'ap_password')
    SUBMIT = (By.ID, 'signInSubmit-input')
    ERROR_MESSAGE = (By.ID, 'message_error')

class HelpPageLocators(object):
    HELPSEARCH = (By.XPATH, '//input[@id=\'helpsearch\']')
    PAYMENTMETHODTEXT = (By.XPATH, '// h2[contains(text(), \'Payment Methods\')]')






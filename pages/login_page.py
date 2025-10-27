# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, driver):
        self.driver = driver
        self.user = (By.ID, "username")
        self.password = (By.ID, "password")
        self.btn = (By.ID, "submit")
        self.error = (By.ID, "error")

    def open(self):
        self.driver.get(self.URL)

    def fill_username(self, u):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.user)).clear()
        self.driver.find_element(*self.user).send_keys(u)

    def fill_password(self, p):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password)).clear()
        self.driver.find_element(*self.password).send_keys(p)

    def click_login(self):
        # Espera a que sea clickable; si no, JS click como fallback
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.element_to_be_clickable(self.btn)).click()
        except Exception:
            el = wait.until(EC.presence_of_element_located(self.btn))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
            self.driver.execute_script("arguments[0].click();", el)

    def login(self, u, p):
        self.fill_username(u)
        self.fill_password(p)
        self.click_login()

    # Aserciones de estado
    def is_login_button_enabled(self):
        return self.driver.find_element(*self.btn).is_enabled()

    def get_error_text(self):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.error)).text
        except Exception:
            return ""

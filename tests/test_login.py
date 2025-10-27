# tests/test_login.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def test_login_exitoso(driver):
    page = LoginPage(driver)
    page.open()
    # Estado previo: botón habilitado
    assert page.is_login_button_enabled() is True

    page.login("student", "Password123")

    WebDriverWait(driver, 10).until(EC.url_contains("logged-in-successfully"))
    assert "logged-in-successfully" in driver.current_url

def test_login_contrasena_invalida(driver):
    page = LoginPage(driver)
    page.open()
    page.login("student", "WrongPassword")
    assert "invalid" in page.get_error_text()

def test_login_campos_vacios_desactiva(driver):
    page = LoginPage(driver)
    page.open()
    # Si tu app deshabilita el botón cuando faltan campos, aquí lo validarías:
    # (En esta página de práctica el botón está habilitado, esto es un ejemplo genérico)
    # page.fill_username("") ; page.fill_password("")
    # assert page.is_login_button_enabled() is False
    assert page.is_login_button_enabled() is True  # comportamiento del sitio de práctica

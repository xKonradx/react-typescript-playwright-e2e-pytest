import pytest
from pages.RegisterPage import RegisterPage
from pages.LoginPage import LoginPage

@pytest.mark.parametrize("username,password", [
    ("testuser1", "testpass123"),
    ("testuser2", "testpass456")
])
def test_register_success(page, base_url, username, password):
    """Test pomyślnej rejestracji nowych użytkowników"""
    register = RegisterPage(page, base_url)
    register.goto()
    
    # Wypełnij formularz rejestracji
    register.register(username, password)
    
    # Sprawdź przekierowanie do logowania
    page.wait_for_url("**/login", timeout=5000)
    
    # Sprawdź czy można się zalogować nowym kontem
    login_page = LoginPage(page)
    login_page.login(username, password)
    
    # Sprawdź czy zalogowano poprawnie
    page.wait_for_url("**/dashboard", timeout=5000)
    assert "dashboard" in page.url

def test_register_existing_login(page, base_url):
    """Test rejestracji z istniejącym loginem"""
    register = RegisterPage(page, base_url)
    register.goto()
    register.register("admin", "password123")
    # Sprawdź czy pojawił się komunikat błędu (zgodny z UI)
    error_message = page.get_by_text("Taki login już istnieje.")
    if not error_message.is_visible():
        error_message = page.get_by_text("Użytkownik o podanym loginie już istnieje")
    if not error_message.is_visible():
        print("Dostępne teksty na stronie:", page.content())
    assert error_message.is_visible()

def test_register_weak_password(page, base_url):
    """Test rejestracji ze słabym hasłem"""
    register = RegisterPage(page, base_url)
    register.goto()
    register.register("newuser", "123")
    # Sprawdź czy pojawił się komunikat błędu (zgodny z UI)
    error_message = page.get_by_text("Hasło musi mieć min. 6 znaków.")
    if not error_message.is_visible():
        error_message = page.get_by_text("Hasło musi mieć co najmniej 6 znaków")
    if not error_message.is_visible():
        print("Dostępne teksty na stronie:", page.content())
    assert error_message.is_visible()

def test_register_password_mismatch(page, base_url):
    """Test rejestracji z niezgodnymi hasłami"""
    register = RegisterPage(page, base_url)
    register.goto()
    
    # Próba rejestracji z różnymi hasłami
    register.register("newuser", "password123", "different123")
    
    # Sprawdź czy pojawił się komunikat błędu
    error_message = page.get_by_text("Hasła nie są zgodne")
    if not error_message.is_visible():
        print("Dostępne teksty na stronie:", page.content())
    assert error_message.is_visible() 
import pytest
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from pages.ProfilePage import ProfilePage

@pytest.mark.parametrize("username,old_password,new_password", [
    ("user", "user123", "nowehaslo1"),
    ("admin", "admin123", "nowehaslo2")
])
def test_change_password_success(page, base_url, username, old_password, new_password):
    """Test pomyślnej zmiany hasła"""
    login_page = LoginPage(page)
    login_page.goto(base_url)
    login_page.login(username, old_password)
    
    # Przejdź do edycji profilu
    profile = ProfilePage(page, base_url)
    profile.goto()
    
    # Zmień hasło
    profile.change_password(old_password, new_password, new_password)
    
    # Sprawdź komunikat sukcesu
    success_message = page.get_by_text("Hasło zostało zmienione")
    assert success_message.is_visible()

@pytest.mark.parametrize("old_password,new_password,confirm_password,expected_error", [
    ("zlehaslo", "nowehaslo", "nowehaslo", "Stare hasło jest nieprawidłowe"),
    ("user123", "123", "123", "min. 6 znaków"),
    ("user123", "nowehaslo", "innehaslo", "nie są zgodne")
])
def test_change_password_validation(page, base_url, old_password, new_password, confirm_password, expected_error):
    """Test walidacji zmiany hasła"""
    login_page = LoginPage(page)
    login_page.goto(base_url)
    login_page.login("user", "user123")
    
    # Przejdź do edycji profilu
    profile = ProfilePage(page, base_url)
    profile.goto()
    
    # Próba zmiany hasła z błędnymi danymi
    profile.change_password(old_password, new_password, confirm_password)
    
    # Sprawdź komunikat błędu
    error_message = page.get_by_text(expected_error)
    assert error_message.is_visible() 
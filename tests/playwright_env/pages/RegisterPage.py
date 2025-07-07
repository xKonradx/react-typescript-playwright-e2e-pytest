class RegisterPage:
    """
    Page Object Model dla strony rejestracji użytkownika.
    Pozwala na interakcję z polami formularza rejestracji i obsługę komunikatów błędów.
    """
    def __init__(self, page, base_url="http://localhost:5173"):
        """
        Inicjalizuje RegisterPage z obiektem page Playwright.
        Ustawia lokalizatory dla pól i przycisku rejestracji.
        """
        self.page = page
        self.base_url = base_url
        self.url = f"{base_url}/register"
        self.login_input = page.get_by_label('Login')
        self.password_input = page.get_by_label('Hasło').nth(0)
        self.repeat_input = page.get_by_label('Powtórz hasło')
        self.submit_btn = page.get_by_role('button', name='Zarejestruj się')
        self.success_msg = page.get_by_test_id('register-success')
        self.error_msg = page.get_by_test_id('register-error')

    def is_current_page(self):
        if "/register" not in self.page.url:
            return False
        try:
            self.login_input.wait_for(timeout=1000)
        except Exception:
            return False
        return self.login_input.is_visible()

    def goto(self):
        """
        Przechodzi do strony rejestracji.
        """
        self.page.goto(self.url)
        try:
            self.login_input.wait_for(timeout=2000)
        except Exception:
            if "/login" in self.page.url:
                return False
            raise
        return True

    def register(self, login, password, repeat=None):
        """
        Wypełnia formularz rejestracji i klika przycisk 'Zarejestruj się'.
        """
        if not self.is_current_page():
            raise Exception("Nie jesteś na stronie rejestracji!")
        self.login_input.fill(login)
        self.password_input.fill(password)
        self.repeat_input.fill(repeat or password)
        self.submit_btn.click()
        self.page.wait_for_timeout(300)

    def get_success(self):
        try:
            if self.success_msg.is_visible():
                return self.success_msg.inner_text()
        except Exception:
            pass
        return ""

    def get_error(self):
        """
        Zwraca tekst komunikatu błędu rejestracji, jeśli jest widoczny.
        """
        try:
            if self.error_msg.is_visible():
                return self.error_msg.inner_text()
        except Exception:
            pass
        return "" 
class LoginPage:
    """
    Page Object Model dla strony logowania.
    Pozwala na interakcję z polami loginu, hasła, przyciskiem logowania oraz obsługę komunikatów błędów.
    """
    def __init__(self, page):
        """
        Inicjalizuje LoginPage z obiektem page Playwright.
        Ustawia lokalizatory dla pól i przycisków.
        """
        self.page = page
        self.username_input = page.get_by_label('Login')
        self.password_input = page.get_by_label('Hasło')
        self.login_button = page.get_by_role('button', name='Zaloguj')
        self.error_message = page.locator('[data-testid="login-error"]')

    def is_current_page(self):
        """
        Sprawdza, czy aktualnie jesteśmy na stronie logowania.
        Zwraca True jeśli pole loginu jest widoczne i URL zawiera '/login'.
        """
        if "/login" not in self.page.url:
            return False
        try:
            self.username_input.wait_for(timeout=1000)
        except Exception:
            return False
        return self.username_input.is_visible()

    def goto(self, base_url):
        """
        Przechodzi do strony logowania pod podanym base_url.
        Zwraca True jeśli pole loginu jest widoczne.
        """
        self.page.goto(f"{base_url}/login")
        try:
            self.username_input.wait_for(timeout=2000)
        except Exception:
            return False
        return True

    def login(self, username, password):
        """
        Wypełnia formularz logowania i klika przycisk 'Zaloguj'.
        """
        if not self.is_current_page():
            raise Exception("Nie jesteś na stronie logowania!")
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        self.page.wait_for_timeout(300)

    def get_error(self):
        """
        Zwraca tekst komunikatu błędu logowania, jeśli jest widoczny.
        """
        if not self.is_current_page():
            return None
        try:
            if self.error_message.is_visible():
                return self.error_message.inner_text()
        except Exception:
            return ""
        return ""

class ProfilePage:
    """
    Page Object Model dla strony profilu użytkownika.
    Pozwala na interakcję z formularzem zmiany hasła oraz obsługę komunikatów błędów.
    """
    def __init__(self, page, base_url="http://localhost:5173"):
        """
        Inicjalizuje ProfilePage z obiektem page Playwright.
        Ustawia lokalizatory dla pól formularza i przycisku zmiany hasła.
        """
        self.page = page
        self.base_url = base_url
        self.old_pass_input = page.get_by_label('Stare hasło')
        self.new_pass_input = page.get_by_label('Nowe hasło').nth(0)
        self.repeat_input = page.get_by_label('Powtórz nowe hasło')
        self.submit_btn = page.get_by_role('button', name='Zmień hasło')
        self.success_msg = page.locator('[data-testid="profile-success"]')
        self.error_msg = page.locator('[data-testid="profile-error"]')
        self.url = f"{base_url}/profile"

    def is_current_page(self):
        if "/profile" not in self.page.url:
            return False
        try:
            self.old_pass_input.wait_for(timeout=1000)
        except Exception:
            return False
        return self.old_pass_input.is_visible()

    def goto(self, url=None):
        """
        Przechodzi do strony profilu. Jeśli podano url, używa go, w przeciwnym razie przechodzi pod domyślny adres profilu.
        """
        target_url = url if url is not None else self.url
        self.page.goto(target_url)
        self.old_pass_input.wait_for(timeout=2000)

    def change_password(self, old_pass, new_pass, repeat_pass):
        """
        Wypełnia formularz zmiany hasła i klika przycisk 'Zmień hasło'.
        """
        if not self.is_current_page():
            raise Exception("Nie jesteś na stronie profilu!")
        self.old_pass_input.fill(old_pass)
        self.new_pass_input.fill(new_pass)
        self.repeat_input.fill(repeat_pass)
        self.submit_btn.click()
        self.page.wait_for_timeout(300)

    def get_success(self):
        if not self.is_current_page():
            return None
        try:
            if self.success_msg.is_visible():
                return self.success_msg.inner_text()
        except Exception:
            return ""
        return ""

    def get_error(self):
        """
        Zwraca tekst komunikatu błędu zmiany hasła, jeśli jest widoczny.
        """
        if self.error_msg and self.error_msg.is_visible():
            return self.error_msg.inner_text()
        return "" 
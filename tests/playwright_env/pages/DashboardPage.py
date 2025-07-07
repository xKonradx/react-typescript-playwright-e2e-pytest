class DashboardPage:
    """
    Page Object Model dla dashboardu użytkownika.
    Pozwala na interakcję z nagłówkiem, przyciskiem wylogowania oraz informacją o użytkowniku.
    """
    def __init__(self, page):
        """
        Inicjalizuje DashboardPage z obiektem page Playwright.
        Ustawia lokalizatory dla nagłówka, przycisku wylogowania i informacji o użytkowniku.
        """
        self.page = page
        self.header = page.get_by_role('heading', name='Dashboard')
        self.logout_button = page.get_by_role('button', name='Wyloguj')
        self.darkmode_toggle = page.get_by_test_id('darkmode-toggle')
        self.user_info = lambda login: page.get_by_text(f"Witaj, {login}!")
        self.role_info = page.locator('div').filter(has_text='Twoja rola:')

    def is_loaded(self):
        """
        Sprawdza, czy dashboard jest załadowany (nagłówek widoczny).
        """
        return self.header.is_visible()

    def toggle_darkmode(self):
        """
        Kliknięcie przełącznika trybu ciemnego na dashboardzie.
        """
        self.darkmode_toggle.click()

    def logout(self):
        """
        Kliknięcie przycisku wylogowania na dashboardzie.
        """
        self.logout_button.click()

    def goto(self, base_url):
        """
        Przechodzi do dashboardu pod podanym base_url.
        """
        self.page.goto(f"{base_url}/dashboard")
        self.page.wait_for_selector('h4[role="heading"]')

    def get_user(self, login):
        """
        Zwraca tekst powitania użytkownika na dashboardzie.
        """
        return self.user_info(login).inner_text()

    def get_role(self):
        """
        Zwraca tekst z informacją o roli użytkownika na dashboardzie.
        """
        return self.role_info.inner_text()

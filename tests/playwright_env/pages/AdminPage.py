class AdminPage:
    """
    Page Object Model dla panelu administratora.
    Pozwala na sprawdzenie obecności nagłówka panelu admina.
    """
    def __init__(self, page):
        """
        Inicjalizuje AdminPage z obiektem page Playwright.
        Ustawia lokalizator dla nagłówka panelu admina.
        """
        self.page = page
        self.header = page.get_by_role('heading').filter(has_text='Admin Panel').first

    def is_visible(self):
        """
        Sprawdza, czy nagłówek panelu admina jest widoczny.
        """
        return self.header.is_visible()

# Playwright Codegen - Instrukcje użycia

## Uruchomienie Codegen

### 1. Interaktywny Codegen
```bash
# Uruchom codegen w trybie interaktywnym
playwright codegen http://localhost:5173

# Lub z określonym browserem
playwright codegen --browser=chromium http://localhost:5173
```

### 2. Codegen z zapisem do pliku
```bash
# Zapisz wygenerowany kod do pliku
playwright codegen --target=python -o tests/playwright_env/tests/generated_test.py http://localhost:5173
```

### 3. Codegen z określonymi lokatorami
```bash
# Użyj predefiniowanych lokatorów
playwright codegen --load-storage=auth.json http://localhost:5173
```

## Najlepsze praktyki Codegen

### 1. Struktura generowanych testów
```python
from playwright.sync_api import Page, expect

def test_generated_flow(page: Page):
    # Codegen automatycznie doda odpowiednie lokatory
    page.goto("http://localhost:5173")
    page.get_by_role("button", name="Zaloguj").click()
    page.get_by_label("Login").fill("admin")
    page.get_by_label("Hasło").fill("admin123")
    page.get_by_role("button", name="Zaloguj się").click()
    
    # Asercje
    expect(page.get_by_text("Witaj admin")).to_be_visible()
```

### 2. Optymalizacja lokatorów
- Używaj `get_by_role()` zamiast `get_by_text()`
- Preferuj `get_by_label()` dla formularzy
- Używaj `get_by_test_id()` dla custom lokatorów

### 3. Dodawanie asercji
```python
# Po wygenerowaniu kodu, dodaj asercje
expect(page).to_have_url("http://localhost:5173/dashboard")
expect(page.get_by_text("Witaj")).to_be_visible()
expect(page.get_by_role("button", name="Wyloguj")).to_be_enabled()
```

## Integracja z istniejącymi testami

### 1. Import Page Object Model
```python
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage

def test_login_flow(page: Page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    # Użyj metod z Page Object Model
    login_page.navigate()
    login_page.login("admin", "admin123")
    dashboard_page.assert_logged_in()
```

### 2. Dodawanie do istniejących klas testowych
```python
class TestLogin:
    def test_generated_login_flow(self, page: Page):
        # Wklej wygenerowany kod tutaj
        pass
```

## Debugowanie z Codegen

### 1. Trace Viewer
```bash
# Uruchom test z trace
pytest tests/test_login.py --tracing=on

# Otwórz trace viewer
playwright show-trace traces/trace-test_login_flow.zip
```

### 2. Screenshots i Video
```bash
# Uruchom z screenshotami
pytest tests/test_login.py --screenshot=on

# Uruchom z video
pytest tests/test_login.py --video=on
```

## Automatyzacja Codegen

### 1. Skrypt do generowania testów
```bash
#!/bin/bash
# generate_tests.sh

echo "Generowanie testów logowania..."
playwright codegen --target=python -o tests/playwright_env/tests/test_login_generated.py http://localhost:5173/login

echo "Generowanie testów rejestracji..."
playwright codegen --target=python -o tests/playwright_env/tests/test_register_generated.py http://localhost:5173/register
```

### 2. Integracja z CI/CD
```yaml
# .github/workflows/test-generation.yml
- name: Generate Tests
  run: |
    cd tests/playwright_env
    ./generate_tests.sh
```

## Troubleshooting

### 1. Problemy z lokatorami
- Sprawdź czy elementy mają odpowiednie role/aria-labels
- Użyj `page.pause()` do debugowania
- Sprawdź czy strona jest w pełni załadowana

### 2. Problemy z timing
- Dodaj `page.wait_for_load_state()`
- Użyj `expect().to_be_visible()` zamiast `click()`
- Dodaj `page.wait_for_timeout()` jeśli potrzebne

### 3. Problemy z autoryzacją
- Użyj `--load-storage=auth.json` do zachowania sesji
- Dodaj kroki logowania na początku testu
- Użyj `page.context.add_cookies()` dla cookies 
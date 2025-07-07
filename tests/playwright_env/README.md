# Środowisko testowe Playwright – Kompletny opis

## Opis

Ten dokument opisuje kompletne środowisko testowe Playwright dla projektu React Login Demo, w tym konfigurację, dobre praktyki oraz przewodnik rozwiązywania problemów.

## Kluczowe funkcje

### Wykonywanie równoległe
- Automatyczne uruchamianie testów równolegle
- Konfigurowalna liczba workerów
- Optymalizacja wydajności

### Trace Viewer
- Automatyczne generowanie plików trace
- Debugowanie testów krok po kroku
- Analiza wydajności

### Codegen
- Interaktywne generowanie testów
- Optymalizacja lokatorów
- Integracja z Page Object Model

### Nagrywanie wideo
- Automatyczne nagrywanie przebiegu testów
- Debugowanie wizualne
- Dokumentacja testów

## Struktura katalogów

```
playwright_env/
├── conftest.py              # Konfiguracja testów (trace/wideo)
├── pytest.ini               # Konfiguracja wykonywania równoległego
├── requirements.txt         # Zależności (pytest-xdist)
├── run_tests.py             # Skrypt uruchamiania testów
├── codegen_instructions.md  # Instrukcje codegen
├── tests/                   # Pliki testowe
├── pages/                   # Page Object Model
├── screenshots/             # Zrzuty ekranu
├── videos/                  # Nagrania wideo
├── traces/                  # Pliki trace
└── reports/                 # Raporty HTML
```

## Instalacja

```bash
cd tests/playwright_env
pip install -r requirements.txt
playwright install chromium
```

## Uruchamianie testów

### Podstawowe komendy

```bash
python run_tests.py
python run_tests.py --mode sequential
python run_tests.py --mode debug
python run_tests.py --browser firefox
python run_tests.py --trace
python run_tests.py --video
python run_tests.py --screenshot
```

### Zaawansowane opcje

```bash
python run_tests.py --tests test_login.py
python run_tests.py --workers 8
python run_tests.py --mode parallel --browser chromium --workers 4 --trace --video --screenshot
```

## Codegen – generowanie testów

### Generowanie interaktywne

```bash
playwright codegen http://localhost:5173
playwright codegen --target=python -o tests/generated_test.py http://localhost:5173
```

### Generowanie automatyczne

```bash
./generate_tests.sh
```

## Trace Viewer

### Otwieranie plików trace

```bash
playwright show-trace traces/trace-test_name.zip
playwright show-trace traces/trace-test_login_flow.zip
```

### Analiza trace

1. Otwórz plik trace w przeglądarce
2. Przejdź przez kroki testu
3. Sprawdź żądania sieciowe
4. Analizuj czasy i wydajność

## Nagrywanie wideo

### Przeglądanie nagrań

```bash
ls videos/
```

### Konfiguracja nagrywania

```python
context = browser.new_context(
    record_video_dir="videos/",
    record_video_size={"width": 1280, "height": 720}
)
```

## Zrzuty ekranu

### Automatyczne zrzuty ekranu

```bash
ls screenshots/
```

### Ręczne zrzuty ekranu

```python
page.screenshot(path="screenshot.png")
```

## Raporty

### Raporty HTML

```bash
open reports/report.html
```

### Raporty niestandardowe

```bash
python run_tests.py --metadata "Environment" "Production"
```

## Debugowanie

### Tryb debugowania

```bash
python run_tests.py --mode debug
```

### Pauza w testach

```python
page.pause()
```

### Analiza trace

```bash
playwright show-trace traces/trace.zip
```

## Integracja CI/CD

### GitHub Actions

```yaml
- name: Run Playwright Tests
  run: |
    cd tests/playwright_env
    python run_tests.py --mode parallel --workers 4 --trace
```

### Wykonywanie równoległe w CI

```yaml
- name: Install dependencies
  run: |
    pip install -r tests/playwright_env/requirements.txt
    playwright install chromium

- name: Run tests
  run: |
    cd tests/playwright_env
    python run_tests.py --mode parallel --workers 4
```

## Dobre praktyki

### 1. Lokatory
- Używaj `get_by_role()` zamiast `get_by_text()`
- Preferuj `get_by_label()` dla formularzy
- Dodawaj `data-testid` dla niestandardowych lokatorów

### 2. Asercje
- Używaj `expect()` zamiast `assert` tam, gdzie to możliwe
- Dodawaj timeouty do asercji
- Sprawdzaj stan elementu przed interakcją

### 3. Wydajność
- Wykorzystuj wykonywanie równoległe
- Optymalizuj setup/teardown
- Monitoruj czasy z użyciem trace viewer

### 4. Utrzymanie
- Regularnie aktualizuj lokatory
- Stosuj Page Object Model
- Dokumentuj niestandardowe helpery

## Pokrycie testowe

| Kategoria       | Liczba testów | Zakres                                                                                                                                                       |
|-----------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dostępność      | 13            | WCAG 2.1, screen reader, kontrast, nawigacja, tytuł, nagłówki, alt text, etykiety, klawiatura, skip links, powiększanie, fokus, język, komunikaty, walidacja |
| Logowanie       | 3             | Poprawne i błędne logowanie (admin/user)                                                                                                                     |
| Wydajność       | 14            | Ładowanie, logowanie, rejestracja, pamięć, DOM, sesje, API, requests, przewijanie, animacje, zasoby, responsywność, cache, TTI                               |
| Edycja profilu  | 5             | Zmiana hasła, walidacja danych                                                                                                                               |
| Rejestracja     | 5             | Sukces, walidacja loginu, hasła, zgodności                                                                                                                   |
| Bezpieczeństwo  | 11            | XSS, SQLi, CSRF, sesje, autoryzacja, timeout, rate limiting, ekspozycja danych, kontrola dostępu, wylogowanie                                                |
| Interfejs       | 11            | Ochrona tras, darkmode, modal, snapshoty, responsywność, 404, loading, walidacja UI                                                                          |

Łączna liczba testów automatycznych: 62

## Testy wizualne (snapshoty)

Testy wizualne wykorzystują plugin `pytest-playwright-snapshot` do automatycznego porównywania zrzutów ekranu z zapisanymi wzorcami (snapshotami).

- Snapshoty są zapisywane w katalogu `__snapshots__` w strukturze odpowiadającej testom, przeglądarce i systemowi operacyjnemu.
- Jeśli snapshot nie istnieje lub UI się zmienił, test nie przejdzie i wyświetli informację o różnicy.

### Jak dodać lub zaktualizować snapshoty?

1. Uruchom testy z flagą:
   ```bash
   pytest --update-snapshots
   ```
2. Nowe snapshoty zostaną zapisane w katalogu `__snapshots__`.
3. Przy kolejnym uruchomieniu testy będą porównywać się z tymi wzorcami.

### Przykład użycia w teście

```python
def test_login_page_visual_comparison(page, assert_snapshot):
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    assert_snapshot(page.screenshot(), "login-page.png")
```

Więcej informacji: [pytest-playwright-snapshot](https://github.com/mxschmitt/pytest-playwright-snapshot)

## Ograniczenia Playwright Python

### Expect assertions z konkretnymi matcherami

Playwright dla Pythona nie zapewnia pełnego wsparcia dla tzw. "expect matchers" znanych z JavaScript/TypeScript. Oznacza to:

#### Różnice między JS/TS a Python:

JavaScript/TypeScript (pełne wsparcie):
```javascript
await expect(page.locator('text=Hello')).toBeVisible();
await expect(page.locator('button')).toHaveText('Wyślij');
await expect(page.locator('input')).toHaveAttribute('type', 'email');
await expect(page.locator('.class')).toHaveClass('active');
```

Python (ograniczone wsparcie):
```python
assert await page.is_visible('text=Hello')
assert await page.text_content('button') == 'Wyślij'
assert await page.get_attribute('input', 'type') == 'email'
assert 'active' in await page.get_attribute('.class', 'class')
```

#### Dlaczego to jest ograniczenie?

1. Mniej czytelne asercje – klasyczne `assert` zamiast dedykowanych matcherów
2. Brak zaawansowanych matcherów – brak `.toHaveAttribute()`, `.toHaveClass()`, `.toBeEnabled()` itd.
3. Mniejsza odporność na zmiany UI – niektóre asercje mogą być mniej stabilne
4. Więcej kodu pomocniczego – niektóre sprawdzenia trzeba implementować ręcznie

#### Jak sobie radzić?

```python
# Zamiast expect().toHaveAttribute()
def assert_element_has_attribute(page, selector, attribute, value):
    actual_value = await page.get_attribute(selector, attribute)
    assert actual_value == value, f"Expected {attribute}={value}, got {actual_value}"

# Zamiast expect().toHaveClass()
def assert_element_has_class(page, selector, expected_class):
    class_attr = await page.get_attribute(selector, 'class')
    assert expected_class in class_attr.split(), f"Class {expected_class} not found in {class_attr}"

# Zamiast expect().toBeEnabled()
def assert_element_is_enabled(page, selector):
    disabled = await page.get_attribute(selector, 'disabled')
    assert disabled is None, f"Element {selector} is disabled"
```

#### Podsumowanie

| Funkcjonalność              | JS/TS         | Python        | Status             |
|-----------------------------|---------------|---------------|--------------------|
| Podstawowe asercje          | Tak           | Tak           | Pełne wsparcie     |
| Zaawansowane matchery       | Tak           | Nie           | Brak wsparcia      |
| Czytelność kodu             | Wysoka        | Ograniczona   | Ograniczona        |
| Odporność na zmiany w UI    | Wysoka        | Częściowa     | Częściowa          |

To nie jest błąd ani problem krytyczny – testy są poprawne i działają, ale nie mają tej samej ergonomii co w JS/TS.

## Rozwiązywanie problemów

### Problemy z wykonywaniem równoległym

```bash
python run_tests.py --workers 1
python run_tests.py --mode sequential -v
```

### Problemy z trace viewer

```bash
ls traces/
playwright show-trace traces/latest.zip
```

### Problemy z nagraniami wideo

```bash
ls videos/
# Sprawdź konfigurację w conftest.py
```

## Dodatkowe zasoby

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest-xdist](https://pytest-xdist.readthedocs.io/)
- [Trace Viewer Guide](https://playwright.dev/python/docs/trace-viewer)
- [Codegen Guide](https://playwright.dev/python/docs/codegen)

- Optymalizacja liczby żądań sieciowych (test automatycznie pomijany w trybie deweloperskim) 
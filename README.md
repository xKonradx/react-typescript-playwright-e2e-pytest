# TS-React + Playwright-Pytest (Python) Demo

## Licencja
Kod udostępniony wyłącznie do wglądu na potrzeby rekrutacyjne. Wszelkie prawa zastrzeżone. Zakaz modyfikowania, kopiowania i używania w innych celach.

## Opis projektu
Aplikacja demonstracyjna systemu logowania z autoryzacją ról, ochroną tras, trybem jasnym/ciemnym oraz kompletnymi testami automatycznymi.

## Instalacja i uruchomienie

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Aplikacja dostępna pod adresem: http://localhost:5173

### Testy automatyczne E2E
```bash
cd tests/playwright_env
pip install -r requirements.txt
python -m playwright install
pytest
```

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

## Dane testowe
Domyślni użytkownicy (plik `frontend/src/data/users.json`):
| Login | Hasło   | Rola           |
|-------|---------|----------------|
| admin | admin123| administrator  |
| user  | user123 | użytkownik     |

## Struktura projektu
```
react-login-demo/
├── frontend/                 # Aplikacja React
│   ├── src/
│   │   ├── components/       # Komponenty interfejsu
│   │   ├── context/          # Kontekst autoryzacji
│   │   ├── views/            # Widoki aplikacji
│   │   └── routes/           # Routing
│   └── package.json
└── tests/playwright_env/     # Testy automatyczne
    ├── pages/                # Page Objects
    ├── tests/                # Testy
    └── requirements.txt
```

## Funkcjonalności
- Rejestracja i logowanie użytkowników z walidacją
- System ról (administrator/użytkownik)
- Ochrona tras wymagających autoryzacji
- Edycja profilu użytkownika
- Tryb jasny/ciemny
- Przełącznik trybu jasnego/ciemnego
- Modal potwierdzenia wylogowania
- Responsywny interfejs

## Testy automatyczne E2E
Aplikacja zawiera kompleksowy zestaw 62 testów automatycznych E2E pokrywających wszystkie kluczowe funkcjonalności zgodnie ze standardami ISO/IEC/IEEE 29119, ISTQB, OWASP Top 10 oraz WCAG 2.1.

### Ocena ryzyka

#### Ryzyka funkcjonalne
| Ryzyko                 | Prawdopodobieństwo | Wpływ     | Priorytet | Działania zapobiegawcze |
|------------------------|--------------------|-----------|-----------|-------------------------|
| Błędne logowanie       | Średnie            | Wysoki    | Wysoki    | Testy walidacji danych  |
| Nieautoryzowany dostęp | Niskie             | Krytyczny | Wysoki    | Testy ochrony tras      |
| Utrata danych sesji    | Niskie             | Średni    | Średni    | Testy wylogowania       |

#### Ryzyka techniczne
| Ryzyko                 | Prawdopodobieństwo | Wpływ     | Priorytet | Działania zapobiegawcze   |
|------------------------|--------------------|-----------|-----------|---------------------------|
| Problemy z przeglądarką| Średnie            | Średni    | Średni    | Testy wieloprzeglądarkowe |
| Wolne wykonanie testów | Wysokie            | Niski     | Niski     | Optymalizacja testów      |
| Niestabilne testy      | Średnie            | Średni    | Średni    | Stabilizacja testów       |

#### Ryzyka bezpieczeństwa
| Ryzyko        | Prawdopodobieństwo | Wpływ     | Priorytet | Działania zapobiegawcze |
|---------------|--------------------|-----------|-----------|-------------------------|
| Ataki XSS     | Niskie             | Krytyczny | Wysoki    | Testy bezpieczeństwa    |
| Ataki CSRF    | Niskie             | Krytyczny | Wysoki    | Testy tokenów           |
| SQL Injection | Niskie             | Krytyczny | Wysoki    | Walidacja danych        |

## Zakres testów

### Testy logowania
- Poprawne logowanie dla administratora i użytkownika
- Obsługa błędnych danych logowania
- Weryfikacja dostępu do odpowiednich sekcji

### Testy rejestracji
- Pomyślna rejestracja nowych użytkowników
- Walidacja istnienia loginu
- Walidacja wymagań hasła (min. 6 znaków)
- Walidacja zgodności pól hasła

### Testy edycji profilu
- Pomyślna zmiana hasła
- Walidacja poprawności starego hasła
- Walidacja długości nowego hasła
- Walidacja zgodności pól hasła

### Testy bezpieczeństwa
- Kontrola dostępu, ochrona przed CSRF
- Zarządzanie sesją, ochrona danych
- Ochrona przed XSS, SQL Injection, walidacja danych wejściowych
- Ograniczanie liczby prób (rate limiting)
- Bezpieczna obsługa wylogowania
- Ochrona przed obejściem uwierzytelniania

### Testy dostępności
- Tekst alternatywny dla obrazów
- Struktura nagłówków, wsparcie czytników ekranu
- Kontrast kolorów
- Powiększanie tekstu
- Nawigacja klawiaturą
- Linki pomijające nawigację
- Tytuły stron
- Widoczność fokusu
- Deklaracja języka strony
- Identyfikacja błędów, walidacja formularzy
- Etykiety pól formularzy

### Testy wydajnościowe
- Pomiar czasu ładowania strony oraz szybkości logowania i rejestracji
- Monitorowanie pamięci JavaScript
- Optymalizacja liczby żądań sieciowych (test automatycznie pomijany w trybie deweloperskim)
- Walidacja liczby elementów w drzewie DOM
- Test równoczesnych sesji (każdy użytkownik w osobnym kontekście przeglądarki)
- Pomiar czasu odpowiedzi symulowanych zapytań
- Sprawdzanie płynności przewijania
- Ocena płynności przejść i animacji
- Optymalizacja ładowania plików i zasobów
- Testy na różnych rozdzielczościach i urządzeniach

### Testy interfejsu
- Przełącznik trybu jasnego/ciemnego
- Proces wylogowania z potwierdzeniem

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

## Metryki jakościowe

### Typy testów
- Scenariusz podstawowy: typowe scenariusze użytkownika
- Walidacja: walidacja danych wejściowych
- Bezpieczeństwo: testy bezpieczeństwa OWASP
- Dostępność: testy dostępności WCAG
- Wydajność: testy wydajnościowe
- Doświadczenie użytkownika: testy UX

### Środowisko testowe
- Przeglądarka: Chromium (tryb bezgłowy)
- Framework: Playwright + pytest
- Język: Python 3.8+
- Automatyzacja: zrzuty ekranu przy błędach

### Wydajność
- Średni czas wykonania: ~2,4 s na test
- Całkowity czas: ~2 minuty dla wszystkich testów
- Najwolniejsze testy: testy wydajnościowe (~5 s)
- Kryteria zakończenia: wszystkie testy muszą zakończyć się sukcesem (100% pass rate)
- Harmonogram: zdefiniowany w `tests/playwright_env/test_schedule.md`

## Komercyjne standardy testów

### Checklista implementacji

| Standard                    | Status     | Opis                                                                         |
|-----------------------------|------------|------------------------------------------------------------------------------|
| Wykonywanie równoległe      | Pełne      | Automatyczne uruchamianie testów równolegle z konfigurowalną liczbą workerów |
| Trace Viewer                | Pełne      | Automatyczne generowanie plików trace z debugowaniem krok po kroku           |
| Codegen                     | Pełne      | Interaktywne generowanie testów z optymalizacją lokatorów                    |
| Nagrywanie wideo            | Pełne      | Automatyczne nagrywanie przebiegu testów dla debugowania wizualnego          |
| Page Object Model           | Pełne      | Implementacja POM z separacją logiki testów od lokatorów                     |
| Lokatory odporne            | Pełne      | Używanie get_by_role(), get_by_label() zamiast niestabilnych selektorów      |
| Hooks                       | Pełne      | Automatyczne setup/teardown z zarządzaniem kontekstami przeglądarki          |
| Asercje expect-style        | Częściowe  | Używanie assert z helperami (ograniczenia Pythona vs JS/TS)                  |
| Testy wizualne              | Pełne      | Automatyczne porównywanie snapshotów z pytest-playwright-snapshot            |
| Testy wydajnościowe         | Pełne      | Testy z automatycznym pomijaniem w trybie dev i limitami produkcyjnymi       |
| Testy bezpieczeństwa        | Pełne      | Pokrycie OWASP Top 10 z testami XSS, CSRF, SQL Injection                     |
| Testy dostępności           | Pełne      | Zgodność z WCAG 2.1 z testami czytników ekranu, kontrastu, nawigacji         |
| Integracja CI/CD            | Pełne      | Konfiguracja GitHub Actions z wykonywaniem równoległym                       |
| Dokumentacja                | Pełne      | Kompletna dokumentacja w języku polskim z przykładami użycia                 |

### Standardy testów wydajnościowych

- Środowisko testowe: testy uruchamiane na buildzie produkcyjnym dla dokładnych pomiarów
- Automatyczne pomijanie: test liczby requestów pomijany w trybie deweloperskim (Vite HMR)
- Konfigurowalne limity: limity dostosowane do wymagań produkcyjnych (20 requestów)
- Jasne komunikaty: wyjaśnienia dlaczego test został pominięty
- Integracja CI/CD: automatyczne uruchamianie testów wydajnościowych na buildzie produkcyjnym

### Zarządzanie danymi testowymi

Plik `frontend/src/data/users.json` zawiera przykładowych użytkowników wykorzystywanych w testach automatycznych.

## Dodatkowe zasoby

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest-xdist](https://pytest-xdist.readthedocs.io/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [WCAG 2.1](https://www.w3.org/TR/WCAG21/)

# Przypadki testowe – Dostępność (Accessibility)

Przypadki testowe dotyczące dostępności aplikacji, zgodne z WCAG 2.1.

### TC-001: Tytuł strony

Cel:
Weryfikacja poprawności tytułu strony głównej.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Otwórz stronę główną
2. Sprawdź tytuł strony w zakładce przeglądarki

Dane testowe:
- Brak

Oczekiwany rezultat:
- Tytuł strony jest zgodny z wymaganiami projektu

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_accessibility.py::test_page_title`

Uwagi:
Brak

### TC-002: Struktura nagłówków

Cel:
Weryfikacja logicznej struktury nagłówków H1-H6.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Otwórz stronę główną
2. Sprawdź hierarchię nagłówków H1-H6

Dane testowe:
- Brak

Oczekiwany rezultat:
- Struktura nagłówków jest logiczna, brak pominiętych poziomów

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_accessibility.py::test_heading_structure`

Uwagi:
Brak

### TC-003: Tekst alternatywny dla obrazów

Cel:
Weryfikacja obecności i poprawności tekstów alternatywnych dla obrazów.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Otwórz stronę główną
2. Sprawdź atrybuty alt wszystkich obrazów

Dane testowe:
- Brak

Oczekiwany rezultat:
- Wszystkie obrazy mają opisowy tekst alternatywny

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_accessibility.py::test_alt_text_for_images`

Uwagi:
Brak

### TC-004: Etykiety formularzy

Cel:
Weryfikacja obecności i powiązania etykiet z polami formularzy.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Otwórz formularze logowania i rejestracji
2. Sprawdź etykiety pól

Dane testowe:
- Brak

Oczekiwany rezultat:
- Każde pole ma czytelną etykietę powiązaną przez for/id

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_accessibility.py::test_form_labels`

Uwagi:
Brak

### TC-005: Kontrast kolorów

Cel:
Weryfikacja kontrastu kolorów zgodnie z WCAG.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Sprawdź kontrast tekstu, przycisków i linków

Dane testowe:
- Brak

Oczekiwany rezultat:
- Kontrast spełnia standardy WCAG AA (min. 4.5:1)

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_accessibility.py::test_color_contrast`

Uwagi:
Brak

### TC-006: Obsługa klawiatury

Cel:
Weryfikacja dostępności wszystkich funkcji za pomocą klawiatury.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Użyj Tab do nawigacji
2. Użyj Enter/Space do aktywacji
3. Użyj Escape do zamykania modali

Dane testowe:
- Brak

Oczekiwany rezultat:
- Wszystkie elementy są dostępne, widoczny wskaźnik fokusu

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_accessibility.py::test_keyboard_navigation`

Uwagi:
Brak

### TC-007: Skip links

Cel:
Weryfikacja obecności i działania linków do pomijania nawigacji.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Otwórz stronę
2. Użyj Tab, aby sprawdzić obecność skip links

Dane testowe:
- Brak

Oczekiwany rezultat:
- Skip links są widoczne i działają poprawnie

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_accessibility.py::test_skip_links`

Uwagi:
Brak

### TC-008: Obsługa czytników ekranu

Cel:
Weryfikacja kompatybilności z czytnikami ekranu.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Uruchom czytnik ekranu
2. Przejdź przez aplikację

Dane testowe:
- Brak

Oczekiwany rezultat:
- Wszystkie elementy są czytane poprawnie, komunikaty o błędach są ogłaszane

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_accessibility.py::test_screen_reader_support`

Uwagi:
Brak

### TC-009: Powiększanie tekstu

Cel:
Weryfikacja możliwości powiększenia tekstu bez utraty funkcjonalności.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Powiększ tekst do 200%
2. Sprawdź czytelność i funkcjonalność

Dane testowe:
- Brak

Oczekiwany rezultat:
- Tekst pozostaje czytelny, funkcjonalność nie jest utracona

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_accessibility.py::test_resize_text`

Uwagi:
Brak

### TC-010: Wskaźnik fokusu

Cel:
Weryfikacja widoczności wskaźnika fokusu podczas nawigacji klawiaturą.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Użyj Tab do nawigacji
2. Sprawdź widoczność wskaźnika na aktywnym elemencie

Dane testowe:
- Brak

Oczekiwany rezultat:
- Wskaźnik fokusu jest widoczny na wszystkich interaktywnych elementach

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_accessibility.py::test_focus_indicator`

Uwagi:
Brak

### TC-011: Deklaracja języka strony

Cel:
Weryfikacja poprawności atrybutu lang w tagu <html>.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Otwórz stronę
2. Sprawdź atrybut lang

Dane testowe:
- Brak

Oczekiwany rezultat:
- Atrybut lang jest ustawiony zgodnie z wymaganiami

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_accessibility.py::test_language_declaration`

Uwagi:
Brak

### TC-012: Komunikaty o błędach

Cel:
Weryfikacja widoczności i treści komunikatów o błędach.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Wywołaj błąd (np. błędne dane w formularzu)
2. Sprawdź komunikat

Dane testowe:
- Brak

Oczekiwany rezultat:
- Komunikat o błędzie jest widoczny i zrozumiały

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_accessibility.py::test_error_messages`

Uwagi:
Brak

### TC-013: Walidacja formularzy

Cel:
Weryfikacja walidacji pól formularzy.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Wprowadź nieprawidłowe dane
2. Zatwierdź formularz

Dane testowe:
- Brak

Oczekiwany rezultat:
- Wyświetlony komunikat o błędzie walidacji

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_accessibility.py::test_form_validation`

Uwagi:
Brak

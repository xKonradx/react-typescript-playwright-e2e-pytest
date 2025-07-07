# Przypadki testowe – Interfejs użytkownika (UI)

Przypadki testowe dotyczące interfejsu użytkownika, wyglądu i responsywności.

### TC-052: Ochrona tras

Cel:
Weryfikacja ochrony tras wymagających autoryzacji.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Spróbuj wejść na chronioną trasę bez logowania

Dane testowe:
- Brak

Oczekiwany rezultat:
- Przekierowanie na logowanie, brak dostępu

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_ui.py::test_protected_routes`

Uwagi:
Brak

### TC-053: Przełącznik trybu jasny/ciemny

Cel:
Weryfikacja działania przełącznika trybu jasny/ciemny.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Przełącz tryb jasny/ciemny
2. Sprawdź zmiany w interfejsie

Dane testowe:
- Brak

Oczekiwany rezultat:
- Interfejs zmienia się zgodnie z wybranym trybem

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_ui.py::test_darkmode_toggle`

Uwagi:
Brak

### TC-054: Modal wylogowania

Cel:
Weryfikacja działania modalu potwierdzenia wylogowania.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Kliknij 'Wyloguj'
2. Sprawdź pojawienie się modalu
3. Potwierdź lub anuluj

Dane testowe:
- Brak

Oczekiwany rezultat:
- Modal działa poprawnie, sesja kończy się po potwierdzeniu

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_ui.py::test_logout_modal`

Uwagi:
Brak

### TC-055: Wygląd strony logowania

Cel:
Weryfikacja wyglądu strony logowania (snapshot test).

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Otwórz stronę logowania
2. Sprawdź układ, kolory, style

Dane testowe:
- Brak

Oczekiwany rezultat:
- Strona wygląda zgodnie z projektem

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_ui.py::test_login_page_visual_comparison[chromium]`

Uwagi:
Brak

### TC-056: Wygląd dashboardu

Cel:
Weryfikacja wyglądu dashboardu (snapshot test).

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Otwórz dashboard
2. Sprawdź układ, kolory, style

Dane testowe:
- Brak

Oczekiwany rezultat:
- Dashboard wygląda zgodnie z projektem

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_ui.py::test_dashboard_page_visual_comparison[chromium]`

Uwagi:
Brak

### TC-057: Wygląd strony rejestracji

Cel:
Weryfikacja wyglądu strony rejestracji (snapshot test).

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Otwórz stronę rejestracji
2. Sprawdź układ, kolory, style

Dane testowe:
- Brak

Oczekiwany rezultat:
- Strona wygląda zgodnie z projektem

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_ui.py::test_register_page_visual_comparison[chromium]`

Uwagi:
Brak

### TC-058: Wygląd strony błędu

Cel:
Weryfikacja wyglądu strony błędu (snapshot test).

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Otwórz stronę błędu
2. Sprawdź układ, kolory, style

Dane testowe:
- Brak

Oczekiwany rezultat:
- Strona błędu wygląda zgodnie z projektem

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_ui.py::test_error_page_visual_comparison[chromium]`

Uwagi:
Brak

### TC-059: Responsywność interfejsu

Cel:
Weryfikacja responsywności interfejsu na różnych urządzeniach.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Zmień rozmiar okna
2. Sprawdź wygląd na desktop/mobile

Dane testowe:
- Brak

Oczekiwany rezultat:
- Interfejs jest czytelny i funkcjonalny na wszystkich rozdzielczościach

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_ui.py::test_responsive_visual_comparison[chromium]`

Uwagi:
Brak

### TC-060: Strona 404

Cel:
Weryfikacja wyświetlania strony 404 dla nieistniejących tras.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Przejdź do nieistniejącej trasy

Dane testowe:
- Brak

Oczekiwany rezultat:
- Wyświetlana jest strona 404

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_ui.py::test_404_page`

Uwagi:
Brak

### TC-061: Stany ładowania

Cel:
Weryfikacja poprawności wyświetlania stanów ładowania.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Wywołaj sytuację ładowania (np. przejście między widokami)

Dane testowe:
- Brak

Oczekiwany rezultat:
- Wyświetlany jest odpowiedni wskaźnik ładowania

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_ui.py::test_loading_states`

Uwagi:
Brak

### TC-062: Walidacja formularzy UI

Cel:
Weryfikacja walidacji formularzy na poziomie interfejsu użytkownika.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Wprowadź nieprawidłowe dane w formularzu
2. Zatwierdź formularz

Dane testowe:
- Brak

Oczekiwany rezultat:
- Wyświetlany jest komunikat o błędzie walidacji

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_ui.py::test_form_validation_ui`

Uwagi:
Brak

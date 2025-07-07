# Przypadki testowe – Bezpieczeństwo

Przypadki testowe dotyczące bezpieczeństwa aplikacji.

### TC-041: Ochrona przed XSS

Cel:
Weryfikacja odporności na ataki Cross-Site Scripting.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Wprowadź payload XSS w polu tekstowym
2. Zatwierdź formularz

Dane testowe:
- Brak

Oczekiwany rezultat:
- Payload nie jest wykonywany, brak alertu

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_security.py::test_xss_protection`

Uwagi:
Brak

### TC-042: Ochrona przed SQL Injection

Cel:
Weryfikacja odporności na ataki SQL Injection.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Wprowadź payload SQLi w polu login
2. Zatwierdź formularz

Dane testowe:
- Brak

Oczekiwany rezultat:
- Brak nieautoryzowanego dostępu, komunikat o błędzie

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_security.py::test_sql_injection_protection`

Uwagi:
Brak

### TC-043: Ochrona przed CSRF

Cel:
Weryfikacja ochrony przed atakami Cross-Site Request Forgery.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Wygeneruj żądanie POST bez tokena CSRF
2. Prześlij żądanie

Dane testowe:
- Brak

Oczekiwany rezultat:
- Żądanie zostaje odrzucone, hasło niezmienione

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_security.py::test_csrf_protection`

Uwagi:
Brak

### TC-044: Próba obejścia uwierzytelniania

Cel:
Weryfikacja braku dostępu do chronionych zasobów bez autoryzacji.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Przejdź do chronionego adresu bez logowania

Dane testowe:
- Brak

Oczekiwany rezultat:
- Przekierowanie na stronę logowania, brak dostępu

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_security.py::test_authentication_bypass`

Uwagi:
Brak

### TC-045: Zarządzanie sesją użytkownika

Cel:
Weryfikacja poprawnego zarządzania sesją.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Zaloguj się
2. Zamknij przeglądarkę lub wyczyść cookies
3. Otwórz aplikację ponownie

Dane testowe:
- Brak

Oczekiwany rezultat:
- Użytkownik nie jest już zalogowany, wymagane ponowne logowanie

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_security.py::test_session_management`

Uwagi:
Brak

### TC-046: Walidacja danych wejściowych

Cel:
Weryfikacja walidacji danych wejściowych użytkownika.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Wprowadź nieprawidłowe dane w formularzu
2. Zatwierdź formularz

Dane testowe:
- Brak

Oczekiwany rezultat:
- Komunikat o błędzie walidacji, brak rejestracji/zmiany hasła

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_security.py::test_input_validation`

Uwagi:
Brak

### TC-047: Ograniczanie liczby prób logowania

Cel:
Weryfikacja ograniczenia liczby prób logowania (rate limiting).

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Wprowadź wielokrotnie błędne dane logowania
2. Obserwuj zachowanie aplikacji

Dane testowe:
- Brak

Oczekiwany rezultat:
- Po przekroczeniu limitu pojawia się blokada lub komunikat o zbyt wielu próbach

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_security.py::test_rate_limiting`

Uwagi:
Brak

### TC-048: Ekspozycja wrażliwych danych

Cel:
Weryfikacja braku ujawniania wrażliwych danych użytkownika.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Przejdź do profilu/dashboardu
2. Sprawdź, czy nie są wyświetlane hasła, tokeny lub inne dane wrażliwe

Dane testowe:
- Brak

Oczekiwany rezultat:
- Wrażliwe dane nie są widoczne w interfejsie ani w odpowiedziach API

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_security.py::test_sensitive_data_exposure`

Uwagi:
Brak

### TC-049: Kontrola autoryzacji

Cel:
Weryfikacja braku dostępu do zasobów poza rolą użytkownika.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Zaloguj się jako user
2. Spróbuj wejść na stronę /admin

Dane testowe:
- Brak

Oczekiwany rezultat:
- Brak dostępu do panelu admina, komunikat o braku uprawnień lub przekierowanie

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_security.py::test_authorization_controls`

Uwagi:
Brak

### TC-050: Bezpieczne wylogowanie

Cel:
Weryfikacja unieważniania sesji po wylogowaniu.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Zaloguj się
2. Kliknij 'Wyloguj'
3. Spróbuj wrócić do chronionych zasobów

Dane testowe:
- Brak

Oczekiwany rezultat:
- Brak dostępu do chronionych zasobów, przekierowanie na logowanie

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_security.py::test_logout_security`

Uwagi:
Brak

### TC-051: Timeout sesji

Cel:
Weryfikacja wygaśnięcia sesji po określonym czasie bezczynności.

Wymagania wstępne:
- Aplikacja uruchomiona

Kroki testowe:
1. Zaloguj się
2. Pozostaw aplikację bez aktywności przez określony czas
3. Spróbuj wykonać akcję

Dane testowe:
- Brak

Oczekiwany rezultat:
- Sesja wygasa, wymagane ponowne logowanie

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_security.py::test_session_timeout`

Uwagi:
Brak

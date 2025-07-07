# Przypadki testowe – Logowanie

Przypadki testowe dotyczące procesu logowania.

### TC-014: Logowanie jako administrator

Cel:
Weryfikacja poprawnego logowania administratora.

Wymagania wstępne:
- Aplikacja uruchomiona

Dane testowe:
login: admin, hasło: admin123

Kroki testowe:
1. Przejdź do logowania
2. Wprowadź dane
3. Zaloguj się

Oczekiwany rezultat:
- Zalogowanie i przekierowanie do dashboardu admina

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_login.py::test_login_success[admin-admin123-admin]`

Uwagi:
Brak

### TC-015: Logowanie jako użytkownik

Cel:
Weryfikacja poprawnego logowania zwykłego użytkownika.

Wymagania wstępne:
- Aplikacja uruchomiona

Dane testowe:
login: user, hasło: user123

Kroki testowe:
1. Przejdź do logowania
2. Wprowadź dane
3. Zaloguj się

Oczekiwany rezultat:
- Zalogowanie i przekierowanie do dashboardu użytkownika

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_login.py::test_login_success[user-user123-user]`

Uwagi:
Brak

### TC-016: Logowanie z błędnymi danymi

Cel:
Weryfikacja obsługi nieprawidłowych danych logowania.

Wymagania wstępne:
- Aplikacja uruchomiona

Dane testowe:
login: wrong, hasło: wrong

Kroki testowe:
1. Przejdź do logowania
2. Wprowadź błędne dane
3. Zaloguj się

Oczekiwany rezultat:
- Komunikat o błędzie, brak zalogowania

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_login.py::test_login_invalid`

Uwagi:
Brak

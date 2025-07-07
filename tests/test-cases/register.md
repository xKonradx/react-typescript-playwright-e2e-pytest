# Przypadki testowe – Rejestracja

Przypadki testowe dotyczące procesu rejestracji.

### TC-036: Rejestracja – sukces (testuser1)

Cel:
Weryfikacja poprawnej rejestracji nowego użytkownika.

Wymagania wstępne:
- Aplikacja uruchomiona

Dane testowe:
login: testuser1, hasło: testpass123

Kroki testowe:
1. Przejdź do rejestracji
2. Wprowadź dane
3. Zarejestruj się

Oczekiwany rezultat:
- Użytkownik zarejestrowany, przekierowanie do logowania

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_register.py::test_register_success[testuser1-testpass123]`

Uwagi:
Brak

### TC-037: Rejestracja – sukces (testuser2)

Cel:
Weryfikacja poprawnej rejestracji nowego użytkownika.

Wymagania wstępne:
- Aplikacja uruchomiona

Dane testowe:
login: testuser2, hasło: testpass456

Kroki testowe:
1. Przejdź do rejestracji
2. Wprowadź dane
3. Zarejestruj się

Oczekiwany rezultat:
- Użytkownik zarejestrowany, przekierowanie do logowania

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_register.py::test_register_success[testuser2-testpass456]`

Uwagi:
Brak

### TC-038: Rejestracja z istniejącym loginem

Cel:
Weryfikacja walidacji unikalności loginu.

Wymagania wstępne:
- Aplikacja uruchomiona

Dane testowe:
login: user, hasło: dowolne

Kroki testowe:
1. Przejdź do rejestracji
2. Wprowadź istniejący login
3. Zarejestruj się

Oczekiwany rezultat:
- Komunikat o zajętym loginie, brak rejestracji

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_register.py::test_register_existing_login`

Uwagi:
Brak

### TC-039: Rejestracja ze słabym hasłem

Cel:
Weryfikacja walidacji siły hasła.

Wymagania wstępne:
- Aplikacja uruchomiona

Dane testowe:
login: testuser4, hasło: 123

Kroki testowe:
1. Przejdź do rejestracji
2. Wprowadź słabe hasło
3. Zarejestruj się

Oczekiwany rezultat:
- Komunikat o słabym haśle, brak rejestracji

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_register.py::test_register_weak_password`

Uwagi:
Brak

### TC-040: Rejestracja z niezgodnymi hasłami

Cel:
Weryfikacja walidacji zgodności haseł.

Wymagania wstępne:
- Aplikacja uruchomiona

Dane testowe:
login: testuser3, hasło: testpass123, powtórz: innehaslo

Kroki testowe:
1. Przejdź do rejestracji
2. Wprowadź różne hasła
3. Zarejestruj się

Oczekiwany rezultat:
- Komunikat o niezgodności haseł, brak rejestracji

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_register.py::test_register_password_mismatch`

Uwagi:
Brak

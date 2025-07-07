# Przypadki testowe – Profil użytkownika

Przypadki testowe dotyczące zarządzania profilem i zmianą hasła.

### TC-031: Zmiana hasła – sukces (user)

Cel:
Weryfikacja poprawnej zmiany hasła przez użytkownika.

Wymagania wstępne:
- Aplikacja uruchomiona

Dane testowe:
login: user, stare hasło: user123, nowe hasło: nowehaslo1

Kroki testowe:
1. Zaloguj się
2. Przejdź do profilu
3. Zmień hasło

Oczekiwany rezultat:
- Hasło zmienione, komunikat o sukcesie

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_profile.py::test_change_password_success[user-user123-nowehaslo1]`

Uwagi:
Brak

### TC-032: Zmiana hasła – sukces (admin)

Cel:
Weryfikacja poprawnej zmiany hasła przez administratora.

Wymagania wstępne:
- Aplikacja uruchomiona

Dane testowe:
login: admin, stare hasło: admin123, nowe hasło: nowehaslo2

Kroki testowe:
1. Zaloguj się
2. Przejdź do profilu
3. Zmień hasło

Oczekiwany rezultat:
- Hasło zmienione, komunikat o sukcesie

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_profile.py::test_change_password_success[admin-admin123-nowehaslo2]`

Uwagi:
Brak

### TC-033: Zmiana hasła – nieprawidłowe stare hasło

Cel:
Weryfikacja walidacji starego hasła przy zmianie.

Wymagania wstępne:
- Aplikacja uruchomiona

Dane testowe:
login: user, stare hasło: zlehaslo, nowe hasło: nowehaslo

Kroki testowe:
1. Zaloguj się
2. Przejdź do profilu
3. Wprowadź błędne stare hasło
4. Zmień hasło

Oczekiwany rezultat:
- Komunikat o błędnym starym haśle, brak zmiany

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_profile.py::test_change_password_validation[zlehaslo-nowehaslo-nowehaslo-Stare hasło jest nieprawidłowe]`

Uwagi:
Brak

### TC-034: Zmiana hasła – zbyt krótkie nowe hasło

Cel:
Weryfikacja walidacji długości nowego hasła.

Wymagania wstępne:
- Aplikacja uruchomiona

Dane testowe:
login: user, stare hasło: user123, nowe hasło: 123

Kroki testowe:
1. Zaloguj się
2. Przejdź do profilu
3. Wprowadź zbyt krótkie nowe hasło
4. Zmień hasło

Oczekiwany rezultat:
- Komunikat o zbyt krótkim haśle, brak zmiany

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_profile.py::test_change_password_validation[user123-123-123-min. 6 znaków]`

Uwagi:
Brak

### TC-035: Zmiana hasła – niezgodne nowe hasła

Cel:
Weryfikacja walidacji zgodności nowych haseł.

Wymagania wstępne:
- Aplikacja uruchomiona

Dane testowe:
login: user, stare hasło: user123, nowe hasło: nowehaslo, powtórz: innehaslo

Kroki testowe:
1. Zaloguj się
2. Przejdź do profilu
3. Wprowadź różne nowe hasła
4. Zmień hasło

Oczekiwany rezultat:
- Komunikat o niezgodności haseł, brak zmiany

Status: Do wykonania

Powiązany test automatyczny:
`tests/test_profile.py::test_change_password_validation[user123-nowehaslo-innehaslo-nie są zgodne]`

Uwagi:
Brak

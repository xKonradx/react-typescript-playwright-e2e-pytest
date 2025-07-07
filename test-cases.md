# Przypadki testowe – React Login Demo

## Spis treści

Wszystkie przypadki testowe zostały podzielone na kategorie:

- [Dostępność (Accessibility)](./tests/test-cases/accessibility.md)
- [Logowanie](./tests/test-cases/login.md)
- [Wydajność (Performance)](./tests/test-cases/performance.md)
- [Profil użytkownika](./tests/test-cases/profile.md)
- [Rejestracja](./tests/test-cases/register.md)
- [Bezpieczeństwo](./tests/test-cases/security.md)
- [Interfejs użytkownika (UI)](./tests/test-cases/ui.md)

---

## Szczegółowe pokrycie testowe

| Kategoria       | Liczba testów | Zakres                                                                                                                                                       |
|-----------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dostępność      | 13            | WCAG 2.1, screen reader, kontrast, nawigacja, tytuł, nagłówki, alt text, etykiety, klawiatura, skip links, powiększanie, fokus, język, komunikaty, walidacja |
| Logowanie       | 3             | Poprawne i błędne logowanie (admin/user)                                                                                                                     |
| Wydajność       | 14            | Ładowanie, logowanie, rejestracja, pamięć, DOM, sesje, API, requests, przewijanie, animacje, zasoby, responsywność, cache, TTI                               |
| Edycja profilu  | 5             | Zmiana hasła, walidacja danych                                                                                                                               |
| Rejestracja     | 5             | Sukces, walidacja loginu, hasła, zgodności                                                                                                                   |
| Bezpieczeństwo  | 11            | XSS, SQLi, CSRF, sesje, autoryzacja, timeout, rate limiting, ekspozycja danych, kontrola dostępu, wylogowanie                                                |
| Interfejs       | 11            | Ochrona tras, darkmode, modal, snapshoty, responsywność, 404, loading, walidacja UI                                                                          |

---

## Instrukcja

Aby przejrzeć przypadki testowe, wybierz odpowiednią kategorię z powyższej listy. Każdy przypadek zawiera:
- cel,
- wymagania wstępne,
- kroki testowe,
- dane testowe (jeśli dotyczy),
- oczekiwany rezultat,
- status,
- powiązanie z testem automatycznym,
- uwagi.

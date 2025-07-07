# React Login Demo – Frontend

## Opis

Ten katalog zawiera frontendową część aplikacji demonstracyjnej systemu logowania z autoryzacją ról, ochroną tras, trybem jasnym/ciemnym oraz integracją z automatycznymi testami E2E.

## Wymagania

- Node.js 18+
- npm 9+
- Przeglądarka: Chromium (zalecana do testów E2E)
- System operacyjny: Windows, macOS lub Linux

## Instalacja

1. Przejdź do katalogu frontend:
   ```bash
   cd frontend
   ```
2. Zainstaluj zależności:
   ```bash
   npm install
   ```

## Uruchamianie aplikacji

Aby uruchomić aplikację w trybie deweloperskim:
```bash
npm run dev
```
Aplikacja będzie dostępna pod adresem: [http://localhost:5173](http://localhost:5173)

## Budowanie aplikacji

Aby zbudować aplikację do wdrożenia produkcyjnego:
```bash
npm run build
```
Wynikowy kod znajdziesz w katalogu `dist/`.

## Struktura katalogów

```
frontend/
├── public/                # Pliki statyczne
├── src/
│   ├── assets/            # Zasoby (obrazy, ikony)
│   ├── components/        # Komponenty interfejsu użytkownika
│   ├── context/           # Kontekst autoryzacji
│   ├── data/              # Pliki z danymi testowymi
│   ├── routes/            # Routing aplikacji
│   ├── views/             # Widoki stron
│   ├── App.tsx            # Główny komponent aplikacji
│   └── main.tsx           # Punkt wejścia aplikacji
├── package.json           # Zależności i skrypty npm
├── postcss.config.cjs     # Konfiguracja PostCSS
├── tsconfig.json          # Konfiguracja TypeScript
└── vite.config.ts         # Konfiguracja Vite
```

## Główne biblioteki i narzędzia

- React – budowa interfejsu użytkownika
- TypeScript – statyczne typowanie
- Vite – szybki bundler i dev server
- React Router – routing aplikacji SPA
- Playwright (w testach E2E) – automatyzacja testów UI

## Funkcjonalności

- Rejestracja i logowanie użytkowników z walidacją
- System ról (administrator/użytkownik)
- Ochrona tras wymagających autoryzacji
- Edycja profilu użytkownika
- Tryb jasny/ciemny (przełącznik)
- Modal potwierdzenia wylogowania
- Responsywny interfejs

## Dodatkowe informacje

- Domyślni użytkownicy do testów znajdują się w pliku `src/data/users.json`.
- Aplikacja nie posiada backendu – wszystkie dane są przechowywane lokalnie (mock).
- Testy E2E oraz szczegółowa dokumentacja testów znajdują się w katalogu `../tests/playwright_env/`.

## Skrypty npm

| Komenda           | Opis                                      |
|-------------------|-------------------------------------------|
| `npm run dev`     | Uruchamia aplikację w trybie deweloperskim|
| `npm run build`   | Buduje aplikację do produkcji             |
| `npm run preview` | Podgląd zbudowanej aplikacji              |
| `npm run lint`    | Sprawdza kod pod kątem błędów ESLint      |

## Kontakt

W przypadku pytań lub problemów skontaktuj się z zespołem projektowym. 
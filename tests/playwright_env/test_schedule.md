# Harmonogram wykonania testów

## Przegląd

| Faza | Testy | Częstotliwość | Środowisko | Czas wykonania |
|------|-------|---------------|------------|----------------|
| Smoke | Krytyczne funkcje | Każdy commit | Dev | ~2 min |
| Regression | Wszystkie testy | Codziennie | Staging | ~15 min |
| Security | Testy bezpieczeństwa | Co tydzień | Staging | ~5 min |
| Performance | Testy wydajnościowe | Co tydzień | Staging | ~10 min |
| Accessibility | Testy dostępności | Co miesiąc | Staging | ~3 min |

## Szczegółowy harmonogram

### 1. Smoke Tests (Krytyczne funkcje)
Częstotliwość: Każdy commit do main branch
Środowisko: Development
Czas: ~2 minuty
Testy:
- `test_login_success[admin-admin123-admin]`
- `test_login_success[user-user123-user]`
- `test_protected_routes`
- `test_register_success[testuser1-testpass123]`

Komenda:
```bash
pytest tests/test_login.py::test_login_success tests/test_ui.py::test_protected_routes tests/test_register.py::test_register_success -v
```

### 2. Regression Tests (Wszystkie testy)
Częstotliwość: Codziennie o 02:00
Środowisko: Staging
Czas: ~15 minut
Testy: Wszystkie 16 testów + nowe testy

Komenda:
```bash
pytest -v --durations=10 --junitxml=test-results.xml
```

### 3. Security Tests (Testy bezpieczeństwa)
Częstotliwość: Co tydzień (niedziela 03:00)
Środowisko: Staging
Czas: ~5 minut
Testy:
- Wszystkie testy z `test_security.py`
- Dodatkowe testy penetracyjne

Komenda:
```bash
pytest tests/test_security.py -v --headed
```

### 4. Performance Tests (Testy wydajnościowe)
Częstotliwość: Co tydzień (sobota 04:00)
Środowisko: Staging
Czas: ~10 minut
Testy:
- Wszystkie testy z `test_performance.py`
- Load testing

Komenda:
```bash
pytest tests/test_performance.py -v --durations=0
```

### 5. Accessibility Tests (Testy dostępności)
Częstotliwość: Co miesiąc (pierwsza niedziela 05:00)
Środowisko: Staging
Czas: ~3 minuty
Testy:
- Wszystkie testy z `test_accessibility.py`
- WCAG 2.1 compliance

Komenda:
```bash
pytest tests/test_accessibility.py -v
```

## Konfiguracja CI/CD

### GitHub Actions Workflow

```yaml
name: Test Suite

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  smoke-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: |
          cd tests/playwright_env
          pip install -r requirements.txt
          python -m playwright install
      - name: Run smoke tests
        run: |
          cd tests/playwright_env
          pytest tests/test_login.py::test_login_success tests/test_ui.py::test_protected_routes -v

  regression-tests:
    runs-on: ubuntu-latest
    needs: smoke-tests
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: |
          cd tests/playwright_env
          pip install -r requirements.txt
          python -m playwright install
      - name: Run regression tests
        run: |
          cd tests/playwright_env
          pytest -v --junitxml=test-results.xml
      - name: Upload test results
        uses: actions/upload-artifact@v3
        with:
          name: test-results
          path: tests/playwright_env/test-results.xml
```

### Cron Jobs (Linux)

```bash
# Smoke tests - każdy commit
# (automatyczne przez CI/CD)

# Regression tests - codziennie o 02:00
0 2 * * * cd /path/to/react-login-demo/tests/playwright_env && pytest -v --junitxml=regression-results.xml

# Security tests - co tydzień o 03:00
0 3 * * 0 cd /path/to/react-login-demo/tests/playwright_env && pytest tests/test_security.py -v

# Performance tests - co tydzień o 04:00
0 4 * * 6 cd /path/to/react-login-demo/tests/playwright_env && pytest tests/test_performance.py -v

# Accessibility tests - co miesiąc o 05:00
0 5 1 * * cd /path/to/react-login-demo/tests/playwright_env && pytest tests/test_accessibility.py -v
```

## Raportowanie

### Metryki do śledzenia

| Metryka | Cel | Alert |
|---------|-----|-------|
| Pass Rate | > 95% | < 90% |
| Execution Time | < 15 min | > 20 min |
| Flaky Tests | < 2% | > 5% |
| Security Issues | 0 | > 0 |
| Performance Degradation | < 10% | > 20% |

### Automatyczne raporty

1. Daily Report - wysyłany codziennie o 08:00
2. Weekly Security Report - wysyłany w poniedziałek o 09:00
3. Monthly Accessibility Report - wysyłany pierwszego dnia miesiąca o 10:00

### Slack Notifications

```python
# Przykład integracji ze Slack
def send_slack_notification(message, channel="#test-results"):
    webhook_url = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
    payload = {
        "channel": channel,
        "text": message,
        "username": "Test Bot"
    }
    requests.post(webhook_url, json=payload)
```

## Escalation Matrix

| Poziom | Warunek | Akcja |
|--------|---------|-------|
| Level 1 | Smoke tests fail | Powiadomienie do developera |
| Level 2 | Regression tests fail | Powiadomienie do team lead |
| Level 3 | Security tests fail | Powiadomienie do security team |
| Level 4 | Performance degradation > 50% | Powiadomienie do DevOps |

## Maintenance

### Cotygodniowe zadania
- [ ] Przegląd wyników testów
- [ ] Aktualizacja testów (jeśli potrzeba)
- [ ] Optymalizacja czasu wykonania
- [ ] Backup danych testowych

### Miesięczne zadania
- [ ] Przegląd strategii testów
- [ ] Aktualizacja narzędzi testowych
- [ ] Szkolenie zespołu
- [ ] Przegląd metryk jakościowych

### Kwartalne zadania
- [ ] Przegląd pokrycia testowego
- [ ] Aktualizacja standardów testowania
- [ ] Przegląd automatyzacji
- [ ] Planowanie nowych testów 
import pytest
from playwright.sync_api import sync_playwright
import os
import tempfile
import requests
import time

# Dodaj import snapshot jeśli pytest-playwright-snapshot jest zainstalowany
try:
    from pytest_playwright_snapshot.plugin import snapshot
except ImportError:
    # Jeśli nie zainstalowano, podaj instrukcję
    # Aby korzystać z testów wizualnych, zainstaluj:
    # pip install pytest-playwright-snapshot
    pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def is_server_running(url, timeout=3):
    """Sprawdza czy serwer działa na podanym URL"""
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code == 200
    except:
        return False

def detect_environment():
    """Automatycznie wykrywa środowisko i zwraca odpowiedni BASE_URL"""
    # Sprawdź zmienną środowiskową
    env = os.getenv('TEST_ENV', '').lower()
    
    if env == 'production':
        return "http://localhost:4173"
    elif env == 'dev':
        return "http://localhost:5173"
    
    # Automatyczna detekcja - sprawdź który serwer działa
    print("🔍 Automatyczna detekcja środowiska...")
    
    # Sprawdź preview (produkcja) - port 4173
    if is_server_running("http://localhost:4173"):
        print("✅ Wykryto serwer produkcyjny na porcie 4173")
        return "http://localhost:4173"
    
    # Sprawdź dev server - port 5173
    if is_server_running("http://localhost:5173"):
        print("✅ Wykryto serwer deweloperski na porcie 5173")
        return "http://localhost:5173"
    
    # Jeśli żaden nie działa, domyślnie używaj 5173 (dev)
    print("⚠️  Nie wykryto działającego serwera. Używam domyślnego portu 5173 (dev)")
    print("💡 Uruchom aplikację: cd frontend && npm run dev")
    return "http://localhost:5173"

@pytest.fixture(scope="session")
def base_url():
    """Fixture zwracająca BASE_URL na podstawie wykrytego środowiska"""
    url = detect_environment()
    print(f"🌐 Używam BASE_URL: {url}")
    return url

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # Konfiguracja z trace viewer i codegen support
        browser = p.chromium.launch(
            headless=True,
            args=[
                '--disable-dev-shm-usage',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-gpu',
                '--disable-web-security',
                '--disable-features=VizDisplayCompositor'
            ]
        )
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser, request, base_url):
    # Konfiguracja z trace viewer, video i screenshot
    context = browser.new_context(
        record_video_dir=os.path.join(BASE_DIR, "videos"),
        record_video_size={"width": 1280, "height": 720},
        viewport={"width": 1280, "height": 720},
        locale="pl-PL",
        timezone_id="Europe/Warsaw"
    )
    
    # Włącz trace viewer
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    page = context.new_page()
    
    # Dodaj event listeners dla codegen
    page.on("pageerror", lambda err: print(f"Page error: {err}"))
    page.on("requestfailed", lambda request: print(f"Request failed: {request.url}"))
    
    yield page
    
    # Zatrzymaj trace i zapisz
    test_name = get_test_name(request.node)
    trace_path = os.path.join(BASE_DIR, "traces", f"trace-{test_name}.zip")
    os.makedirs(os.path.join(BASE_DIR, "traces"), exist_ok=True)
    context.tracing.stop(path=trace_path)
    
    context.close()

# Helper function dla nazwy testu
def get_test_name(item):
    """Zwraca nazwę testu z item"""
    return item.nodeid.replace('::', '_').replace('/', '_').replace('.py', '')

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Robi screenshot tylko przy nieudanym teście Playwright (jeśli używana jest fixture 'page').
    Dodatkowo zapisuje trace viewer i video.
    """
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            # Screenshot
            screenshots_dir = os.path.join(BASE_DIR, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            filename = f"{item.nodeid.replace('::', '__').replace('/', '_')}.png"
            path = os.path.join(screenshots_dir, filename)
            page.screenshot(path=path)
            print(f"\n[Screenshot saved to {path}]")
            
            # Video (jeśli dostępne)
            try:
                video_path = page.video.path() if page.video else None
                if video_path:
                    print(f"\n[Video saved to {video_path}]")
            except:
                pass

@pytest.fixture(autouse=True)
def setup_test_environment():
    """Setup dla środowiska testowego"""
    # Utwórz katalogi dla artifacts
    os.makedirs(os.path.join(BASE_DIR, "screenshots"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "videos"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "traces"), exist_ok=True)
    yield

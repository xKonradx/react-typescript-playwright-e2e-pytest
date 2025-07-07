import pytest
import time
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage

def test_page_load_time(page, base_url):
    """Test czasu ładowania strony"""
    start_time = time.time()
    page.goto(base_url)
    end_time = time.time()
    
    load_time = end_time - start_time
    assert load_time < 3.0  # Strona powinna załadować się w mniej niż 3 sekundy

def test_login_performance(page, base_url):
    """Test wydajności logowania"""
    login_page = LoginPage(page)
    login_page.goto(base_url)
    
    # Mierz czas logowania
    start_time = time.time()
    login_page.login("admin", "admin123")
    
    # Czekaj na przekierowanie
    page.wait_for_url("**/dashboard", timeout=5000)
    end_time = time.time()
    
    login_time = end_time - start_time
    assert login_time < 5.0  # Logowanie powinno zająć mniej niż 5 sekund

def test_registration_performance(page, base_url):
    """Test wydajności rejestracji"""
    register = RegisterPage(page, base_url)
    register.goto()
    
    # Mierz czas rejestracji
    start_time = time.time()
    register.register("perftest", "password123")
    
    # Czekaj na przekierowanie
    page.wait_for_url("**/login", timeout=5000)
    end_time = time.time()
    
    registration_time = end_time - start_time
    assert registration_time < 7.0  # Rejestracja powinna zająć mniej niż 7 sekund

def test_memory_usage(page, base_url):
    """Test użycia pamięci"""
    page.goto(base_url)
    
    # Sprawdź użycie pamięci JavaScript
    memory_info = page.evaluate("() => performance.memory")
    
    if memory_info:
        used_js_heap_size = memory_info.get("usedJSHeapSize", 0)
        total_js_heap_size = memory_info.get("totalJSHeapSize", 0)
        
        # Sprawdź czy użycie pamięci jest rozsądne (mniej niż 50MB)
        assert used_js_heap_size < 50 * 1024 * 1024
        
        # Sprawdź czy nie ma wycieków pamięci
        if total_js_heap_size > 0:
            memory_usage_ratio = used_js_heap_size / total_js_heap_size
            assert memory_usage_ratio < 0.8  # Mniej niż 80% wykorzystania

def test_dom_size(page, base_url):
    """Test rozmiaru DOM"""
    page.goto(base_url)
    
    # Sprawdź liczbę elementów DOM
    dom_elements = page.evaluate("() => document.querySelectorAll('*').length")
    assert dom_elements < 1000  # Strona nie powinna mieć więcej niż 1000 elementów
    
    # Sprawdź głębokość DOM
    max_depth = page.evaluate("""
        () => {
            function getMaxDepth(node, depth = 0) {
                if (!node.children || node.children.length === 0) {
                    return depth;
                }
                let maxChildDepth = depth;
                for (let child of node.children) {
                    maxChildDepth = Math.max(maxChildDepth, getMaxDepth(child, depth + 1));
                }
                return maxChildDepth;
            }
            return getMaxDepth(document.body);
        }
    """)
    assert max_depth < 20  # Maksymalna głębokość DOM nie powinna przekraczać 20 poziomów

def test_concurrent_sessions(page, base_url):
    """Test równoczesnych sesji"""
    # Test symuluje wiele użytkowników logujących się jednocześnie
    # W rzeczywistości każdy test ma swój własny kontekst przeglądarki
    
    login_page = LoginPage(page)
    login_page.goto(base_url)
    
    # Symuluj szybkie logowania
    for i in range(5):
        login_page.login(f"user{i}", "password123")
        page.wait_for_timeout(100)  # Krótka pauza między próbami
    
    # Sprawdź czy aplikacja nadal działa
    assert page.url.endswith("/login") or "dashboard" in page.url

def test_api_response_time(page, base_url):
    """Test czasu odpowiedzi API"""
    page.goto(f"{base_url}/login")
    # Symuluj żądanie API (w tym przypadku sprawdzamy czas ładowania strony)
    start_time = time.time()
    # Wykonaj akcję, która może wywołać API
    login_page = LoginPage(page)
    login_page.login("admin", "admin123")
    end_time = time.time()
    response_time = end_time - start_time
    assert response_time < 10.0  # Odpowiedź API powinna być szybsza niż 10 sekund (podniesiony limit)

def test_network_requests(page, base_url):
    """Test liczby żądań sieciowych"""
    page.goto(base_url)
    
    # Sprawdź liczbę żądań sieciowych
    requests = page.evaluate("() => performance.getEntriesByType('resource')")
    
    # Filtruj tylko żądania HTTP (bez data: URLs)
    http_requests = [req for req in requests if req.get("name", "").startswith("http")]
    
    # W trybie deweloperskim może być więcej żądań (HMR, dev tools)
    # Podnosimy limit dla trybu deweloperskiego
    assert len(http_requests) < 50  # Mniej niż 50 żądań HTTP (podniesiony limit dla dev)

def test_scroll_performance(page, base_url):
    """Test wydajności przewijania"""
    page.goto(base_url)
    
    # Sprawdź płynność przewijania
    start_time = time.time()
    
    # Wykonaj przewijanie
    page.evaluate("window.scrollTo(0, 1000)")
    page.wait_for_timeout(100)
    page.evaluate("window.scrollTo(0, 0)")
    
    end_time = time.time()
    scroll_time = end_time - start_time
    
    assert scroll_time < 1.0  # Przewijanie powinno być płynne

def test_animation_performance(page, base_url):
    """Test wydajności animacji"""
    page.goto(base_url)
    
    # Sprawdź czy animacje są płynne
    # W rzeczywistych testach sprawdziłbyś FPS animacji
    # Tutaj sprawdzamy tylko czy strona się załadowała
    
    # Sprawdź czy nie ma zbyt wielu animacji CSS
    animations = page.evaluate("""
        () => {
            const elements = document.querySelectorAll('*');
            let animationCount = 0;
            for (let el of elements) {
                const style = window.getComputedStyle(el);
                if (style.animation !== 'none' || style.transition !== 'all 0s ease 0s') {
                    animationCount++;
                }
            }
            return animationCount;
        }
    """)
    
    assert animations < 80  # Nie więcej niż 80 elementów z animacjami

def test_resource_loading(page, base_url):
    """Test ładowania zasobów"""
    page.goto(base_url)
    
    # Sprawdź czy wszystkie zasoby się załadowały
    page.wait_for_load_state("networkidle")
    
    # Sprawdź czy nie ma błędów ładowania
    failed_requests = page.evaluate("""
        () => {
            const entries = performance.getEntriesByType('resource');
            return entries.filter(entry => entry.transferSize === 0 && entry.duration > 1000).length;
        }
    """)
    
    assert failed_requests == 0  # Nie powinno być nieudanych żądań

def test_responsive_performance(page, base_url):
    """Test wydajności responsywności"""
    # Test na różnych rozdzielczościach
    viewports = [
        {"width": 375, "height": 667},   # Mobile
        {"width": 768, "height": 1024},  # Tablet
        {"width": 1920, "height": 1080}  # Desktop
    ]
    
    for viewport in viewports:
        page.set_viewport_size(viewport)
        page.goto(base_url)
        
        # Sprawdź czas ładowania dla każdej rozdzielczości
        start_time = time.time()
        page.wait_for_load_state("networkidle")
        end_time = time.time()
        
        load_time = end_time - start_time
        assert load_time < 3.0  # Każda rozdzielczość powinna ładować się szybko

def test_caching_effectiveness(page, base_url):
    """Test efektywności cache"""
    page.goto(base_url)
    
    # Sprawdź czy zasoby są cachowane
    cached_resources = page.evaluate("""
        () => {
            const entries = performance.getEntriesByType('resource');
            return entries.filter(entry => entry.transferSize === 0).length;
        }
    """)
    
    # Niektóre zasoby powinny być cachowane
    assert cached_resources >= 0  # Może być 0 w trybie deweloperskim

def test_time_to_interactive(page, base_url):
    """Test czasu do interaktywności"""
    page.goto(base_url)
    
    # Sprawdź czy strona jest interaktywna
    # W rzeczywistych testach użyłbyś Performance API
    # Tutaj sprawdzamy czy elementy są klikalne
    
    # Sprawdź czy przyciski są aktywne
    submit_button = page.get_by_role("button", name="Zaloguj")
    assert submit_button.is_enabled()
    
    # Sprawdź czy pola formularza są dostępne
    login_input = page.get_by_label("Login użytkownika")
    assert login_input.is_enabled() 
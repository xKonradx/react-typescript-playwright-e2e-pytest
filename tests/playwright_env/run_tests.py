#!/usr/bin/env python3
"""
Skrypt do uruchamiania testów Playwright z różnymi opcjami konfiguracji
"""

import subprocess
import sys
import os
import argparse
from pathlib import Path

def run_command(command, description):
    """Uruchamia komendę i wyświetla wynik"""
    print(f"\n{'='*50}")
    print(f"🚀 {description}")
    print(f"{'='*50}")
    print(f"Komenda: {' '.join(command)}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(command, check=True, capture_output=False)
        print(f"✅ {description} - Zakończone pomyślnie")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Błąd: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Uruchamianie testów Playwright")
    parser.add_argument("--mode", choices=["parallel", "sequential", "headed", "debug"], 
                       default="parallel", help="Tryb uruchamiania testów")
    parser.add_argument("--browser", choices=["chromium", "firefox", "webkit"], 
                       default="chromium", help="Przeglądarka do testów")
    parser.add_argument("--tests", help="Konkretny plik testowy lub pattern")
    parser.add_argument("--workers", type=int, default=4, help="Liczba workerów dla parallel execution")
    parser.add_argument("--trace", action="store_true", help="Włącz trace viewer")
    parser.add_argument("--video", action="store_true", help="Włącz nagrywanie video")
    parser.add_argument("--screenshot", action="store_true", help="Włącz screenshots")
    
    args = parser.parse_args()
    
    # Zmień katalog na playwright_env
    os.chdir(Path(__file__).parent)
    
    # Podstawowa komenda pytest
    cmd = ["python", "-m", "pytest"]
    
    # Dodaj opcje w zależności od trybu
    if args.mode == "parallel":
        cmd.extend(["-n", str(args.workers), "--dist=loadfile"])
        print(f"🔧 Tryb: Parallel execution z {args.workers} workerami")
    elif args.mode == "sequential":
        print("🔧 Tryb: Sequential execution")
    elif args.mode == "headed":
        cmd.extend(["--headed"])
        print("🔧 Tryb: Headed browser")
    elif args.mode == "debug":
        cmd.extend(["--headed", "--slowmo", "1000", "-s"])
        print("🔧 Tryb: Debug z powolnym wykonaniem")
    
    # Dodaj opcje przeglądarki
    cmd.extend(["--browser", args.browser])
    
    # Dodaj opcje trace/video/screenshot
    if args.trace:
        cmd.extend(["--tracing=on"])
        print("📹 Trace viewer: Włączony")
    if args.video:
        cmd.extend(["--video=on"])
        print("🎥 Video recording: Włączony")
    if args.screenshot:
        cmd.extend(["--screenshot=on"])
        print("📸 Screenshots: Włączone")
    
    # Dodaj konkretne testy jeśli podano
    if args.tests:
        cmd.append(args.tests)
        print(f"🎯 Testy: {args.tests}")
    else:
        cmd.append("tests/")
        print("🎯 Testy: Wszystkie")
    
    # Dodaj opcje raportowania
    cmd.extend([
        "--html=reports/report.html",
        "--self-contained-html",
        "--metadata", "Browser", args.browser,
        "--metadata", "Mode", args.mode,
        "--metadata", "Workers", str(args.workers)
    ])
    
    # Utwórz katalogi
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("videos", exist_ok=True)
    os.makedirs("traces", exist_ok=True)
    
    # Uruchom testy
    success = run_command(cmd, "Uruchamianie testów Playwright")
    
    if success:
        print(f"\n🎉 Testy zakończone pomyślnie!")
        print(f"📊 Raport HTML: reports/report.html")
        print(f"📸 Screenshots: screenshots/")
        print(f"🎥 Videos: videos/")
        print(f"📹 Traces: traces/")
        
        # Otwórz raport jeśli dostępny
        report_path = Path("reports/report.html")
        if report_path.exists():
            print(f"🌐 Otwieranie raportu...")
            try:
                import webbrowser
                webbrowser.open(f"file://{report_path.absolute()}")
            except:
                print(f"📄 Raport dostępny w: {report_path.absolute()}")
    else:
        print(f"\n💥 Testy zakończone z błędami!")
        sys.exit(1)

if __name__ == "__main__":
    main() 
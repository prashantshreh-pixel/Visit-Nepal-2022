"""
run_all.py — Visit Nepal 2022 Launcher
=======================================
Starts both the Django web server and the Rasa NLP chatbot server
from the repository root. Run with:

    python run_all.py

Press Ctrl+C to gracefully stop both servers.
"""

import os
import sys
import subprocess
import time

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT  = os.path.dirname(os.path.abspath(__file__))
DJANGO_DIR = os.path.join(REPO_ROOT, "django_app")
RASA_DIR   = os.path.join(REPO_ROOT, "rasa_bot")

print("=" * 65)
print(" 🏔️  Visit Nepal 2022 — Application Launcher")
print("=" * 65)

processes = []

try:
    # ------------------------------------------------------------------
    # 1. Start Rasa NLP Chatbot Server
    # ------------------------------------------------------------------
    if os.path.exists(RASA_DIR):
        print("\n🤖  Launching Rasa Chatbot Server...")
        rasa_proc = subprocess.Popen(
            ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*"],
            cwd=RASA_DIR,
            shell=True,
        )
        processes.append(("Rasa Chatbot", rasa_proc))
        print("    ✅  Rasa process started  →  http://localhost:5005")
    else:
        print("⚠️  rasa_bot/ directory not found — skipping Rasa launch.")

    # Give Rasa a moment to initialize before Django starts
    time.sleep(2)

    # ------------------------------------------------------------------
    # 2. Start Django Web Server
    # ------------------------------------------------------------------
    print("\n🌐  Launching Django Web Server...")
    django_proc = subprocess.Popen(
        [sys.executable, "manage.py", "runserver"],
        cwd=DJANGO_DIR,
        shell=True,
    )
    processes.append(("Django Web Server", django_proc))
    print("    ✅  Django started            →  http://127.0.0.1:8000")

    print("\n" + "=" * 65)
    print("  Both servers are running. Press Ctrl+C to stop them.")
    print("=" * 65 + "\n")

    # Keep alive — report if either process dies unexpectedly
    while True:
        time.sleep(2)
        for name, proc in processes:
            if proc.poll() is not None:
                print(f"\n⚠️  {name} terminated (exit code {proc.returncode}).")

except KeyboardInterrupt:
    print("\n\n🛑  Shutting down servers...")
    for name, proc in processes:
        print(f"    Stopping {name}...")
        try:
            proc.terminate()
            proc.wait(timeout=5)
        except Exception:
            proc.kill()
    print("👋  All processes stopped cleanly.\n")

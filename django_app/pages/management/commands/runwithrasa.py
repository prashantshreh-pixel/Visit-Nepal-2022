import os
import sys
import subprocess
import time
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Launches both Rasa Chatbot Engine and Django Dev Server simultaneously"

    def handle(self, *args, **options):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        rasa_dir = os.path.join(base_dir, "Chatbot_rasa")

        self.stdout.write(self.style.SUCCESS("=" * 60))
        self.stdout.write(self.style.SUCCESS("🚀 Starting Visit Nepal 2022 (Django + Rasa)..."))
        self.stdout.write(self.style.SUCCESS("=" * 60))

        processes = []

        try:
            if os.path.exists(rasa_dir):
                self.stdout.write(self.style.MIGRATE_HEADING("🤖 Starting Rasa Chatbot server..."))
                rasa_proc = subprocess.Popen(
                    ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*"],
                    cwd=rasa_dir,
                    shell=True
                )
                processes.append(("Rasa", rasa_proc))
                time.sleep(2)

            self.stdout.write(self.style.MIGRATE_HEADING("🌐 Starting Django development server..."))
            django_proc = subprocess.Popen(
                [sys.executable, "manage.py", "runserver"],
                cwd=base_dir,
                shell=True
            )
            processes.append(("Django", django_proc))

            while True:
                time.sleep(1)

        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("\nStopping Rasa and Django servers..."))
            for name, proc in processes:
                try:
                    proc.terminate()
                except Exception:
                    proc.kill()
            self.stdout.write(self.style.SUCCESS("Clean exit."))

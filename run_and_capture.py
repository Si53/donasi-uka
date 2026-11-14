import subprocess
import time
import socket
import sys
import os

def main():
    print("Starting Django server on 127.0.0.1:8000...")
    server_proc = subprocess.Popen([sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000', '--noreload'])

    ready = False
    for _ in range(30):
        try:
            with socket.create_connection(('127.0.0.1', 8000), timeout=0.5):
                ready = True
                break
        except Exception:
            time.sleep(0.5)

    if not ready:
        server_proc.kill()
        print("Error: Django server failed to start within 15 seconds")
        sys.exit(1)

    print("Django server ready! Running screenshot automation...")
    script = sys.argv[1] if len(sys.argv) > 1 else 'take_screenshots'
    try:
        import importlib
        mod = importlib.import_module(script.replace('.py', ''))
        mod.main()
    finally:
        print("Stopping Django server...")
        server_proc.terminate()
        try:
            server_proc.wait(timeout=3)
        except Exception:
            server_proc.kill()
        print("Django server stopped.")

if __name__ == '__main__':
    main()


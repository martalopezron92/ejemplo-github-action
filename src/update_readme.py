import subprocess
from datetime import datetime

def run_tests():
    try:
        subprocess.check_call(["pytest", "-q"])
        return "✅ Tests correctos"
    except subprocess.CalledProcessError:
        return "❌ Tests fallidos"

def update_readme(status: str):
    with open("README.md", "a") as f:
        ahora = datetime.now()
        f.write(str(ahora) + ": " + status + "\n")
    
if __name__ == "__main__":
    status = run_tests()
    update_readme(status)

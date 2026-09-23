
import os
import subprocess
from datetime import datetime

def run_scan(command, output_name):

  timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"results/{output_name}_{timestamp}.txt"

    print(f"\n[+] Exécution : {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    with open(output_file, "w") as f:
        f.write(result.stdout)

    print(f"[+] Résultats sauvegardés dans {output_file}\n")


import os
import subprocess
from datetime import datetime

def run_scan(command, output_name):

  #Générer un timestamp
  #.strftime formate la date dans un format lisible
  timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  
  #Construire le nom du fichier
  #on veut que chaque fichier ait le le nom du scanune date unique
    output_file = f"results/{output_name}_{timestamp}.txt"

  #Afficher la commande exécutée, la commande Nmap qui va être lancée
    print(f"\n[+] Exécution : {command}")


    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    with open(output_file, "w") as f:
        f.write(result.stdout)

    print(f"[+] Résultats sauvegardés dans {output_file}\n")

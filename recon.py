
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


def menu():
    print("""NMAP RECON TOOLKIT
1. Scan découverte d'hôte (-sn)
2. Scan SYN (-sS)
3. Scan TCP Connect (-sT)
4. Scan UDP (-sU)
5. Scan FIN (-sF)
6. Scan furtif (-sn -T0)
7. Scripts SMB (users, groups, shares)
8. Scan -sC (scripts par défaut)
0. Quitter
""")

choice = input("Choix : ")
    target = input("Cible (IP ou réseau) : ")

    if choice == "1":
        run_scan(f"nmap -sn {target}", "host_discovery")

    elif choice == "2":
        run_scan(f"nmap -sS {target}", "syn_scan")

    elif choice == "3":
        run_scan(f"nmap -sT {target}", "tcp_connect")

    elif choice == "4":
        run_scan(f"nmap -sU {target}", "udp_scan")

    elif choice == "5":
        run_scan(f"nmap -sF {target}", "fin_scan")

    elif choice == "6":
        run_scan(f"nmap -sn -T0 {target}", "stealth_scan")

    elif choice == "7":
        run_scan(f"nmap --script smb-enum-users,smb-enum-groups,smb-enum-shares -p445 {target}", "smb_enum")

    elif choice == "8":
        run_scan(f"nmap -sC {target}", "default_scripts")

    elif choice == "0":
        exit()

    else:
        print("Choix invalide.")

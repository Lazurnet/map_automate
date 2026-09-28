# map automate (Septembre 2026)

J'ai fait cet outil Python qui permet d’automatiser les scans Nmap étudiés dans le module **3.2 – Reconnaissance active** du cours NetAcad *Hacker Éthique*.  
Ce projet m'a permis de comprendre comment lancer différents types de scans, sauvegarder automatiquement les résultats dans des fichiers générés.
![Made with Python](https://img.shields.io/badge/Made%20with-Python-yellow)

##  Objectif

- Automatiser les scans Nmap courants  
- Générer des fichiers horodatés dans un dossier `results/`  

## Installation

Dans votre machine Linux (VM Kali ou LabVM) :

```
sudo apt update
sudo apt install nmap -y
```

Cloner le projet :

```
git clone https://github.com/user_name/project_name
cd nmap-recon-toolkit
```

## Utilisation

Lancer le script :

```
python3 recon.py
```

Choisir un scan, entrer une IP ou un réseau, et le script génère automatiquement un fichier dans results/  
Lecture du fichier :  ```cat host_discovery_2026-09-27_13-28-25.txt```

![lancer le script et choisir des scans](demo.png "scan").


## Astuces

Lister les fichiers par ordre chronologique : ```ls -t```  
Afficher automatiquement le dernier fichier :```cat $(ls -t | head -n 1)```


## Notes
Ce projet accompagne mon apprentissage du module 3.2 du cours NetAcad :  
- Analyse de ports  
- Découverte d’hôtes  
- Options de timing  
- Scripts NSE  
- Énumération SMB  
- Automatisation de la reconnaissance active

# Sources
https://nmap.org/book/man-target-specification.html

outil Python qui automatise les scans Nmap étudiés dans le module 3.2 du cours NetAcad “Hacker Éthique”.


https://nmap.org/book/man-target-specification.html

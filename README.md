# Projet de Craqueur de Mot de Passe

Ce projet est un craqueur de mot de passe simple écrit en Python. Il utilise une liste de mots de passe (wordlist) pour tenter de trouver un mot de passe cible fourni par l'utilisateur. Le programme parcourt toutes les wordlists présentes dans le dossier `src/wordlist` et essaie de trouver une correspondance avec le mot de passe cible.

## Structure du Projet

```
password-cracker
├── src
│   ├── main.py          # Point d'entrée de l'application
│   ├── cracker.py       # Contient la classe PasswordCracker
│   └── wordlist         # Dossier contenant les listes de mots de passe
├── requirements.txt      # Dépendances nécessaires
└── README.md            # Documentation du projet
```

## Installation

1. Clonez le dépôt :
   ```
   git clone <URL_DU_DEPOT>
   cd password-cracker
   ```

2. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

## Utilisation

1. Ajoutez vos fichiers de wordlist dans le dossier `src/wordlist`. Chaque fichier doit contenir des mots de passe potentiels, un par ligne.

2. Exécutez le programme :
   ```
   python src/main.py
   ```

3. Suivez les instructions à l'écran pour entrer le mot de passe à craquer.

## Fonctionnalités

- Prend en charge plusieurs wordlists dans un dossier spécifique.
- Mesure le temps nécessaire pour trouver le mot de passe.
- Facile à utiliser et à modifier pour des besoins spécifiques.

## Avertissement

Ce projet est destiné à des fins éducatives uniquement. Veuillez ne pas l'utiliser à des fins malveillantes.

---

# Password Cracker Project

This project is a simple password cracker written in Python. It uses a list of passwords (wordlist) to try to find a target password provided by the user. The program goes through all the wordlists present in the `src/wordlist` folder and tries to find a match with the target password.

## Project Structure

```
password-cracker
├── src
│   ├── main.py          # Application entry point
│   ├── cracker.py       # Contains the PasswordCracker class
│   └── wordlist         # Folder containing password lists
├── requirements.txt      # Necessary dependencies
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <REPOSITORY_URL>
   cd password-cracker
   ```

2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Add your wordlist files to the `src/wordlist` folder. Each file should contain potential passwords, one per line.

2. Run the program:
   ```
   python src/main.py
   ```

3. Follow the on-screen instructions to enter the password to crack.

## Features

- Supports multiple wordlists in a specific folder.
- Measures the time taken to find the password.
- Easy to use and modify for specific needs.

## Disclaimer

This project is intended for educational purposes only. Please do not use it for malicious purposes.
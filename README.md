# Projet de Craqueur de Mot de Passe

Ce projet est un craqueur de mot de passe simple écrit en Python. Il utilise une liste de mots de passe (wordlist) pour tenter de trouver un mot de passe cible fourni par l'utilisateur.

## Structure du Projet

```
password-cracker
├── src
│   ├── main.py          # Point d'entrée de l'application
│   ├── cracker.py       # Contient la classe PasswordCracker
│   └── wordlist.txt     # Liste de mots de passe potentiels
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

1. Ouvrez le fichier `src/wordlist.txt` et ajoutez vos mots de passe potentiels, un par ligne.

2. Exécutez le programme :
   ```
   python src/main.py
   ```

3. Suivez les instructions à l'écran pour entrer le mot de passe à craquer.

## Fonctionnalités

- Prend en charge une wordlist personnalisée.
- Mesure le temps nécessaire pour trouver le mot de passe.
- Facile à utiliser et à modifier pour des besoins spécifiques.

## Avertissement

Ce projet est destiné à des fins éducatives uniquement. Veuillez ne pas l'utiliser à des fins malveillantes.
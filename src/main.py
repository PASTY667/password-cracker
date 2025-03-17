from time import time
from cracker import PasswordCracker

def main():
    target_password = input("Entrez le mot de passe à craquer : ")
    with open('wordlist.txt', 'r') as file:
        wordlist = [line.strip() for line in file.readlines()]

    cracker = PasswordCracker(wordlist)
    start_time = time()
    found_password = cracker.crack_password(target_password)
    end_time = time()

    if found_password:
        print(f"Mot de passe trouvé : {found_password}")
        print(f"Temps pris pour le trouver : {end_time - start_time:.2f} secondes")
    else:
        print("Mot de passe non trouvé dans la wordlist.")

if __name__ == "__main__":
    main()
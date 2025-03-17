class PasswordCracker:
    def __init__(self, wordlist):
        self.wordlist = wordlist

    def crack_password(self, target_password):
        import time
        
        start_time = time.time()
        with open(self.wordlist, 'r') as file:
            for line in file:
                password = line.strip()
                if password == target_password:
                    end_time = time.time()
                    return f"Mot de passe trouvé : {password} en {end_time - start_time:.2f} secondes"
        end_time = time.time()
        return f"Mot de passe non trouvé en {end_time - start_time:.2f} secondes"
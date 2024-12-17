import random, string, traceback

# Passwort-Generator-Funktion
def password_generator(settings, pwgen, variables):
    try:
        if settings.language=="de":
            print(f"\n=== Passwort Generator ===")
        else:
            print("\n=== Password Generator ===")
        
        if settings.language=="de":
            print(f"!!!INFO!!! Dieses feature ist eventuell noch nicht ganz reif für nutzung!\nFehler bitte in den GitHub oder die Email-Adresse:\n{variables.mail}\n{variables.beta_site}")
        
        # Eingabe der Passwortlänge
        while True:
            try:
                if settings.language=="de":
                    length= int(input("Gebe die Länge an (minimum 8): "))
                else:
                    length = int(input("Enter password length (minimum 8): "))
                if length < 8:
                    if settings.language=="de":
                        print("Passwortlänge muss 8 lang sein.")
                    else:
                        print("Password length must be at least 8.")
                else:
                    break
            except ValueError:
                if settings.language=="de":
                    print("Bitte gib eine nummer.")
                else:
                    print("Please enter a valid number.")
        if pwgen.autopwgen==False:
            # Ausgeschlossene Sonderzeichen abfragen
            if settings.language=="de":
                excluded_chars = input("Schreib die Charactere die ausgelassen weerden sollen (e.g., '@#$'): ")
                
                # Komplexität vorschlagen
                include_uppercase = input("Großbuchstaben mit im passwort? (yes/no): ").lower() == "yes"
                include_numbers = input("NUmmern im Passwort? (yes/no): ").lower() == "yes"
                include_specials = input("Spezielle Buchstaben? (yes/no): ").lower() == "yes"
            else:
                excluded_chars = input("Enter characters to exclude (e.g., '@#$'): ")

                # Komplexität vorschlagen
                include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
                include_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
                include_specials = input("Include special characters? (yes/no): ").lower() == "yes"
        
        else:
            excluded_chars=pwgen.excluded_chars
            include_uppercase=pwgen.include_uppercase
            include_numbers=pwgen.include_numbers
            include_specials=pwgen.include_specials
        
        # Zeichensatz basierend auf den Optionen erstellen
        char_pool = string.ascii_lowercase
        if include_uppercase:
            char_pool += string.ascii_uppercase
        if include_numbers:
            char_pool += string.digits
        if include_specials:
            char_pool += string.punctuation
        
        # Ausgeschlossene Zeichen entfernen
        char_pool = ''.join([c for c in char_pool if c not in excluded_chars])
        
        if not char_pool:
            if settings.language=="de":
                print("Keine validen buchstaben und Nummern un Spezialbuchstaben übrig zum generieren. Bitte änder die Einstellungen.")
                return
            else:
                print("No valid characters left to generate a password. Please adjust your settings.")
                return
        
        # Passwort generieren
        password = ''.join(random.choices(char_pool, k=length))
        if settings.language=="de":
            print(f"Generiertes Passwort: {password}\n")
        else:
            print(f"Generated password: {password}\n")
        e=""
        return e, password
    except Exception as e:
        print(f"An error occurred in the password generator: {str(e)}")
        password=""
        return e, password

if __name__=="__main__":
    print("That module is not supposed to be run alone. Import it in your other code.")


import random
import string

def generiere_passwort(länge):
    # Definiere die möglichen Zeichen (Großbuchstaben, Kleinbuchstaben und Ziffern)
    zeichen = string.ascii_lowercase + string.ascii_uppercase + string.digits
    
    # Erzeuge das Passwort, indem zufällig Zeichen aus der Zeichenmenge ausgewählt werden
    passwort = ''.join(random.choice(zeichen) for _ in range(länge))
    
    return passwort

# Beispielaufruf:
print(generiere_passwort(12))  # Ausgabe: z.B. "aX4kG7jD2w8Q"
print(generiere_passwort(8))   # Ausgabe: z.B. "B7r4h2mQ"

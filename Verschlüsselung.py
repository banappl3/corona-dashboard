def caesar_verschlüsseln(text, n):
    """Verschlüsselt einen Text mit der Caesar-Verschlüsselung um n Positionen."""
    verschlüsselter_text = ""
    
    for char in text:
        if char.isalpha():
            # Bestimme den ASCII-Wert des Zeichens und verschiebe ihn
            start = ord('A') if char.isupper() else ord('a')
            verschlüsselter_text += chr((ord(char) - start + n) % 26 + start)
        else:
            # Nicht-Buchstaben bleiben unverändert
            verschlüsselter_text += char
    
    return verschlüsselter_text

def caesar_entschlüsseln(text, n):
    """Entschlüsselt einen mit der Caesar-Verschlüsselung verschlüsselten Text um n Positionen."""
    return caesar_verschlüsseln(text, -n)

# Beispielaufrufe:
original_text = "Hallo Welt!"
verschlüsselt = caesar_verschlüsseln(original_text, 3)
entschlüsselt = caesar_entschlüsseln(verschlüsselt, 3)

print(f"Original: {original_text}")
print(f"Verschlüsselt: {verschlüsselt}")
print(f"Entschlüsselt: {entschlüsselt}")


def vigenere_verschluesseln(plain_text, key):
    """Verschlüsselt den Klartext mit dem Vigenère-Verfahren."""
    result = []
    key = key.upper()
    plain_text = plain_text.upper()

    key_index = 0
    for char in plain_text:
        if char.isalpha():  # Nur Buchstaben verschlüsseln
            shift = ord(key[key_index]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(encrypted_char)
            
            # Schlüsselindex wird nur bei Buchstaben erhöht
            key_index = (key_index + 1) % len(key)
        else:
            result.append(char)  # Nicht-Buchstaben bleiben unverändert

    return ''.join(result)

def vigenere_entschluesseln(cipher_text, key):
    """Entschlüsselt den verschlüsselten Text mit dem Vigenère-Verfahren."""
    result = []
    key = key.upper()
    cipher_text = cipher_text.upper()

    key_index = 0
    for char in cipher_text:
        if char.isalpha():  # Nur Buchstaben entschlüsseln
            shift = ord(key[key_index]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result.append(decrypted_char)
            
            # Schlüsselindex wird nur bei Buchstaben erhöht
            key_index = (key_index + 1) % len(key)
        else:
            result.append(char)  # Nicht-Buchstaben bleiben unverändert

    return ''.join(result)

# Beispielaufruf:
plain_text = "Hallo Welt"
key = "KEY"

encrypted_text = vigenere_verschluesseln(plain_text, key)
print(f"Verschlüsselter Text: {encrypted_text}")

decrypted_text = vigenere_entschluesseln(encrypted_text, key)
print(f"Entschlüsselter Text: {decrypted_text}")



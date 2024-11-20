def binär_zu_dezimal(binär):
    # Überprüfen, ob die Eingabe ein gültiger Binärstring ist
    if not all(c in '01' for c in binär):
        return "Ungültige Binärzahl"

    # Umwandlung der Binärzahl in eine Dezimalzahl
    dezimal = 0
    for i, bit in enumerate(reversed(binär)):  # Wir gehen von rechts nach links
        if bit == '1':
            dezimal += 2 ** i

    return str(dezimal)

# Beispielaufrufe:
print(binär_zu_dezimal("1011"))  # Ausgabe: "11"
print(binär_zu_dezimal("1101"))  # Ausgabe: "13"
print(binär_zu_dezimal("11111111"))  # Ausgabe: "255"
print(binär_zu_dezimal("100"))  # Ausgabe: "4"

def dezimal_zu_binaer(n):
    # Basisfall: Wenn die Zahl 0 ist, geben wir "0" zurück
    if n == 0:
        return "0"
    # Rekursiver Fall: Wenn n größer als 0 ist
    else:
        return dezimal_zu_binaer(n // 2) + str(n % 2)

# Beispielaufruf:
print(dezimal_zu_binaer(10))  # Ausgabe: "1010" (Binär von 10)
print(dezimal_zu_binaer(255)) # Ausgabe: "11111111" (Binär von 255)


def hex_to_bin(hex_str):
    # Wandelt die Hexadezimalzahl in eine Binärzahl um und entfernt das '0b' Präfix
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)

# Beispiel:
hex_str = "00ff00"
bin_str = hex_to_bin(hex_str)
print(f"Hexadezimal: {hex_str} → Binär: {bin_str}")

def bin_to_hex(bin_str):
    # Wandelt die Binärzahl in eine Hexadezimalzahl um und entfernt das '0x' Präfix
    return hex(int(bin_str, 2))[2:].upper()

# Beispiel:
bin_str = "110110101"
hex_str = bin_to_hex(bin_str)
print(f"Binär: {bin_str} → Hexadezimal: {hex_str}")

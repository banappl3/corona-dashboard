def power(x, n):
    # Basisfall: x^0 ist immer 1
    if n == 0:
        return 1
    # Rekursiver Fall: x^n = x * x^(n-1)
    else:
        return x * power(x, n - 1)
    
def power_iterative(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    
    if exponent < 0:
        result = 1 / result
    
    return result
print(power_iterative(3,2))


def fakultaet_iterativ(n):
    # Startwert für das Produkt ist 1
    ergebnis = 1
    
    # Multipliziere alle Zahlen von 1 bis n
    for i in range(1, n + 1):
        ergebnis *= i
    
    return ergebnis

# Beispielaufruf:
print(fakultaet_iterativ(5))  # Ausgabe: 120 (5! = 5 * 4 * 3 * 2 * 1)
print(fakultaet_iterativ(0))  # Ausgabe: 1 (0! = 1)

def summe_der_ziffern(n):
    # Wenn die Zahl negativ ist, machen wir sie positiv (optional)
    n = abs(n)
    
    # Variable für die Summe der Ziffern
    summe = 0
    
    # Solange die Zahl größer als 0 ist
    while n > 0:
        # Füge die letzte Ziffer zur Summe hinzu
        summe += n % 10
        # Entferne die letzte Ziffer
        n //= 10
    
    return summe

# Beispielaufruf:
print(summe_der_ziffern(123))  # Ausgabe: 6 (1 + 2 + 3)
print(summe_der_ziffern(98765))  # Ausgabe: 35 (9 + 8 + 7 + 6 + 5)
print(summe_der_ziffern(-456))  # Ausgabe: 15 (4 + 5 + 6)


def finde_primzahlen(n):
    # Liste aller Zahlen von 0 bis n, initial als True (angenommen, alle sind Primzahlen)
    sieve = [True] * (n + 1)
    
    # Setze 0 und 1 auf False, weil sie keine Primzahlen sind
    sieve[0] = sieve[1] = False
    
    # Gehe durch die Zahlen und markiere alle Vielfachen als Nicht-Primzahlen
    for start in range(2, int(n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, n + 1, start):
                sieve[multiple] = False
    
    # Alle Indizes, die True sind, stellen Primzahlen dar
    primzahlen = [num for num, is_prime in enumerate(sieve) if is_prime]
    
    return primzahlen

# Beispielaufruf:
print(finde_primzahlen(30))  # Ausgabe: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def primfaktoren(n):
    # Liste zur Speicherung der Primfaktoren
    faktoren = []
    
    # Teile n so lange durch 2, wie es durch 2 teilbar ist
    while n % 2 == 0:
        faktoren.append(2)
        n //= 2
    
    # Gehe alle ungeraden Zahlen von 3 bis √n durch
    faktor = 3
    while faktor * faktor <= n:
        while n % faktor == 0:
            faktoren.append(faktor)
            n //= faktor
        faktor += 2
    
    # Wenn n größer als 2 ist, ist n selbst ein Primfaktor
    if n > 2:
        faktoren.append(n)
    
    return faktoren

# Beispielaufruf:
print(primfaktoren(56))  # Ausgabe: [2, 2, 2, 7]
print(primfaktoren(315))  # Ausgabe: [3, 3, 5, 7]
print(primfaktoren(97))   # Ausgabe: [97]

def ist_primzahl(num):
    # Überprüfen, ob num eine Primzahl ist
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def n_primzahl(n):
    count = 0  # Zähler für die gefundenen Primzahlen
    num = 2  # Start mit der ersten möglichen Primzahl

    # Schleife, um die n-te Primzahl zu finden
    while True:
        if ist_primzahl(num):
            count += 1
            if count == n:
                return num  # Wenn die n-te Primzahl gefunden ist, gib sie zurück
        num += 1

# Beispielaufruf:
print(n_primzahl(5))  # Ausgabe: 11 (die 5. Primzahl)
print(n_primzahl(10)) # Ausgabe: 29 (die 10. Primzahl)
print(n_primzahl(10000)) # Ausgabe: 541 (die 100. Primzahl)

print(ist_primzahl(n_primzahl(10000)))


def ggT(a, b):
    # Euklidischer Algorithmus zur Berechnung des ggT
    while b != 0:
        a, b = b, a % b
    return a

def kgV(a, b):
    # Berechnung des kgV anhand der Formel: kgV = |a * b| / ggT(a, b)
    return abs(a * b) // ggT(a, b)

# Beispielaufruf:
print(kgV(12, 18))  # Ausgabe: 36
print(kgV(7, 5))    # Ausgabe: 35
print(kgV(15, 25))  # Ausgabe: 75

def prod(a,b):
    return ggT(a,b)*kgV(a,b)

print("Produkt: "+str(prod(3,5)))




def quadratwurzel(x, epsilon=1e-6):
    # Wenn x negativ ist, gibt es keine reale Quadratwurzel
    if x < 0:
        return "Ungültige Eingabe (negative Zahl)"
    
    # Startwert für die Näherung, z.B. x / 2
    y = x / 2.0
    
    # Iterative Berechnung der Quadratwurzel mit dem Newton-Raphson-Verfahren
    while abs(y * y - x) > epsilon:
        y = (y + x / y) / 2
    
    return y

# Beispielaufrufe:
print(quadratwurzel(25))  # Ausgabe: 5.0
print(quadratwurzel(2))   # Ausgabe: ungefähr 1.4142135623730951
print(quadratwurzel(9))   # Ausgabe: 3.0
print(quadratwurzel(0))   # Ausgabe: 0.0
print(quadratwurzel(-4))  # Ausgabe: Ungültige Eingabe (negative Zahl)


def ist_prime(n):
    """Hilfsfunktion, um zu prüfen, ob eine Zahl eine Primzahl ist."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_twins(limit):
    """Funktion, um alle Primzwillinge bis zu einer Zahl 'limit' zu finden."""
    primtwillinge = []
    
    # Durchlaufe alle Zahlen von 2 bis limit - 2
    for i in range(2, limit - 1):
        if ist_prime(i) and ist_prime(i + 2):
            primtwillinge.append((i, i + 2))
    
    return primtwillinge

# Beispielaufrufe:
print(find_prime_twins(30))  # Ausgabe: [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31)]
print(find_prime_twins(50))  # Ausgabe: [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)]




def ist_pythagoreisches_triplet(a, b, c):
    """Überprüft, ob die drei Zahlen a, b, c ein pythagoreisches Triplet bilden."""
    # Sortiere die Zahlen, damit wir sicherstellen, dass c die größte Zahl ist
    a, b, c = sorted([a, b, c])
    
    # Überprüfen, ob a^2 + b^2 = c^2
    return a**2 + b**2 == c**2

# Beispielaufrufe:
print(ist_pythagoreisches_triplet(3, 4, 5))  # Ausgabe: True (3, 4, 5 ist ein Triplet)
print(ist_pythagoreisches_triplet(5, 12, 13))  # Ausgabe: True (5, 12, 13 ist ein Triplet)
print(ist_pythagoreisches_triplet(8, 15, 17))  # Ausgabe: True (8, 15, 17 ist ein Triplet)
print(ist_pythagoreisches_triplet(7, 24, 25))  # Ausgabe: True (7, 24, 25 ist ein Triplet)
print(ist_pythagoreisches_triplet(1, 2, 3))    # Ausgabe: False (1, 2, 3 ist kein Triplet)



import random
import math

def ist_prime(n):
    """Überprüft, ob n eine Primzahl ist."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def zufallszahl_und_prime_check(n):
    """Generiert eine zufällige Zahl zwischen 1 und 100 und prüft, ob sie eine Primzahl ist."""
    zufallszahl = random.randint(1, n)
    print(f"Zufallszahl: {zufallszahl}")
    
    if ist_prime(zufallszahl):
        return f"{zufallszahl} ist eine Primzahl."
    else:
        return f"{zufallszahl} ist keine Primzahl."

# Beispielaufruf:
print(zufallszahl_und_prime_check(100))


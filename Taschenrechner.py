def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Fehler! Division durch null."
    return x / y

def power(x, y):
    return x ** y

def exp_x(x, n_terms=20):
    result = 1  # Der erste Term der Reihe ist 1
    term = 1    # Der erste Term (x^0 / 0!) ist 1
    for n in range(1, n_terms):
        term *= x / n  # Der nächste Term wird iterativ berechnet
        result += term  # Der Term wird zur Gesamtsumme hinzugefügt
    return result


import math

# Beispiel:
x = 0  # Berechnung von e^1
result = exp_x(x)
print(f"e^{x} ≈ {result}")
x = 1  # Berechnung von e^1
result = exp_x(x)
print(f"e^{x} ≈ {result}")



def sin_x(x, n_terms=20):
    result = 0
    term = x  # Der erste Term ist einfach x
    for n in range(n_terms):
        result += term
        # Berechne den nächsten Term
        term *= -x**2 / ((2*n+2) * (2*n+3))  # Der nächste Term basiert auf dem vorherigen
    return result

def cos_x(x):
    return sin_x(x+math.pi/2,n_terms=20)

# Beispiel:
x = 0  # Berechnung von sin(1)
result = cos_x(x)
print(f"cos({x}) ≈ {result}")

x = math.pi  # Berechnung von sin(1)
result = cos_x(x)
print(f"cos({x}) ≈ {result}")


def calculator():
    print("Taschenrechner")
    print("Wähle eine Operation:")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")
    print("5. Potenz")
    print("6. exp")
    print("7. Sinus")
    print("8. Cosinus")

    while True:
        # Eingabe der Operation
        choice = input("Gib die Nummer der Operation ein (1/2/3/4/5/6/7/8): ")

        # Überprüfen, ob die Eingabe gültig ist
        if choice in ['1', '2', '3', '4', '5']:
            # Eingabe der Zahlen
            num1 = float(input("Gib die erste Zahl ein: "))
            num2 = float(input("Gib die zweite Zahl ein: "))

            # Berechnungen basierend auf der Wahl
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
        else:
            print("Ungültige Eingabe! Bitte wähle eine gültige Zahl von 1 bis 5.")
        
        # Weitere Berechnungen oder Beenden
        next_calculation = input("Möchtest du eine weitere Berechnung durchführen? (ja/nein): ").lower()
        if next_calculation != 'ja':
            print("Taschenrechner beendet.")
            break

calculator()
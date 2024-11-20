
from datetime import datetime, timedelta

def datum_n_tage_später(n):
    """Berechnet das Datum, das n Tage nach dem aktuellen Datum liegt."""
    # Holen des aktuellen Datums
    aktuelles_datum = datetime.today().date()
    
    # Berechnung des zukünftigen Datums durch Addition von n Tagen
    zukünftiges_datum = aktuelles_datum + timedelta(days=n)
    
    return zukünftiges_datum

# Beispielaufruf:
n = 10  # Beispiel: 10 Tage nach dem aktuellen Datum
print(f"Heutiges Datum: {datetime.today().date()}")
print(f"Datum in {n} Tagen: {datum_n_tage_später(n)}")


def get_weekday(day, month, year):
    # Wenn der Monat Januar oder Februar ist, betrachten wir ihn als 13. bzw. 14. Monat des Vorjahres
    if month < 3:
        month += 12
        year -= 1

    # Berechnung der Variablen K und J
    K = year % 100
    J = year // 100

    # Zellersche Kongruenzformel
    h = (day + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

    # Wochentag: 0=Samstag, 1=Sonntag, ..., 6=Freitag
    weekdays = ["Samstag", "Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
    return weekdays[h]

# Beispiel:
day = 20
month = 11
year = 2024
weekday = get_weekday(day, month, year)
print(f"Der {day}.{month}.{year} ist ein {weekday}.")

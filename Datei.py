def dateigröße_umwandeln(dateipfad):
    """Ermittelt die Größe einer Datei und gibt sie in der passenden Einheit zurück."""
    # Ermitteln der Dateigröße in Byte
    import os
    dateigröße = os.path.getsize(dateipfad)
    
    # Die verschiedenen Einheiten, beginnend mit Byte
    einheiten = ["Byte", "KB", "MB", "GB", "TB", "PB"]
    
    # Bestimmen der richtigen Einheit
    i = 0
    while dateigröße >= 1024 and i < len(einheiten) - 1:
        dateigröße /= 1024
        i += 1
    
    # Rückgabe der Dateigröße in der passenden Einheit, auf 2 Dezimalstellen gerundet
    return f"{dateigröße:.2f} {einheiten[i]}"

# Beispielaufruf:
# Geben Sie den Pfad einer Datei auf Ihrem System ein
print(dateigröße_umwandeln("tutorials.py"))
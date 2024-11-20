def quicksort(arr):
    # Wenn die Liste nur ein Element oder leer ist, ist sie bereits sortiert
    if len(arr) <= 1:
        return arr
    
    # Wähle ein Pivot-Element (hier das mittlere Element)
    pivot = arr[len(arr) // 2]
    
    # Teile das Array in drei Teile:
    # - Die Elemente kleiner als das Pivot
    # - Die Elemente gleich dem Pivot
    # - Die Elemente größer als das Pivot
    links = [x for x in arr if x < pivot]
    mitte = [x for x in arr if x == pivot]
    rechts = [x for x in arr if x > pivot]
    
    # Wende Quicksort rekursiv auf die Teile an und kombiniere die Ergebnisse
    return quicksort(links) + mitte + quicksort(rechts)

# Beispielaufruf:
arr = [33, 10, 55, 17, 8, 42, 90, 2]
sorted_arr = quicksort(arr)
print(sorted_arr)

def bubble_sort(arr):
    """Sortiert eine Liste mit dem Bubble Sort-Algorithmus."""
    n = len(arr)
    
    # Äußere Schleife für alle Durchgänge durch die Liste
    for i in range(n):
        # Wir gehen nur bis n-i-1, da nach jedem Durchgang das größte Element
        # an das Ende "aufgeblasen" wird und wir es nicht erneut prüfen müssen.
        for j in range(0, n - i - 1):
            # Wenn das aktuelle Element größer ist als das nächste, tausche sie
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

# Beispielaufruf:
unsortierte_liste = [64, 34, 25, 12, 22, 11, 90]
sortierte_liste = bubble_sort(unsortierte_liste)

print(f"Sortierte Liste: {sortierte_liste}")


def merge_sort(arr):
    """Sortiert die Liste arr mit dem Merge Sort-Algorithmus."""
    if len(arr) <= 1:
        return arr

    # Teile die Liste in zwei Hälften
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Rekursiver Aufruf von merge_sort für beide Hälften
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Mische (merge) die beiden sortierten Hälften
    return merge(left_half, right_half)

def merge(left, right):
    """Hilfsfunktion, die zwei sortierte Listen zusammenführt."""
    sorted_list = []
    i = j = 0

    # Vergleiche die Elemente der beiden Listen und füge das kleinere Element zur sortierten Liste hinzu
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Wenn noch Elemente in der linken Liste übrig sind, füge sie hinzu
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    # Wenn noch Elemente in der rechten Liste übrig sind, füge sie hinzu
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

# Beispielaufruf:
unsortierte_liste = [38, 27, 43, 3, 9, 82, 10]
sortierte_liste = merge_sort(unsortierte_liste)

print(f"Sortierte Liste: {sortierte_liste}")

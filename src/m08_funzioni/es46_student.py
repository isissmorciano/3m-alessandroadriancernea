# # Esercizio 46: Funzione per calcolare l'area di un triangolo

# ## Obiettivo
# Creare una funzione che calcola l'area di un triangolo dati base e altezza.

# ## Istruzioni
# 1. Definire una funzione chiamata `calcola_area_triangolo` che accetta due parametri: `base` (float) e `altezza` (float).
# 2. La funzione deve restituire l'area calcolata come (base * altezza) / 2.
# 3. Nel programma principale, chiedere all'utente di inserire base e altezza, chiamare la funzione e stampare il risultato.

def calcola_area_triangolo(base: float, altezza: float) -> float:
    area: float = (base*altezza) / 2
    return area

def main() -> None:
    base: int = int(input("Quanto vuoi che valga la tua base?: "))
    altezza: int = int(input("Quanto vuoi che valga la tua altezza?: "))
    area: float = calcola_area_triangolo(base, altezza)
    print(f"La base che mi hai dato è: {base}, mentre l'altezza è: {altezza} ed l'area è: {area}")

main()
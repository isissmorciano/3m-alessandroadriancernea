# # Esercizio 47: Calcolatrice modulare

# ## Obiettivo
# Creare una calcolatrice semplice usando l'approccio modulare con funzioni.

# ## Istruzioni
# 1. Definire una funzione `chiedi_numeri` che chiede due numeri e li restituisce in una lista.
# 2. Definire una funzione `scegli_operazione` che mostra un menu e restituisce l'operazione scelta (+, -, *, /).
# 3. Definire una funzione `calcola` che accetta due numeri e l'operazione e restituisce il risultato.
# 4. Definire una funzione `main` che orchestra il programma chiamando le altre funzioni.
# 5. Gestire l'operazione non valida restituendo None e stampando un messaggio.

def chiedi_numeri() -> list[float]:
    
    numero1: float = float(input("Quanto vuoi che valga il primo numero?: "))
    numero2: float = float(input("Quanto vuoi che valga il secondo numero?: "))
    return [numero1, numero2]

def scegli_operazione():
    
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")

    scelta = int(input("Inserisci la scelta: "))
    if scelta == "1":
        return "+"
    elif scelta == "2":
        return "-"
    elif scelta == "3":
        return "*"
    elif scelta == "4":
        return "/"
    else:
        return "Devi scegliere tra 1 e 4"

def calcola(numero1: float, numero2: float, operazione: float):
    if operazione == "+":
        return numero1 + numero2
    elif operazione == "-":
        return numero1 - numero2
    elif operazione == "*":
        return numero1 * numero2
    elif operazione == "/":
        if numero2 != 0:
            return numero1 / numero2
        else:
            return print("errore: c'è uno zero")
    else:
        return

def main() -> None:
#"""Funzione principale che orchestra il programma."""
    print("Benvenuto nella Calcolatrice Modulare!")
    numeri = chiedi_numeri()
    operazione = scegli_operazione()
    risultato = calcola(numeri[0], numeri[1], operazione)

    if risultato is not None:
        print(f"Il risultato è: {risultato}")
    else:
        print("Operazione non valida.")

main()
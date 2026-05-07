# # Esercizio 24: Creazione e stampa di una tabella di 1

# ## Obiettivo
# Scrivere un programma Python che chieda all'utente di inserire il numero di righe (n) e colonne (m), e stampi una tabella di 1 di dimensioni n x m.

# ## Istruzioni
# 1. Richiedere all'utente di inserire n (numero di righe) e m (numero di colonne), entrambi interi positivi.
# 2. Stampare la tabella, con ogni riga su una linea separata e gli elementi separati da spazi.

# ## Suggerimento
# Usa `print(1, end=" ")` per stampare i numeri senza andare a capo, e `print()` per andare a capo dopo ogni riga.

# ## Esempio
# Per n=3, m=4:
# ```
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# ```

n: int = int(input("Dimmi il numero di righe che vuoi mettere: "))
if n <= 0:
    print("Deve essere un numero positivo ed intero!")
    exit()

m: int = int(input("Dimmi il numero di colonne che vuoi mettere: "))
if m <= 0:
    print("Deve essere un numero positivo ed intero!")
    exit()

carattere_scelto: str = input("Dimmi il carattere che vuoi mettere: ")
print()
print()

for i in range(n): # Viene eseguito sulle righe: si ripete 3 volte
    for j in range(m): # Viene eseguito sulle colonne: si ripete 4 volte
        # Queste istruzioni vengono eseguite 12 volte (3x4)
        print(carattere_scelto, end=" ") 
    print()

# # Esercizio 26: Ordinamento manuale di una lista di numeri

# ## Obiettivo
# Scrivere un programma Python che chieda all'utente quanti numeri inserire,
#  li legga uno per uno, li memorizzi in una lista,
#  e ordini la lista in ordine crescente utilizzando un algoritmo di ordinamento manuale (senza usare `sort()` o funzioni simili).

# ## Istruzioni
# 1. Richiedere all'utente di inserire il numero di valori da considerare (numero intero positivo).
# 2. Utilizzare un ciclo per leggere ciascun numero dall'utente e aggiungerlo a una lista vuota (inizializzata come `numeri = []`).
# 3. Implementare un ordinamento manuale usando cicli annidati.
# 4. Gestire il caso in cui la lista sia vuota (numero di valori = 0), stampando un messaggio di errore.
# 5. Stampare la lista originale e quella ordinata, ad esempio: "Lista originale: [numeri originali], Lista ordinata: [numeri ordinati]".

# ## Nota sull'algoritmo manuale
# Esistono diversi modi per ordinare manualmente una lista.
#  Il più semplice si chiama bubble sort, che confronta elementi adiacenti e li scambia se necessario.

# ## Esempio
# Per 4 numeri: 3, 1, 4, 2  
# Lista originale: [3, 1, 4, 2]  
# Lista ordinata: [1, 2, 3, 4]



valore_considerato = int(input("Quanti valori vuoi considerare?: "))
if valore_considerato < 1:
    print("Deve essere intero & positivo!")

numeri: list[int] = []

for i in range(valore_considerato):
    numero: int = int(input("Inserisci valore: "))
    numeri.append(numero)

for i in range(   len(numeri)-1     ):
    # if numeri[0] > numeri[1] # 3 > 1
    if numeri[i] > numeri[i+1]:
        numeri[i], numeri[i+1] = numeri[i+1], numeri[i] # invertili 

print(numeri)



# valore_minimo = numeri[0]

# for i in numeri:
#     if i < valore_minimo:
#         valore_minimo = i

# print (valore_minimo)


import random

# # Esercizio 49: Gioco "Indovina il numero" con approccio top-down

# ## Obiettivo
# Creare un gioco semplice dove l'utente deve indovinare un numero casuale generato dal computer, con feedback sui tentativi e contatore.
#  Il programma deve essere risolto usando l'approccio top-down, decomponendo il problema principale in sottoproblemi più piccoli, ciascuno gestito da una funzione dedicata.

# ## Cos'è l'approccio top-down?
# L'approccio top-down consiste nel dividere un problema complesso in sottoproblemi più semplici e indipendenti.
#  Ogni sottoproblema viene risolto da una funzione separata, migliorando la leggibilità, la manutenibilità e il test del codice.
#  In questo esercizio, il gioco è decomposto in funzioni per generazione, input, verifica, contatore e output.

# ## Istruzioni
# 1. Definire una funzione `genera_numero` che genera e restituisce un numero casuale tra 1 e 100.
# 2. Definire una funzione `chiedi_tentativo` che chiede all'utente di inserire un tentativo e lo restituisce come intero.
# 3. Definire una funzione `verifica_tentativo` che accetta il tentativo e il numero segreto, e restituisce una stringa:
#  "corretto" se indovinato, "alto" se troppo alto, "basso" se troppo basso.
# 4. Definire una funzione `aggiorna_contatore` che incrementa e restituisce il numero di tentativi.
# 5. Definire una funzione `stampa_fine` che accetta i tentativi e il numero, e stampa un messaggio di vittoria.
# 6. Definire una funzione `main` che orchestra il gioco: genera il numero, gestisce il ciclo di tentativi, chiama le altre funzioni e termina quando indovinato.
# 7. Nel ciclo principale, usa un `while True` per continuare fino a indovinamento, chiamando le funzioni appropriate.

# ## Suggerimenti
# - Usa il modulo `random` per generare il numero (importalo all'inizio).
# - Gestisci input non validi (es. non numeri) nella funzione `chiedi_tentativo` con un try-except.
# - Testa ogni funzione separatamente prima di integrarle.

def genera_numero() -> int:
    return random.randint(1, 100)

def chiedi_tentativo(numero_generato: int) -> int:
    try:
        tentativo: int = int(input("Dimmi un numero da 1 a 100: "))
        return tentativo
    except ValueError:
        print("Errore inserisci un numero")

def verifica_tentativo(previsione, numero_da_indovinare) -> str:
    if previsione > numero_da_indovinare:
        return "alto"
    elif previsione < numero_da_indovinare:
        return "basso"
    elif previsione == numero_da_indovinare:
        return "corretto"
    else:
        return "boh!"


def aggiorna_contatore(contatore: int) -> int:
    return contatore + 1

def stampa_fine(tentativo, numero_segreto) -> str:
    if tentativo == numero_segreto:
        return f"hai indovinato con {contatore} tentativi!"

def main():
    numero_generato: int = genera_numero()
    print(f"SOLO PER NOI il numero generato e': {numero_generato}")  # 63

    numero_di_tentativi = 0

    while True:
        tentativo: int = chiedi_tentativo(numero_generato) # chiedi un numero all utente
        # verifica se l'utente ha indovinato
        risultato: str = verifica_tentativo(tentativo, numero_generato)
        numero_di_tentativi = aggiorna_contatore(numero_di_tentativi)
        if risultato == "corretto":
            print(f"Hai indovinato in {numero_di_tentativi} tentativi")
            break
        elif risultato == "alto":
            print(f"Riprova. Il numero da indovinare e' piu' basso")
        elif risultato == "basso":
            print(f"Riprova. Il numero da indovinare e' piu' alto")
        else:
            print(f"AHHHHHHHHHHHHHHHH")


    
            
    # final: str = stampa_fine(tentativo, numero_generato)
    # print(f"Hey bro, il numero randomico era {numero_generato}")
    # print(f"ci hai messo {blabla}")
    
main()
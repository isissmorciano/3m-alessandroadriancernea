# # Esercizio 48: Calcolo del fattoriale con ricorsione

# ## Obiettivo
# Creare una funzione ricorsiva che calcola il fattoriale di un numero.

# ## Cos'è la ricorsione?
# La ricorsione è una tecnica di programmazione in cui una funzione chiama se stessa per risolvere un problema. Una funzione ricorsiva deve avere:
# - Un **caso base**: una condizione che ferma la ricorsione (ad esempio, quando n == 0 o n == 1).
# - Un **caso ricorsivo**: la chiamata alla funzione stessa con un input ridotto (ad esempio, fattoriale(n-1)).

# Questo approccio è utile per problemi che possono essere divisi in sottoproblemi simili, come il calcolo del fattoriale.

# ## Istruzioni
# 1. Definire una funzione chiamata `fattoriale` che accetta un parametro intero `n` e restituisce il fattoriale.
# 2. La funzione deve usare la ricorsione: fattoriale(n) = n * fattoriale(n-1), con caso base fattoriale(0) = 1.
# 3. Nel programma principale, chiedere all'utente di inserire un numero intero positivo, chiamare la funzione e stampare il risultato.


def fattoriale(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * fattoriale(n-1)

# fattoriale di 5 --> 5 * fattoriale(4) --> 5 * 24 --> 120
# fattoriale di 4 --> 4 * fattoriale(3) --> 4 * 6 --> 24
# fattoriale di 3 --> 3 * fattoriale(2) --> 3 * 2 --> 6
# fattoriale di 2 --> 2 * fattoriale(1) --> 2 * 1 --> 2
# fattoriale di 1 --> 1


print(fattoriale(n = 5))
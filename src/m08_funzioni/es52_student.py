# # Esercizio 52: Calcolatore BMI con approccio top-down

# ## Obiettivo
# Creare un programma per calcolare l'Indice di Massa Corporea (BMI) e classificare il risultato usando l'approccio top-down con molteplici funzioni specializzate.

# ## Formula BMI
# BMI = peso (kg) / (altezza (m))²

# ## Categorie BMI
# - < 18.5: Sottopeso
# - 18.5 - 24.9: Peso normale
# - 25.0 - 29.9: Sovrappeso
# - ≥ 30.0: Obeso

# ## Approccio top-down
# Decomporre il problema principale in sottoproblemi indipendenti:
# - Acquisire i dati dell'utente (peso e altezza)
# - Validare i dati inseriti
# - Calcolare il BMI
# - Classificare il risultato in categoria
# - Visualizzare il risultato in modo leggibile
# - Gestire il menu principale

# ## Istruzioni

# 1. **Definire `chiedi_peso()`**: Chiede all'utente il peso in kg. Valida che sia > 0. Se non valido, chiede di nuovo. Restituisce il peso come float.

# 2. **Definire `chiedi_altezza()`**: Chiede all'utente l'altezza in metri. Valida che sia > 0. Se non valido, chiede di nuovo. Restituisce l'altezza come float.

# 3. **Definire `calcola_bmi(peso, altezza)`**: Accetta peso (kg) e altezza (m), calcola e restituisce il BMI come float.

# 4. **Definire `classifica_bmi(bmi)`**: Accetta il valore BMI e restituisce una stringa con la categoria: "Sottopeso", "Peso normale", "Sovrappeso" o "Obeso".

# 5. **Definire `get_colore_categoria(bmi)`**: Accetta il BMI e restituisce un'emoji per visualizzare la categoria:
#    - BMI < 18.5: "🔵 Sottopeso"
#    - BMI 18.5-24.9: "🟢 Peso normale"
#    - BMI 25.0-29.9: "🟡 Sovrappeso"
#    - BMI ≥ 30.0: "🔴 Obeso"

# 6. **Definire `stampa_risultato(peso, altezza, bmi, categoria)`**: Stampa un risultato formattato con:
#    - Peso: X.X kg
#    - Altezza: X.XX m
#    - BMI: X.X
#    - Categoria con emoji

# 7. **Definire `stampa_menu()`**: Stampa il menu con opzioni:
#    - "1. Calcola BMI"
#    - "2. Esci"

# 8. **Definire `main()`**: Orchestra il programma:
#    - Mostra il menu in un ciclo while
#    - Se scelta 1: chiama `chiedi_peso()` e `chiedi_altezza()`, calcola BMI e categoria, stampa il risultato
#    - Se scelta 2: esce dal ciclo
#    - Gestisce scelte non valide

# ## Suggerimenti
# - Usa try-except per convertire gli input a float in `chiedi_peso()` e `chiedi_altezza()`
# - La formula: BMI = peso / (altezza * altezza)
# - Usa if-elif-else per classificare il BMI
# - Formatta il BMI con 1 decimale nella stampa (f"{bmi:.1f}")
# - Ogni funzione ha un compito specifico (single responsibility)

def chiedi_peso() -> float:
    domanda_peso = float(input("Quanto pesi in kg?: "))
    if domanda_peso < 0:
        print("Errore: Sei un fantasma.")
    return domanda_peso

def chiedi_altezza() -> float:
    domanda_altezza = float(input("Quanto sei alto in metri?: "))
    if domanda_altezza < 0:
        print("Errore: Sei micronanoultrasuperscopicamente piccolo.")
    return domanda_altezza

def calcola_bmi(domanda_peso: float, domanda_altezza: float) -> float:
    bmi = domanda_peso * (domanda_altezza * domanda_altezza)
    return bmi

def classifica_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return("Sei sottopeso.")
    elif bmi >= 18.5 and bmi <= 24.9:
        return("Pesi come la maggioranza.")
    elif bmi >= 25.0 and bmi <= 29.9:
        return("Sei sovrappeso.")
    else:
        return("Sei obeso.")

def get_colore_categoria(bmi: float) -> str:
    if bmi < 18.5:
        return("🔵Sei sottopeso.")
    elif bmi >= 18.5 and bmi <= 24.9:
        return("🟢Pesi come la maggioranza .")
    elif bmi >= 25.0 and bmi <= 29.9:
        return("🟡Sei sovrappeso.")
    else:
        return("🔴Sei obeso.")

def stampa_risultato(peso: float, altezza: float, bmi: float, get_colore_categoria: str) -> None:
    stampa_peso = print(f"il tuo peso è: {peso:.1f} kg")
    stampa_altezza = print(f"la tua altezza è: {altezza:.2f} metro/i")
    stampa_bmi = print(f"il tuo bmi è: {bmi:.1f}")
    stampa_categoria = print(f"la tua categoria di peso è: {get_colore_categoria}\n")

def stampa_menu():
    print("===MENU===")
    print("1. Calcoli BMI")
    print("2. Esci")

def main():
    while True:
        stampa_menu()
        scelta = input("Scegli 1 o 2!: ")

        if scelta == "1":
            domanda_peso = chiedi_peso()
            domanda_altezza = chiedi_altezza()
            bmi = calcola_bmi(domanda_peso, domanda_altezza)
            categoria = get_colore_categoria(bmi)
            stampa_risultato(domanda_peso, domanda_altezza, bmi, get_colore_categoria)
        elif scelta == "2":
            print("ciau ciau =D")
            break
        else:
            print("scelta non valida")

main()
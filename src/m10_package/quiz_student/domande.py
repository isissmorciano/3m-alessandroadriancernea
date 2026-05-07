# ### Parte 2: Modulo `domande.py`
# Funzioni per gestire le domande (rappresentate come dizionari):
# - `crea_domanda(testo: str, opzioni: list[str], risposta: int) -> dict:`
#   - `risposta` è l'indice 0-based dell'opzione corretta
# - `info_domanda(domanda: dict) -> str:`
#   - Restituisce una stringa leggibile con domanda + opzioni numerate
# - `risposta_valida(domanda: dict, scelta: int) -> bool:`
#   - Verifica se la scelta (1-based) è valida
# - `verifica_risposta(domanda: dict, scelta: int) -> bool:`
#   - Restituisce True se la scelta (1-based) è corretta

def crea_domanda(testo: str, opzioni: list[str], risposta: int) -> dict:
    boh = {"testo": testo, "opzioni": opzioni, "risposta": risposta}
    return boh  

def info_domanda(domanda: dict) -> str:
    info = "Domanda: " + domanda["testo"] + "\n"

    for i in range(len(domanda["opzioni"])):
        numero = i + 1
        testo_opzione = domanda["opzioni"][i]
        info += str(numero) + ". " + testo_opzione + "\n"

    return info

def risposta_valida(domanda: dict, scelta: int) -> bool:
    return 1 <= scelta <= len(domanda["opzioni"])

def verifica_risposta(domanda: dict, scelta: int) -> bool:
    if not risposta_valida(domanda, scelta):
        return False
    return domanda["risposta"] == scelta - 1
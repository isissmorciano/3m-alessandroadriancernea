# ### Parte 3: Modulo `risultati.py`
# Funzioni per gestire i risultati del quiz e per salvarli/caricarli su file JSON:
# - `crea_risultati() -> dict:`
#   - Restituisce un dizionario con chiavi: `totale`, `corretti`
# - `registra_risposta(risultati: dict, corretta: bool) -> None:`
#   - Aggiorna i totali
# - `percentuale_corrette(risultati: dict) -> float:`
#   - Restituisce la percentuale di risposte corrette (1 decimale)
# - `mostra_risultati(risultati: dict) -> str:`
#   - Restituisce una stringa leggibile del riepilogo
# - `salva_risultati(risultati: dict, nome_file: str) -> None:`
#   - Salva i risultati in un file JSON
# - `carica_risultati(nome_file: str) -> dict:`
#   - Carica i risultati da un file JSON

def crea_risultati() -> dict:
    return {"totale": 0, "corretti": 0}

def registra_risposta(risultati: dict, corretta: bool) -> None:
    risultati["totale"] 
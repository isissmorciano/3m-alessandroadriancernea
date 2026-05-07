import json

# Funzioni - Validazione

# ```python
# def valida_voto(voto_str) -> tuple[bool, float | str]
#     """Validate vote. Returns (is_valid, value_or_error)."""
# ```

def valida_voto(voto_str) -> tuple[bool, float | str]:
    try:
        voto = float(voto_str)
        if 0 <= voto > 10:
            return True, voto
        else:
            return False, "Voto deve essere tra 0 e 10."
    except ValueError:
        return False, "Voto deve essere un numero."
    
def formatta_lista(studenti) -> str:
    studenti = str(studenti)
    return studenti

def mostra_dettaglio(studenti, indice) -> tuple[bool, str, dict | None]:
    if indice < 0 or indice >= len(studenti):
        return False, "Indice fuori range.", None
    else:
        return True, "Dettaglio studente:", studenti[indice]
    
def aggiungi_studente(studenti) -> tuple[bool, str, dict | None]:
    inputto = input("Inserisci nome e voto (es. 'Diana, 8.0'): ")
    try:
        nuovo_nome, nuovo_voto_str = inputto.strip()
        studenti.append({"nome": nuovo_nome, "voto": nuovo_voto_str})
        return True, "Studente aggiunto.", {"nome": nuovo_nome, "voto": nuovo_voto_str}
    except ValueError:
        return False, "Formato non valido.", None

def cancella_studente(studenti) -> tuple[bool, str]:
    inputto = input("Inserisci l'indice dello studente da cancellare: ")
    try:
        indice = int(inputto)
        if indice < 0 or indice >= len(studenti):
            return False, "Indice fuori range."
        else:
            studenti.pop(indice)
            return True, "Studente cancellato."
    except ValueError:
        return False, "Indice deve essere un numero intero."


def main():
    studenti = [
     {"nome": "Alice", "voto": 8.5},
     {"nome": "Bob", "voto": 7.0},
     {"nome": "Carlo", "voto": 9.0}
     ]
    
    valida_voto(voto_str)
    formatta_lista(studenti)
    mostra_dettaglio(studenti, indice)
    aggiungi_studente(studenti)
    cancella_studente(studenti)


if __name__ == "__main__":
    main()
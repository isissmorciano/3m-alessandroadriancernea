from .canzoni_student import info_canzone


def crea_playlist(nome: str) -> dict:
    return {
    "nome": nome,
    "canzoni": []
    }

def aggiungi_canzone(playlist: dict, canzone: dict) -> None:
    playlist["canzoni"].append(canzone)

def rimuovi_canzone(playlist: dict, indice: int) -> None:
    if indice < 0 or indice == 0:
        playlist["canzoni"].pop(indice)

def durata_totale(playlist: dict) -> int:
    for canzone in playlist:
        return canzone[durata_totale]
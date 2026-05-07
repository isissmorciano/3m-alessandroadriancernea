def conta_parole(nome_file: str) -> dict[str, int]:
    """Legge un file e conta le occorrenze di ogni parola (case-insensitive, senza punteggiatura)."""
    conteggio = {}
    with open(nome_file, "r", encoding="utf-8") as file:
        contenuto = file.read().lower().replace(".", "").replace(",", "")
        parole = contenuto.split()
        
        for parola in parole:
            if parola in conteggio:
                conteggio[parola] += 1
            else:
                conteggio[parola] = 1
    return conteggio

def stampa_conteggio(dizionario: dict[str, int]) -> None:
    print("Conteggio parole:")
    for parola, numero in sorted(dizionario.items()):
        print(f"{parola}: {numero}")

def main():
    testo = "Python è un linguaggio di programmazione. Python è semplice e potente."
    nome_file = "es57_student.txt"
    
    with open(nome_file, "w", encoding="utf-8") as file:
        file.write(testo)
    
    dizionario_conteggio = conta_parole(nome_file)
    stampa_conteggio(dizionario_conteggio)

if __name__ == "__main__":
    main()

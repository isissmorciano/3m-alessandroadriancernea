def aggiungi_elemento(lista: list[dict]) -> bool:
    nome = input("Nome elemento: ")
    if not nome or nome.isdigit():
        return False

    try:
        prezzo = float(input("Prezzo: "))
    except ValueError:
        return False

    lista.append({"nome": nome, "prezzo": prezzo})
    return True


def rimuovi_elemento(lista: list[dict]) -> None:
    nome = input("Nome da rimuovere: ")
    for item in lista:
        if item["nome"] == nome:
            lista.remove(item)
            print("Elemento rimosso")
            return
    print("Elemento non trovato")


def visualizza_lista(lista: list[dict]) -> None:
    if not lista:
        print("La lista è vuota")
    else:
        for item in lista:
            print(f"{item['nome']}: {item['prezzo']}€")


def calcola_totale(lista: list[dict]) -> float:
    return sum(item["prezzo"] for item in lista)


def main():
    lista = []

    while True:
        print("======= MENU =======")
        print("1. Aggiungi elemento")
        print("2. Rimuovi elemento")
        print("3. Visualizza lista")
        print("4. Visualizza totale")
        print("5. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            if aggiungi_elemento(lista):
                print("Elemento aggiunto")
            else:
                print("Errore nell'aggiunta")
        elif scelta == "2":
            rimuovi_elemento(lista)
        elif scelta == "3":
            visualizza_lista(lista)
        elif scelta == "4":
            print(f"Totale: {calcola_totale(lista)}€")
        elif scelta == "5":
            print("Uscita...")
            break
        else:
            print("Scelta non valida")

main()
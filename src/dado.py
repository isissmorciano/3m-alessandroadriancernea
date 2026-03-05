import random

def dado() -> int:
    while True:
        dado = random.randint(1, 6)
        if dado != 6:
            print("non è uscito 6")
        else:
            print(f"è uscito {dado}")
            break

dado()
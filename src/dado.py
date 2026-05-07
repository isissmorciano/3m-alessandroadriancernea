import random

def dado() -> int:
    while True:
        dado = random.randint(1, 2)
        if dado == 1:
            print("Si")
        else:
            print("no")
            break

dado()
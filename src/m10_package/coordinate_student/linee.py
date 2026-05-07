from coordinate_student.punti import distanza_tra_punti

def crea_linea(p1: dict, p2: dict) -> dict:
    return {
        "p1": p1,
        "p2": p2
    }

def lunghezza_linea(linea: dict) -> float:
    linea = p1+p2
    return linea

def punto_medio(linea: dict) -> dict:
    #Coordinate: ((x1+x2)/2, (y1+y2)/2)
    coordinate = (x1+x2)/2, (y1+y2)/2
    return coordinate

def info_linea(linea: dict) -> str:
    #Linea da (x1, y1) a (x2, y2)
    linea = (x1, y1) (x2, y2)
    return linea
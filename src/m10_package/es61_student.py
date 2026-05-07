# from musica_student import canzoni, playlist
# from musica_student.playlist_student import Playlist
# from musica_student.canzoni_student import Canzone
from musica_student.canzoni_student import crea_canzone, info_canzone


mia_canzone: dict = crea_canzone(titolo = "boh", artista = "Eminem", durata = 200)

mia_canzone_str: str = info_canzone(mia_canzone)

print(mia_canzone_str)
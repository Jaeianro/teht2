from urllib import request
from player import Player

class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        # Avataan URL ja luetaan sen sisältö
        players_file = request.urlopen(self._url)
        players = []

        for line in players_file:
            # Dekoodataan rivit UTF-8:lla
            decoded_line = line.decode("utf-8")
            parts = decoded_line.split(";")

            # Tarkistetaan, että tiedot ovat kunnossa
            if len(parts) > 3:
                # Luodaan Player-olio ja lisätään se pelaajaluetteloon
                player = Player(
                    parts[0].strip(),  # Pelaajan nimi
                    parts[1].strip(),  # Joukkue
                    int(parts[3].strip()),  # Pisteet
                    int(parts[4].strip())   # Ottelut
                )

                players.append(player)

        return players
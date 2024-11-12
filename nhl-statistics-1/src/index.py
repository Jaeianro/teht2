from statistics_service import StatisticsService
from player_reader import PlayerReader

def main():
    # Luo PlayerReader-olio ja anna sille URL-osoite
    stats = StatisticsService(
      PlayerReader("https://raw.githubusercontent.com/ohjelmistotuotanto-jyu/tehtavat/refs/heads/main/osa2/stats/players-23-24.txt")
    )
    # Haetaan pelaajat Philadelphia Flyers -joukkueesta
    philadelphia_flyers_players = stats.team("PHI")
    # Haetaan kymmenen parasta pistetilaston pelaajaa
    top_scorers = stats.top(10)

    # Tulostetaan Philadelphia Flyers -joukkueen pelaajat
    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    # Tulostetaan kymmenen parasta pistetilaston pelaajaa
    print("Top point getters:")
    for player in top_scorers:
        print(player)

if __name__ == "__main__":
    main()
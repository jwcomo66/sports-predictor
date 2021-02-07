from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
print(client.season_schedule(season_end_year=2021))
client.players_season_totals(
    season_end_year=2018, 
    output_type=OutputType.CSV, 
    output_file_path="./2017_2018_player_season_totals.csv"
)
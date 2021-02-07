from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType, Team
print(client.season_schedule(season_end_year=2021))
client.players_season_totals(
    season_end_year=2018, 
    output_type=OutputType.CSV, 
    output_file_path="./2017_2018_player_season_totals.csv"
)

client.play_by_play(
    home_team=Team.BOSTON_CELTICS, 
    year=2018, month=10, day=16, 
    output_type=OutputType.CSV, 
    output_file_path="./2018_10_06_BOS_PBP.csv"
)
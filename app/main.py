import json
from logic.toss_prediction import predict_toss
from logic.match_prediction import predict_match_winner

# Load data
with open('app/data/historical_stats.json', 'r') as f:
    historical_stats = json.load(f)

with open('app/data/weather_effect.json', 'r') as f:
    weather_effect = json.load(f)

# Inputs
team_a = input("Enter Team A Name (ind,aus,sl,wi,eng,nz,sa):")
team_b = input("Enter Team B Name (ind,aus,sl,wi,eng,nz,sa):")
stadium = input("Enter Stadium Name (wankhede,lords,mcg,oval,newlands,cape town,eden gardens,trafford,chinnaswamy,sydney) :")
weather = input("Enter Weather Condition (sunny/cloudy/rainy): ")

# Fetch stats
stats = {
    "team_a_win_rate": historical_stats["stadiums"][stadium][team_a]["win_rate"],
    "team_b_win_rate": historical_stats["stadiums"][stadium][team_b]["win_rate"],
    "stadium_advantage_team_a": historical_stats["stadiums"][stadium][team_a]["stadium_advantage"],
    "stadium_advantage_team_b": historical_stats["stadiums"][stadium][team_b]["stadium_advantage"],
    "weather_favorability_team_a": weather_effect[weather][team_a],
    "weather_favorability_team_b": weather_effect[weather][team_b],
    "team_a_player_avg": historical_stats["teams"][team_a]["player_avg"],
    "team_b_player_avg": historical_stats["teams"][team_b]["player_avg"],
}

# Predict toss and match
toss_winner = predict_toss(team_a, team_b, historical_stats["toss_wins"])
match_winner = predict_match_winner(team_a, team_b, stats)

# Output results
print(f"Toss Winner: {toss_winner}")
print(f"Predicted Match Winner: {match_winner}")

def predict_match_winner(team_a, team_b, stats):
    score_team_a = (
        stats['team_a_win_rate'] * 0.4 +
        stats['team_a_player_avg'] * 0.3 +
        stats['stadium_advantage_team_a'] * 0.2 +
        stats['weather_favorability_team_a'] * 0.1
    )
    score_team_b = (
        stats['team_b_win_rate'] * 0.4 +
        stats['team_b_player_avg'] * 0.3 +
        stats['stadium_advantage_team_b'] * 0.2 +
        stats['weather_favorability_team_b'] * 0.1
    )
    return team_a if score_team_a > score_team_b else team_b

import random

def predict_toss(team_a, team_b, toss_history):
    team_a_toss_wins = toss_history.get(team_a, 0)
    team_b_toss_wins = toss_history.get(team_b, 0)
    total_tosses = team_a_toss_wins + team_b_toss_wins
    if total_tosses == 0:
        return random.choice([team_a, team_b])
    team_a_probability = team_a_toss_wins / total_tosses
    return team_a if random.random() < team_a_probability else team_b

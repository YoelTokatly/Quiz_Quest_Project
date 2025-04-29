def initialize_game():
    players = []
    scores = {}
    rounds = 3
    return players, scores, rounds

def declare_winner(scores):
    # Find the highest score
    max_score = max(scores.values())

    # Identify the player with the highest score
    for player, score in scores.items():
        if score == max_score:
            print(f"Congratulations, {player}! You won with a score of {score}!")

    
def show_scores(scores):
    for player, score in scores.items():
        print(f"{player} has a score of {score}.")
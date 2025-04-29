def initialize_game():
    players = []
    scores = {}
    rounds = 3
    return players, scores, rounds

def declare_winner(scores):
    # Find the highest score among all players
    max_score = max(scores.values())
    
    # Create a list of all players who have the highest score
    winners = [player for player, score in scores.items() if score == max_score]
    
    # Return the list of winners (could be one or multiple in case of a tie)
    return winners

    # Identify the player with the highest score
    for player, score in scores.items():
        if score == max_score:
            print(f"Congratulations, {player}! You won with a score of {score}!")

    
def show_scores(scores):
    for player, score in scores.items():
        print(f"{player} has a score of {score}.")



        

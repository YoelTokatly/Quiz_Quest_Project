def start():
    import random
    import utilities as utils
    import point2 as ask
    import helper_functions as helper

    print("Welcome to the quiz!")
    print("You will be asked a series of questions.")
    
    num_of_players = int(input("How many players are there? "))
    
    if num_of_players < 1:
        print("There must be at least one player.")
        exit(1)
    
    scores = {}
    players = []
    counter = 0
    while counter < num_of_players:
        player_name = input(f"Enter the name of player {counter + 1}: ")
        players.append(player_name)
        scores[player_name] = 0
        print(f"Welcome {player_name}! You are Player number {counter + 1}.")
        counter += 1

    print("\nInitial scores:")
    utils.show_scores(scores)
    print("\nThe game is starting!")

    # Number of rounds as specified in the task
    rounds = 3
    
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}!")
        for player in players:
            print(f"\n{player}'s turn!")
            helper.ask_question(player, ask.questions, scores)
            utils.show_scores(scores)
    
    winners = utils.declare_winner(scores)
    if len(winners) == 1:
        print(f"\nCongratulations, {winners[0]}! You won!")
    else:
        print(f"\nIt's a tie! The winners are: {', '.join(winners)}")
    print("Game over!")
    
if __name__ == "__main__":
    start()





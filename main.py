def start():
    import pandas as pd
    import ask as ask

    print("Welcome to the quiz!")
    print("You will be asked a series of questions.")
    
    

    num_of_players = int(input("How many players are there? "))
    
    if num_of_players < 1:
        print("There must be at least one player.")
        exit(1)
    scores = {"name" : 0 }
    counter = 0
    while counter < num_of_players:
        player_name = input(f"Enter the name of player {counter + 1}: ")
        scores[player_name] =  0
        print(f"welcome  {player_name}! you are Player number {counter + 1}.")
        counter += 1

    df_scores = pd.DataFrame(scores, index= [0])
    # show score table

    print(df_scores)
    print("The game is starting!")

    for player in scores.keys():
        ask.ask_question(player)
        ask.show_scores()
    ask.declare_winner(scores)
    print("Game over!")
    
if  __name__ == "__main__":
    start()





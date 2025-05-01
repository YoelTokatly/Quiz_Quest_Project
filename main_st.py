
def ask_question(player, questions, scores):
   import streamlit as st
   import random   
   import pandas as pd
   correct_answer = None

   st.write(f"### {player} Choose a category")  
    # Choose a category
   with st.form(key=f"{player} form_Choose a category"):
        selected_option = st.radio(
            "Choose your answer:",
            ["science", "history", "pop culture"],
            index=None
        )
        
        # Submit button
        submitted = st.form_submit_button("Submit Answer")
        
        if submitted:
            if selected_option is None:
                st.warning("Please select an answer before submitting.")
                return None, None
            
         # Check correctness
            # is_correct = (selected_option == correct_answer) if correct_answer is not None else None
            is_correct = (selected_option != None)
            
            # Display feedback
            if is_correct:
                st.success(f"✅ you chose {selected_option}")                
            # return selected_option, is_correct
        

        question_data = random.choice(questions[selected_option])
#printing the question from the category:
        st.text(question_data["q"])
#asking for answer from the player
        answer = st.text_input("Enter your answer: ").lower()
        if answer == question_data["a"].lower():
            st.text("Correct!")
            scores[player] += 1
            st.text(f"{player}'s score is {scores[player]}")
        else:
            st.text(f"Wrong answer! The correct answer is {question_data['a']}")
        
        st.table(pd.DataFrame(scores.items(), columns=["Player", "Score"]))

        



def start():
    import random
    import utilities as utils
    import point2 as ask
    import helper_functions as helper
    import streamlit as st
    import pandas as pd

    # Set page config
    st.set_page_config(
    page_title="Welcome to the quiz!",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="expanded"
    )

    st.title("🎮 Interactive Quiz Game 🎮")
    st.write("Welcome to the quiz!")
    st.write("You will be asked a series of questions.")
    # print("Welcome to the quiz!")
    # print("You will be asked a series of questions.")
    st.header("Game Setup")
    
    
    with st.form("player_setup_form"):
         st.write("Please enter the number of players and their names.")
         num_of_players = st.number_input("How many players are there?", min_value=1, value=1, step=1)
         submit_button = st.form_submit_button("Continue")
    # num_of_players = int(input("How many players are there? "))

         if submit_button:
            # no need to check if num_of_players < 1, as the number input already does that
            # Reset game state
            st.session_state.players = []
            st.session_state.scores = {}
            
            # get player name 
            st.session_state.num_players = num_of_players
            st.session_state.game_stage = 'collect_names'
            st.rerun()

    if st.session_state.game_stage == 'collect_names':
        with st.form("player_names_form"):
             st.write("Please enter the names of the players.")
             players = []
             scores = {}
             for player in range(num_of_players):
                    player_name = st.text_input(f"Enter the name of player {player + 1}: ")
                    players.append(player_name)
                    scores[player_name] = 0
                    # st.text(f"Welcome {player_name}! You are Player number {player + 1}.")
             start_game = st.form_submit_button("Start Game")
            #  st.session_state.game_stage = 'start_game'
 
 
 
 
    #####game stage: start_game
    if start_game :
        st.table(pd.DataFrame(scores.items(), columns=["Player", "Score"]))
        st.subheader("The game is starting!")
                # Initialize game state
        st.session_state.players = players
        for player in players:
                    st.session_state.scores[player] = 0
                
                # st.session_state.current_round = 1
                # st.session_state.current_player_index = 0
                # st.session_state.question_asked = False
                # st.session_state.game_stage = 'play'
                # st.rerun()
    elif start_game:
                st.error("Please enter names for all players.")
       


    rounds = 1
    
    for round_num in range(1, rounds + 1):
        st.text(f"\nRound {round_num}!")
        for player in players:
            st.text(f"\n{player}'s turn!")
            ask_question(player, ask.questions, scores)
            st.table(pd.DataFrame(scores.items(), columns=["Player", "Score"]))
            # st.selectbox("Next player", options=['yes,no':]], index=0, key=f"next_player_{player}")
            # utils.show_scores(scores)
    
    # winners = utils.declare_winner(scores)
    # if len(winners) == 1:
    #     print(f"\nCongratulations, {winners[0]}! You won!")
    # else:
    #     print(f"\nIt's a tie! The winners are: {', '.join(winners)}")
    # print("Game over!")
    
if __name__ == "__main__":
    start()





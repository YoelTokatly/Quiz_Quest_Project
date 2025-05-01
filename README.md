# Quiz_Quest_Project

# Quiz Quest

## Description
Quiz Quest is an interactive, multi-player quiz game written in Python. Players take turns answering questions from different categories (science, history, and pop culture), earning points for correct answers. The game supports multiple players and runs for a customizable number of rounds, with a winner declared at the end based on the highest score.

## Features
- Multi-player support: Play with friends and family
- Category selection: Choose from science, history, or pop culture questions
- Score tracking: Automatically keeps track of each player's score
- Configurable rounds: Set the number of rounds for shorter or longer games
- Winner declaration: Automatically determines the winner or announces a tie

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/quiz-quest.git

# Navigate to the project directory
cd quiz-quest

# No external dependencies required! The game uses only Python standard libraries
```

## Usage

```bash
# Run the main game file
python main.py
```

Follow the on-screen prompts to:
1. Enter the number of players
2. Provide each player's name
3. Take turns selecting categories and answering questions
4. See the final winner(s) after all rounds are complete

## Project Structure

- `main.py`: Entry point that starts the game and manages the game flow
- `helper_functions.py`: Contains the core game mechanics like asking questions
- `point2.py`: Houses the dictionary of questions for different categories
- `utilities.py`: Helper functions for game initialization, score tracking, and winner declaration

## Customization

You can easily customize the game by:

1. Adding new questions to the categories in `point2.py`
2. Creating new categories by adding them to the `questions` dictionary
3. Adjusting the number of rounds by changing the `rounds` variable in `main.py`

## Contributing
Contributions are welcome! If you'd like to contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements
Special thanks to all collaborators on this project:
- Dikla Buchnik - Core game mechanics and helper functions
- Inna G- Project support and testing
- Lion - Project support and testing
- Yoel- Main game development and coordination

## Contact
- Yoel - [GitHub Profile](https://github.com/YoelTokatly)
- Project Link: [https://github.com/YoelTokatly/Quiz_Quest_Project](https://github.com/YoelTokatly/Quiz_Quest_Project)

## Project Status
This project is currently in active development. Feel free to contribute or suggest improvements!

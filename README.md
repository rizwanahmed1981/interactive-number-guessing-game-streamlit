
---

# Interactive Number Guessing Game with Streamlit

Welcome to the Interactive Number Guessing Game! This application allows users to think of a number within a specified range, and the computer attempts to guess it based on user feedback. Built with Python and Streamlit, this game offers an engaging experience demonstrating the power of interactive web applications.

## Features

- **Interactive Gameplay**: The computer guesses the number you're thinking of, adjusting its guesses based on your feedback.
- **User-Friendly Interface**: Leveraging Streamlit's intuitive design for seamless interaction.
- **Dynamic Feedback**: Users provide real-time feedback to guide the computer's guesses.

## How to Play

1. **Start the Game**: Launch the application, and you'll be prompted to think of a number within a specified range (e.g., 1 to 100).
2. **Computer's Guess**: The computer will make an initial guess.
3. **Provide Feedback**:
   - Indicate if the computer's guess is too high, too low, or correct.
4. **Continue**: Based on your feedback, the computer will adjust its next guess.
5. **Game Over**: The game concludes when the computer correctly guesses your number.

## Installation

To run this application locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/rizwanahmed1981/interactive-number-guessing-game-streamlit.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd interactive-number-guessing-game-streamlit
   ```

3. **Create a Virtual Environment**:

   ```bash
   uv venv
   ```

4. **Activate the Virtual Environment**:

   - On Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source env/bin/activate
     ```

5. **Install Dependencies**:

   ```bash
   uv add -r requirements.txt
   ```

6. **Run the Application**:

   ```bash
   uv run streamlit run game.py
   ```

   This command will open the application in your default web browser.

## Dependencies

- **Python**: Ensure you have Python installed (version 3.7 or higher recommended).
- **Streamlit**: For creating the interactive web interface.
- **Random**: To generate random numbers for the guessing logic.

## Contributing

Contributions are welcome! If you'd like to enhance the game or fix issues:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Description of changes"
   ```

4. Push to the branch:

   ```bash
   git push origin feature-name
   ```

5. Open a Pull Request detailing your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Inspired by classic number guessing games and the desire to create an interactive web application using Streamlit.

---


Best regards,

# [Rizwan Ahmed] 
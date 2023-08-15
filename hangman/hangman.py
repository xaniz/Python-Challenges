# _    _                                         
#| |  | |                                        
#| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
#|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
#| |  | | (_| | | | | (_| | | | | | | (_| | | | |
#|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                    __/ |                      
#                    |___/  


# Import necessary modules
import random
import words
import drawings

# Choose a random word from the word list
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)  # Calculate the length of the chosen word
lives = 6  # Initialize the number of lives
end_of_game = False  # Flag to determine if the game has ended

# Create a list of underscores to represent the display
display = ['_' for _ in range(word_length)]

# Main game loop
while '_' in display and not end_of_game:
    if lives == 0:
        print("Game over")
        end_of_game = True
        break

    guess = input("Guess a letter: ").lower()  # Ask for player's guess
    correct_guess = False  # Initialize a flag for correct guesses
            
    # Check each position in the chosen word
    for i in range(word_length):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
            correct_guess = True
    
    # If guess is incorrect, decrement lives and display hangman drawing
    if not correct_guess:
        lives -= 1
        print(drawings.stages[lives])
    
    print(display)  # Display the current progress
    
# Check if the player has guessed all letters
if '_' not in display:
    print("You win")
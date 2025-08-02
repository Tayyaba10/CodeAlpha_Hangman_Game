# This is a simple hangman game implementation in Python.
import random
import string

# word list for the game
words = ["python", "java", "kotlin", "javascript", "hangman", "programming", "computer", "science", "developer", "software", "engineer", "algorithm", "data", "structure", "function", "variable", "object", "class", "inheritance", "polymorphism"]

def get_random_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_random_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_lowercase)
    guessed_letters = set()
    lives = 8
    
    # loop until the word is guessed or lives run out
    while len(word_letter) > 0 and lives > 0:
        
        print(f"\nYou have {lives} Lives left.")
    
        print("\nYou have used these letters:", " ".join(guessed_letters))
    
        word_display = [letter if letter in guessed_letters else "-" for letter in word]
        print("Current word:", " ".join(word_display))
    
        user_letter = input("\nGuess a letter: ").lower()

        # check if the input is a single letter
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            
            # check if the letter is in the word
            if user_letter in word_letter:
                word_letter.remove(user_letter)
                print("Good guess!")
                
            # check if the letter is not in the word
            else:
                lives -=  1
                print("Letter is not in the word.")
                
        # check if the input is a letter
        elif user_letter in guessed_letters:
            print("You have already guessed that letter. Please try again.")
            
        else:
            print("Invalid character. Please enter a letter from A-Z.")
            
    # check if the user has run out of lives
    if lives == 0:
        print(f"\nYou died with the word {word} in your mind.")
    else:
        print(f"\nCongratulations! You guessed the word {word} correctly.")

if __name__ == "__main__":
    print("\033[1;3m Welcome to Hangman! \033[0m")
    print("Try to guess the word before you run out of lives.")
    print("You have 8 lives to guess the word.")
    
    hangman()
    # check if the user wants to play again or not
    while True:
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "Y":
            hangman()
        elif play_again == "N":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please enter Y or N.")
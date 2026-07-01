import random

def hangman():
    # List of predefined words
    words = ["python", "gemini", "developer", "challenge", "coding"]

    # Randomly select a word
    word = random.choice(words)

    # Create hidden word with underscores
    guessed_word = ["_"] * len(word)

    # Variables
    incorrect_guesses = 0
    guessed_letters = []
    max_incorrect_guesses = 6

    # Welcome Message
    print("=" * 40)
    print("🎮 Welcome to Hangman Game!")
    print("=" * 40)
    print("Guess the word one letter at a time.\n")

    # Show hidden word
    print("Word:", " ".join(guessed_word))

    # Main Game Loop
    while incorrect_guesses < max_incorrect_guesses and "_" in guessed_word:

        print("\nIncorrect guesses left:", max_incorrect_guesses - incorrect_guesses)
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) if guessed_letters else "None")

        # Take user input
        guess = input("\nEnter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter only one alphabet letter.")
            continue

        # Check already guessed
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Correct Guess
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess

            print("✅ Correct Guess!")

        # Wrong Guess
        else:
            incorrect_guesses += 1
            print("❌ Wrong Guess!")

        # Show current word after every guess
        print("\nCurrent Word:")
        print(" ".join(guessed_word))
        print("-" * 40)

    # Final Result
    print("\n" + "=" * 40)

    if "_" not in guessed_word:
        print("🎉 Congratulations!")
        print("You guessed the word:", word)
    else:
        print("😢 Game Over!")
        print("The correct word was:", word)

    print("=" * 40)


# Run Program
if __name__ == "__main__":
    hangman()
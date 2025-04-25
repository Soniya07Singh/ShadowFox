import random

# Word list with hints
words_with_hints = {
    "elephant": "A large animal with a trunk.",
    "python": "A popular programming language.",
    "guitar": "A string musical instrument.",
    "ocean": "A large body of salt water.",
    "chocolate": "A sweet treat made from cocoa.",
    "umbrella": "Used to protect from rain.",
    "bicycle": "A two-wheeled mode of transport.",
    "mountain": "A large natural elevation of the earth's surface.",
}

# Hangman visual stages
hangman_stages = [
    """
     _______
    |       |
    |       
    |      
    |      
    |      
    |_____
    """,
    """
     _______
    |       |
    |       O
    |      
    |      
    |      
    |_____
    """,
    """
     _______
    |       |
    |       O
    |       |
    |      
    |      
    |_____
    """,
    """
     _______
    |       |
    |       O
    |      /|
    |      
    |      
    |_____
    """,
    """
     _______
    |       |
    |       O
    |      /|\\
    |      
    |      
    |_____
    """,
    """
     _______
    |       |
    |       O
    |      /|\\
    |      / 
    |      
    |_____
    """,
    """
     _______
    |       |
    |       O
    |      /|\\
    |      / \\
    |      
    |_____
    """,
]

MAX_TRIES = len(hangman_stages) - 1

def play_hangman():
    word, hint = random.choice(list(words_with_hints.items()))
    guessed_letters = []
    wrong_guesses = 0
    word_display = ["_" for _ in word]

    print("\n🎯 Welcome to Hangman!")
    print(f"💡 Hint: {hint}")

    while wrong_guesses < MAX_TRIES and "_" in word_display:
        print(hangman_stages[wrong_guesses])
        print("Word: " + " ".join(word_display))
        print(f"Guessed Letters: {', '.join(guessed_letters)}")
        guess = input("🔤 Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❗ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
            for i, char in enumerate(word):
                if char == guess:
                    word_display[i] = guess
        else:
            print("❌ Wrong guess!")
            wrong_guesses += 1

    # Final Game State
    print(hangman_stages[wrong_guesses])
    if "_" not in word_display:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("💀 Game Over! The correct word was:", word)

# Main loop to replay
play_more = True
while play_more:
    play_hangman()
    again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
    if again == 'no':
        print("👋 Thanks for playing Hangman!")
        play_more = False

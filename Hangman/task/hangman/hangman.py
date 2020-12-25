import random

print("H A N G M A N")
while True:
    choice = input('Type "play" to play the game, "exit" to quit:')
    if choice == "exit":
        break
    elif choice == "play":
        words = ['python', 'java', 'kotlin', 'javascript']
        word = random.choice(words)
        guessed_word = ["-" for i in range(len(word))]

        updated_word = list(word)

        guessed_letters = []
        chances = 8
        while chances > 0:
            print("\n", "".join(guessed_word))
            guess = input("Input a letter:")
            if len(guess) != 1:
                print("You should input a single letter")
            elif not guess.islower():
                print("Please enter a lowercase English letter")
            else:
                if guess in updated_word:
                    for i in range(len(word)):
                        if guess == updated_word[i]:
                            guessed_word[i] = updated_word[i]
                            updated_word[i] = "-"
                elif guess in word or guess in guessed_letters:
                    print("You've already guessed this letter")
                else:
                    print("That letter doesn't appear in the word")
                    chances = chances - 1
                guessed_letters.append(guess)
            if "".join(guessed_word) == word:
                break

        if "".join(guessed_word) == word:
            print("You survived!\n")
        else:
            print("You lost!\n")

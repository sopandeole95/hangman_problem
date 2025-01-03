import hangman_art

import random

import hangman_words

print(hangman_art.logo)



chosen_word = random.choice(hangman_words.word_list)

word_length = len(chosen_word)



end_of_game = False

lives = 6



#Create blanks

display = []

for _ in range(word_length):

    display += "_"



while not end_of_game:

    guess = input("Guess a letter: ").lower()



    for position in range(len(display)):

      if guess == display[position]:

        print(f"You've already guessed {guess}")

    #Check guessed letter

    for position in range(word_length):

        letter = chosen_word[position]

        if letter == guess:

            display[position] = letter



    #Check if user is wrong.

    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word and you lose a life")

        lives -= 1

        if lives == 0:

            end_of_game = True

            print("You lose.")

    print(f"{' '.join(display)}")



    #Check if user has got all letters.

    if "_" not in display:

        end_of_game = True

        print("You win.")



    print(hangman_art.stages[lives])
#Step 1
import random
from hangman_words import word_list
from hangman_art import logo, stages

# input _

guesses = []
chosen_word = random.choice(word_list)
print(logo)
lives = 6
display = []
word_len = len(chosen_word)

for character in range(word_len):
  display += '_'

while '_' in display:
  print(f"{' '.join(display)}\n")
  guess = input('Guess: \n')
  guesses += guess

  if guess in display:
    print("You already said that")

  for i in range(word_len):
    if guess == chosen_word[i]:
      display[i] = chosen_word[i]

  if guess not in chosen_word:
    lives -= 1
    print(f"Your guess was: {guess}")
    print(stages[lives])

  if lives == 0:
    print(f"you lose :(, this was the word: {chosen_word}")
    quit()

  if not '_' in display:
    print("Congrats you've won!")

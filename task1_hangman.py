import random
words = ["python", "apple", "mango", "school", "laptop"]
word = random.choice(words)
guessed = []
lives = 6
while lives > 0:
    display = [l if l in guessed else "_" for l in word]
    print(" ".join(display))
    print(f"Lives: {lives}")
    if "_" not in display:
        print("You won! Great job!")
        break
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print("Already guessed!")
        continue
    guessed.append(guess)
    if guess not in word:
        lives -= 1
        print(f"Wrong! Lives left: {lives}")
if lives == 0:
    print(f"Game over! Word was: {word}")

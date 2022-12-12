#Building a number guessing game 
#When number is guessed should give a measure of how accurate the guess is
# Whether guess is higher or lower than number
import random 


NUMBER = random.randrange(1, 9)



guess_count = 0
guess_limit = 3
print("GUESSING GAME\n\n")
while guess_count < guess_limit:
    guess = int(input("Guess the number.\n\n"))
    guess_count += 1

    if guess == NUMBER:
        print("You guessed the number!")
        break
    elif guess > NUMBER:
       print("Lower...")

    elif guess < NUMBER:
        print("Upper...")

    
else:
    print("Sorry You failed.\n\n")
    print("Number was", NUMBER)


    
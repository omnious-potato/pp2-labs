import random
number = random.randrange(1, 20)

print("Hello! What's your name?")
name = input()
print(f"Well, {name}, I am thinking of a number between 1 and 20.")    

counter = 0
while(True):    
    print("Take a guess.")
    current_guess = int(input())
    counter += 1

    if(current_guess < number):
        print("Your guess is too low.")
    if(current_guess > number):
        print("Your guess is too high.")
    
    if(current_guess == number):
        print(f"Good job, {name}! You guessed my number in {counter} guesses!")
        break
    
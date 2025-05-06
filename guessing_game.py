import random

print("*** Number Guessing Game ***\n");

secret_number = random.randint(1, 100);
#print(secret_number); #debug only

print("The computer has generated a random number between 1 and 100.");
print("Try to guess what number was generated to win!\n");

correctGuess = False;
attempt_count = 0;

while correctGuess != True:
    try:
        numGuess_str = input("Enter a number (1 - 100): ");
        numGuess = int(numGuess_str);
        
        attempt_count += 1; #add a count to attempts tried
        
        if numGuess < secret_number: #if guess is to low
            print("Too low!\n");
        elif numGuess > secret_number: #if guess is to high
            print("Too high!\n");
        elif numGuess == secret_number: #if guess is correct
            print("Correct! You win!\n");
            print(f"You found the number in {attempt_count} tries!");
            correctGuess = True;
    except ValueError:
        print("Error, only enter numbers!\n");

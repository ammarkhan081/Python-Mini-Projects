import random
top_of_range=input("Enter range:")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("Enter number greater than 0")
        quit()
else:
    print("Enter correct number")
    quit()

random_number=random.randrange(1,top_of_range)
guesses=0
while True:
    guesses+=1
    user_input=input("Enter your guess: ")
    if user_input.isdigit():
        user_input=int(user_input)
    else:
        print("Please enter a number next time ")
        continue
    if random_number==user_input:
        print("You got it")
        break
    elif user_input>random_number:
        print("you enter above the number")
    else:
        print("You enter below the number")

print(f"You got number in {guesses} guesses")

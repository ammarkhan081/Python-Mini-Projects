name=input("Enter Your Name:")
print(f"Welcome to such a good adventure {name} ")

answer=input("You are on the dirt road, it has come to an end and you can go left/right. Which way would you like to go?: ").lower()
if answer.lower()=="left":
    answer=input("You come to a river, you can walk around it or swim across? Please enter (walk/swim) ")
    if answer.lower()=="walk":
        print("You walk for many miles, ran out from water and you lost the game")
    elif answer.lower()=="swim":
        print("You swim across and eaton by alligator")
    else:
        print("Not a valid option. You lose ")

elif answer.lower()=="right":
    answer=input("You come to a bridge, it looks wobbly, do you to cross it or head back? Please enter (cross/head back): ")
    if answer.lower()=="cross":
        answer=input("You cross a stranger an met a stranger, did you want to talk with them? Please enter (Yes/No): ")
        if answer.lower()=="yes":
            print("You talk to stranger and they give you gold and you won")
        elif answer.lower()=="no":
            print("You ignored the stranger and they offended you and you lose")
        else:
            print("Not a valid option. You lose ")
    elif answer.lower()=="head back":
        print("You head back and lost the game")
    else:
        print("Not a valid option. You lose ")
else:
    print("Not a valid option. You lose ")

name = input("Enter Your Name: ")
print(f"Welcome to the enchanted forest, {name}! Your journey begins now.")

answer = input("You find yourself at a crossroads in the forest. Do you want to follow the path lit by glowing mushrooms or the one covered in mist? Please enter (mushrooms/mist): ").lower()
if answer == "mushrooms":
    answer = input("The glowing mushrooms lead you to a hidden waterfall. Do you want to explore behind the waterfall or continue along the path? Please enter (explore/continue): ").lower()
    if answer == "explore":
        print("Behind the waterfall, you discover a hidden cave filled with ancient treasures. You take a piece of gold and win!")
    elif answer == "continue":
        print("You continue along the path but soon find yourself lost in the dark forest. Unfortunately, you lose your way and the adventure ends here.")
    else:
        print("Not a valid option. You lose.")

elif answer == "mist":
    answer = input("The misty path takes you to a mysterious tower. Do you want to enter the tower or walk around it? Please enter (enter/walk around): ").lower()
    if answer == "enter":
        answer = input("Inside the tower, you find a spiral staircase leading up. Do you climb the stairs or search the ground floor? Please enter (climb/search): ").lower()
        if answer == "climb":
            print("At the top of the tower, you find a magical book that grants you wisdom and power. You win!")
        elif answer == "search":
            print("As you search the ground floor, a trapdoor opens beneath you, and you fall into a pit. The adventure ends here.")
        else:
            print("Not a valid option. You lose.")
    elif answer == "walk around":
        print("As you walk around the tower, you stumble upon a hidden garden filled with enchanted creatures. They guide you out of the forest safely. You win!")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")




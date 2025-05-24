import random
user_win=0
comp_win=0
draw=0
options=["rock","paper","scissors"]
while True:
    user=input("Enter rock/paper/scissors or q for quit:")
    if user.lower()=="q":
        break
    if user not in options:
        continue
    random_num=random.randint(0,2)
    comp=options[random_num]
    print(comp)
    if comp==user:
        print("Draw")
        draw+=1
    elif comp=="paper" and user=="rock":
        print("comp won")
        comp_win+=1
    elif comp=="scissors" and user=="paper":
        print("comp won")
        comp_win+=1
    elif comp=="rock" and user=="scissors":
        print("comp won")
        comp_win+=1
    else:
        print("User won")
        user_win+=1

print("user win ",user_win)
print("comp win ",comp_win)
print("draw",draw)
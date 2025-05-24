from cryptography.fernet import Fernet
def view():
    with open("Password.txt","r") as f:
        for line in f.readlines():
            print(line.rstrip())

def add():
    name=input("Enter Name: ")
    password=input("Enter Password: ")

    with open("Password.txt","a") as f:
        f.write("Name: "+name+" Password: "+password+" \n")

while True:
    mode=input("Would you like to add new password/view an existing one/Quit? Please enter one of them (add/view/q): ")
    if mode=="q":
        break
    elif mode=="add":
        add()
    elif mode=="view":
        view()
    else:
        print("Invalid Input")
        continue
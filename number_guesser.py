import random
art = """
 _      _     _      ____  _____ ____    _____ _     _____ ____  ____  _____ ____ 
/ \  /|/ \ /\/ \__/|/  _ \/  __//  __\  /  __// \ /\/  __// ___\/ ___\/  __//  __\
| |\ ||| | ||| |\/||| | //|  \  |  \/|  | |  _| | |||  \  |    \|    \|  \  |  \/|
| | \||| \_/|| |  ||| |_\\|  /_ |    /  | |_//| \_/||  /_ \___ |\___ ||  /_ |    /
\_/  \|\____/\_/  \|\____/\____\\_/\_\  \____\\____/\____\\____/\____/\____\\_/\_\
                                                                                  
"""
print(art)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
diff = input("Choose a difficulty. Type 'easy' or 'hard': ")

cont = True 
attepmts = 0

if diff == "hard":
    attepmts = 5
elif diff == "easy":
    attepmts = 10
print(f"You have {attepmts} remaining to guess a number")


cpu_number = random.randint(1, 101)


def guessing():
    global attepmts
    global cont
    if attepmts == 0:
            print("You lost")
            cont = False
            return
    st_user_guess = input("Make a guess: ")
    user_guess = int(st_user_guess)
    if user_guess == cpu_number:
        print("You win!")
        cont = False
        return;
    else:
        attepmts -= 1
        if user_guess < cpu_number:
            print("Too low.")
        else:
            print("Too high.")
        print(f"You have {attepmts} remaining to guess a number")

while cont:
    guessing()
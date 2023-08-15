rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

option_list = [rock, paper, scissors]
#Getting players input
human_input = input("Rock 0, Paper 1 or Scissors 2 ?")
human = int(human_input)

if human == 0 or human == 1 or human == 2:
    print(option_list[human])
else:
    print("Options are 0, 1 or 2")
    
#Getting CPU input
cpu = random.randint(0, 2)
print(option_list[cpu])
    
#Game logic
if (human == 0 and cpu == 0) or (human == 1 and cpu == 1) or (human == 2 and cpu == 2):
    print("It's a draw")
elif (human == 1 and cpu == 0) or (human == 0 and cpu == 2) or (human == 2 and cpu == 1):
    print("You win")
elif (human == 0 and cpu == 1) or (human == 2 and cpu == 0) or (human == 1 and cpu == 2):
    print("You lose")
    
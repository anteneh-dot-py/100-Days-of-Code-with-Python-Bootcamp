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
import random

game_choice =[rock,paper,scissors]
user_choice=int(input("Choose one: 1.rock 2.paper 3.scissors"))-1
computer_choice=random.randint(0,len(game_choice)-1)

print(f"you choose {game_choice[user_choice]}")
print(f"computer choice{game_choice[computer_choice]}")
if user_choice==computer_choice:
      print("Draw")
elif (user_choice==0 and computer_choice==2) or (user_choice==2 and computer_choice==1) or (user_choice==1 and computer_choice==0):
    print("You win")

else:
       print("Computer wins")
        

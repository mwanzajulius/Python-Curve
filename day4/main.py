#Randomization
import random
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
game_images=[rock,paper,scissors]
print("Welcome to Rock, Paper, Scissors.")
user_choice=int(input("Choose 0 for rock, 1 for paper, 2 for scissors:"))
if user_choice>=0 and user_choice<=2:
    print(game_images[user_choice])
computer_choice=random.randint(0,2)
if computer_choice>=0 and computer_choice<=2:
    print(game_images[computer_choice])
if user_choice==computer_choice:
    print("It's a tie!")
elif user_choice==0 and computer_choice==1:
    print("Paper beats rock. You lose!")
elif user_choice==1 and computer_choice==2:
    print("Scissors beats paper. You lose!")
elif user_choice==2 and computer_choice==0:
    print("Rock beats scissors. You lose!")
elif user_choice==0 and computer_choice==2:
    print("Scissors beats rock. You win!")
elif user_choice==1 and computer_choice==0:
    print("Paper beats rock. You win!")
elif user_choice==2 and computer_choice==1:
    print("Scissors beats paper. You win!")
else:
    print("Invalid choice. Try again.!")
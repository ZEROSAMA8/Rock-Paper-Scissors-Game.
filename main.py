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
print("Wlecom to rock paper scissoers game :))))))")
game =[rock,paper,scissors] 
ask = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n "))
if ask >=3:
  print("You typed an invalis number, You lost!")
else:
 print(game[ask])

 compu_cho = random.randint(0,2)
 print("Computer chose:\n")
 print(game[compu_cho])
# if ask >=3:
#   print("You typed an invalis number, You lost!")
 if ask ==0 and compu_cho ==2:
  print("Congratulations ::)))))), You won this game.\n Would you like to play with me again? I will win this time ;")
 elif compu_cho==0 and ask==2:
  print("You lost this game:(( Would you like to play again?")
 elif compu_cho > ask:
  print("You lost this game:(( Would you like to play again?")
 elif ask > compu_cho:
  print("Congratulations ::)))))), You won this game.\n Would you like to play with me again? I will win this time ;")
 elif compu_cho == ask :
  print("You Draw with Computer.")

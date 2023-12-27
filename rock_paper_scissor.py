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
choice=input("Choose rock, paper or scissor \t")
rpclist=["rock","paper","scissors"]
choice_index=rpclist.index(choice)
mylist=[rock,paper,scissors]
print("You choose"+mylist[choice_index])
compchoice=random.choice(mylist)
print("The computer choose \n"+compchoice)
compchoice_index=mylist.index(compchoice)
if choice_index==0 and compchoice_index==2:
      print("You win")

elif choice_index>compchoice_index:
   print("You win")

elif choice_index==compchoice_index:
     print("Its a draw")
else:
     print("You lose")      
      
   

# -*- coding: utf-8 -*-
"""rock_paper_scissors.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HbN1Dni5iJa2LqwEqr-8m_-6oMykBohg
"""

import random 

def play():

  user = input ("'r' for rock,  'p' for paper, 's' for scissors: ")
  liste = ["r","p","s"]

  i = random.randint(0,2)
  computer = liste[i]

  if user == "r": 
    if computer == "p":
      print("Computer chose paper", "\n", "You lose")
    elif computer == "s":
      print("Computer chose scissors", "\n", "You win!")
    else:
      print("Computer also chose rock", "It's a tie")

  elif user =="p":
    if computer == "p":
      print("Computer also chose paper", "\n", "It's a tie")
    elif computer == "s":
      print("Computer chose scissors", "\n", "You lose")
    else:
      print("Computer chose rock", "You win!")


  else:
    if computer == "p":
      print("Computer chose paper", "\n", "You win!")
    elif computer == "s":
      print("Computer chose scissors", "\n", "It's  tie")
    else:
      print("Computer also chose rock", "You lose")

play()

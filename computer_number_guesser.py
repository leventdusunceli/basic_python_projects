#In this function the user picks a number in a range that they define as the input of the function

def computer_guess (x,i):
  high = i 
  low =  x
  print(f"Ok, pick a number between {low} and {high}", "\n")
  guess_feedback = ""
  tries = 0 
  while guess_feedback != "correct":

    if low != high:
      guess = random.randint(low,high)

    else:
      guess = low

    guess_feedback = input(f"Is your number {guess}? Type correct ,too high or too low : ").lower()
    if guess_feedback == "too high":
      high = guess-1
      tries += 1
      print("ok, I'll try again","\n")
    elif guess_feedback == "too low":
      low = guess +1
      tries += 1
      print("ok, I'll try again" ,"\n" )

  tries += 1 
  print(f"Bingo! It only took me {tries} tries!")

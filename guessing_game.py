import random

class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
        self.last_guess  = None
        self.last_result = None

    def guess(self, last_guess):
        self.last_guess = last_guess

        if self.last_guess > self.answer:
            return 'High'
        elif self.last_guess < self.answer:
            return 'Low'
        return 'Correct'


    def solved(self):
        return self.last_guess == self.answer
        
game = GuessingGame(random.randint(1,100))


while game.solved() == False:
   
  game.last_guess  = input("Enter your guess: ")
  try: 
    game.last_guess = int(game.last_guess)
  except Exception:
    print('Not an integer.')
  
  game.last_result = game.guess(game.last_guess)
  print(game.last_result)

  if(game.solved() == True):
    print(f"{game.last_guess} was correct!")



import random
import os
import re


def check_play_status():
  valid_responses = ['yes', 'no', 'y']
  while True:
      try:
          response = input('Do you wish to play again? (Yes or No): ')
          if response.lower() not in valid_responses:
              raise ValueError('Yes or No only')

          if response.lower() == 'yes':
              return True
          elif response.lower() =='y':
              return True
          else:
              os.system('cls' if os.name == 'nt' else 'clear')
              print('Thanks for playing!')
              print(f'Final Score - You: {user_score}, Computer: {computer_score}')
              exit()

      except ValueError as err:
          print(err)

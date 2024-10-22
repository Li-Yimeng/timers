import time 
from PIL import Image # the pillow library makes it easy to display images 
import random

# Game starts
print('Players stand')

# Initialize variables
im = Image.open("times-up.jpeg")
sleep_time = random.randint(10,25)
sat_down_players = []
start_time = time.time()
remaining_time = sleep_time

# Program sleeps
while remaining_time >0: 
    player_name = str(input('Please enter the name of sat down player:'))
    if player_name: 
        sat_down_players.append(player_name)
    times = time.time() - start_time
    remaining_time = sleep_time - int(times)
    
im.show()

if sat_down_players:
    winner = sat_down_players[-1]
    print(f'The winner is: {winner}')
else: 
    print('All players are standing. No one wins')
    
    

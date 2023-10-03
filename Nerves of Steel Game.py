# This program is for the "Nerves of Steel" Party game

# Display "Players Stand"
print ("Players Stand")


# This program is timer that counts down


import time # The time library has a sleep function that will pause the script for a specifized amount of time

# Import Random Module
import random

# Generate a random timer between 5 and 25 seconds
set_time = random.randint(5, 25)

time.sleep(set_time)

# Display "Time Up. Last to sit down wins." after the randomized time
print("Time Up. Last to sit down wins.")
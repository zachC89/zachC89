#First project: Project XP leveling System

#Part 1.) Global Player stats and the only global variables we are using in this scenario
player_level = 1
player_xp = 0
xp_per_level = 100

#Part 2.) Calculating the player's xp
def calculate_total_xp(level, xp):
    total_xp = level + xp
    return total_xp

#Part 3.) Showing the amount of XP gained
def gain_xp(amount):
    global player_xp, player_level #Need to add global to modify global variables above outside the function
    player_xp = player_xp + amount

    print(f"You gained {amount} XP!")

    #Now we add a loop for the Level-up part (handles multiple levels at once)
    while player_xp >= xp_per_level:
        player_xp-= xp_per_level
        player_level += 1
        print(f"Congratulations! You leveled up! You are now level {player_level}!")

    print(f"Current XP: {player_xp} XP")
    return player_xp, player_level

#Part 4.) Showing off the player's stats
#This function is showing the player's stats from their current level, xp they currently have and xp needed for the next level up
def show_stats():
    print(f"Level: {player_level}")
    print(f"XP: {player_xp}")
    print(f"XP needed for the next level: {xp_to_next_level()}") #This shows how much XP they need to level up

#Bonus Functions
#This function is telling the player how much xp they will need to reach the next level
def xp_to_next_level():
    xp_required = xp_per_level - player_xp
    return  xp_required

#Battle simulator without import random, lists dictionaries, and external files
def simulate_battle():
    print("The Minotaur is here!")
    print("You strike the Minotaur with multiple strikes!")
    print("You have slain the mighty beast!")
    global player_level
    xp_reward = (player_level *12) * 5 + 20
    print(xp_reward)
    return xp_reward

#The next 2 def simulate_battle are just copy and paste from the first one and used different printing for each new boss monster
def simulate_battle1():
    print("The ugly Hydra makes an attempt to bite you!")
    print("You dodge and then crush the hydra with a heavy boulder!")
    print("The multi-headed monster is now crushed!")
    global player_level
    xp_reward = (player_level *12) * 10 + 20
    print(xp_reward)
    return xp_reward


def simulate_battle2():
    print("The mighty Zeus has appeared!")
    print("You attack Zeus with all of your might!")
    print("You have defeated the strongest Olympian God!")
    global player_level
    xp_reward = (player_level *12) * 15 + 20
    print(xp_reward)
    return xp_reward


#Part 5.) Main Program Flow
#Here are 3 calls to each battle above. This also shows that the exp rewards grow exponentially after each battle
#This is the first project base here and the next ones will build on top of it but this is just the build blocks for it
gain_xp(simulate_battle())
show_stats()

gain_xp(simulate_battle1())
show_stats()

gain_xp(simulate_battle2())
show_stats()

#Key Takeaways:
#This Project Is a Perfect Stepping Stone
#Right now this is a mini‑engine that will be built overtime(long term project):

#global state

#XP math

#leveling logic

#helper functions

#battle simulations

#modular structure

#clean output

#no imports, no shortcuts
#First project: Project XP leveling System version 2.0
#Version 2.0 has V1.0 notes removed and new notes for this specific version only

player_level = 1
player_xp = 0
xp_per_level = 100
max_hp = player_level * 25
player_hp = max_hp
#Added two new variables because I'm going to add healing/resting in the battles
#Want max_hp for the player to be easy to read and have linear scaling per level up
resting = False

def calculate_total_xp(level, xp):
    total_xp = level + xp
    return total_xp

#Updated max_hp in is function to scale max hp while the player levels up
def gain_xp(amount):
    global player_xp, player_level, max_hp
    player_xp += amount

    #added in place operators to clean up code

    print(f"You gained {amount} XP!")

    while player_xp >= xp_per_level:
        player_xp -= xp_per_level
        player_level += 1
        max_hp = player_level * 25
        print(f"Congratulations! You leveled up! You are now level {player_level}!")

    print(f"Current XP: {player_xp} XP")
    return player_xp, player_level, max_hp



def show_stats():
    print(f"Level: {player_level}")
    print(f"XP: {player_xp}")
    print(f"XP needed for the next level: {xp_to_next_level()}")


def xp_to_next_level():
    xp_required = xp_per_level - player_xp
    return  xp_required


def calculate_damage():
    base_damage = 20
    crit_chance = base_damage * 0.2
    total_damage_dealt = (base_damage + crit_chance) * (player_level + 1)
    return total_damage_dealt
#The purpose of this function is to have a battle function that scales linear to the player's level
#I want the numbers to reflect a more realistic RPG battle system

#Damage meter function
def format_damage(damage):
    return f"{damage:_}"
                    #:_ is a format specifier that tells python to put an underscore after every 3 numbers
                    #example instead of 3,000,000 python will print 3_000_000 which is cleaner code to read

#Adding a healing function so if the player takes damage they can heal and head back out to battle
#Had trouble with this particular function due to adding nested if statements
#Purpose of this function is to also scale max hp healing with each level and give flat healing to player after each battle
#Learned importance of *indentation placements here* spaces/indentations really matter
#This is so far the most complicated function in this project for me, hence the difficulty....
def heal():
    global player_hp, max_hp
    if resting:
        if player_hp == max_hp:
            print(f"You are already at full health time. Head out to battle!")
            return max_hp
        else:
            print(f"You need to recover some health!")
            healing = 20
            new_hp = player_hp + healing
            print(f"After resting for 5 seconds you recovered {healing} hp.")

            if new_hp > max_hp:
                new_hp = max_hp
            player_hp = new_hp
            print(f"You now have {player_hp} hp and are ready to fight again!")
            return new_hp
    #player isn't resting = not resting
    if player_hp == max_hp:
        print(f"You are already at full health. Time to fight!")
        return player_hp
    else:
        print(f"You heal as you make your way between battles.")
        healing = 20
        new_hp = player_hp + healing
        print(f"You make your way to a safe area for a little bit to recover some hp.")
        print(f"After 5 seconds you recovered {healing} hp.")

        if new_hp > max_hp:
            new_hp = max_hp

        player_hp = new_hp
        print(f"You now have {player_hp} hp and are ready to get back into battle!")
        return player_hp


#V2.0 Updated battle simulator with damage function added to it
#V2.0 also updated final print statement to look more professional and clean
#V2.0 battle simulator has a damage meter that prints big numbers cleanly ex. player does 2,500, python prints 2_500
#V2.0 Has Conditional Battle outcomes using logical Operators
#Battles 1 and 3 don't have global player_level because I don't need it here since we aren't modifying it
#I kept it in battle 2 for V2.0 for personal reasons since it's still new but will be removed in future updates
def simulate_battle():
    print("The Minotaur is here!")
    print("You strike the Minotaur with multiple strikes!")
    damage = calculate_damage()
    pretty_damage = format_damage(int(damage))
    print(f"You dealt {pretty_damage} damage!")
    print("You have slain the mighty beast!")
    xp_reward = (player_level *12) * 5 + 20
    print(f"Defeating the Minotaur gave you {xp_reward} xp")
    return xp_reward

#Moved global player_level to top of the function because I call player_level in an if/else statement
#global player_level was lower in V1.0 which was fine but for V2.0 it needed to be moved to the top to work properly
def simulate_battle1():
    print("The ugly Hydra makes an attempt to bite you!")
    if player_level <= 1:
        print("You dodge and then crush the hydra with a heavy boulder!")
    else:
        print(f"The Hydra bites your head and you are now dead!")
        print(f"You gained no xp since you died. Cme back STRONGER!")
        return 0

    damage = calculate_damage()
    pretty_damage = format_damage(int(damage))
    print(f"You dealt {pretty_damage} damage to the multi-headed monster!")
    print("The Hydra monster is now crushed!")
    xp_reward = (player_level *12) * 10 + 20
    print(f"Killing the Hydra has rewarded you {xp_reward} xp.")
    return xp_reward

#This battle is adding a Conditional battle outcome to which the player is too low of a level and gets 0 xp
def simulate_battle2():
    print("The mighty Zeus has appeared!")
    if player_level < 4:
        print(f"The God of the Sky's mere presence shakes your very core and you flee!")
        print(f"Running away has granted you 0 xp.")
        return 0

    print("You attack Zeus with all of your might!")
    damage = calculate_damage()
    pretty_damage = format_damage(int(damage))
    print(f"You struck {pretty_damage} damage to the mighty God!")
    print("You have defeated the strongest Olympian!")
    xp_reward = (player_level *12) * 15 + 20
    print(f"Defeating Zeus gave you {xp_reward} xp.")
    return xp_reward

print(f"Hp after healing: {player_hp}")
gain_xp(simulate_battle())
show_stats()
player_hp = heal()

print(f"Hp after healing: {player_hp}")
gain_xp(simulate_battle1())
show_stats()
player_hp = heal()

print(f"Hp after healing: {player_hp}")
gain_xp(simulate_battle2())
show_stats()
player_hp = heal()
player_level = 1
player_xp = 0
xp_per_level = 100


def calculate_total_xp(level, xp):
    total_xp = level + xp
    return total_xp


def gain_xp(amount):
    global player_xp, player_level
    player_xp = player_xp + amount

    print(f"You gained {amount} XP!")

    while player_xp >= xp_per_level:
        player_xp-= xp_per_level
        player_level += 1
        print(f"Congratulations! You leveled up! You are now level {player_level}!")

    print(f"Current XP: {player_xp} XP")
    return player_xp, player_level


def show_stats():
    print(f"Level: {player_level}")
    print(f"XP: {player_xp}")
    print(f"XP needed for the next level: {xp_to_next_level()}")


def xp_to_next_level():
    xp_required = xp_per_level - player_xp
    return  xp_required


def simulate_battle():
    print("The Minotaur is here!")
    print("You strike the Minotaur with multiple strikes!")
    print("You have slain the mighty beast!")
    global player_level
    xp_reward = (player_level *12) * 5 + 20
    print(xp_reward)
    return xp_reward


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


gain_xp(simulate_battle())
show_stats()

gain_xp(simulate_battle1())
show_stats()

gain_xp(simulate_battle2())
show_stats()

# Set the player's starting health
player_health = 100
print(f"Starting health: {player_health}")

# A monster attacks! Subtract 25 damage
player_health = player_health - 25
print(f"A monster attacks! Health after attack: {player_health}")

# The player finds a potion! Add 10 health
player_health = player_health + 10
print(f"You found a potion! Health after potion: {player_health}")

# Print the final health
print(f"\nFinal player health: {player_health}")

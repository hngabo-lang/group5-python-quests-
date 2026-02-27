# Ask the player which direction they want to go
direction = input("choose Do you go 'left' or 'right'? ").strip().lower()

if direction == "left":
    # If they go left, ask what they do next
    action = input(" Do you 'swim' across or 'wait' for a boat? ").strip().lower()

    if action == "swim":
        # Swimming leads to treasure
        print("You bravely swim across and discover a glittering chest of treasure! You WIN!")
    else:
        # Waiting leads to a different outcome
        print("You wait... and wait... The boat never comes. You head home empty-handed.")

elif direction == "right":
    # Going right leads to a different outcome
    print("You head right and walk straight into a dragon's lair. You flee in terror!")
else:
    # Any other input
    print("You stand frozen with indecision and a goblin pickpockets you. Game over!")




start = '''
You're on a survival game show called "Real Life Temple Run" that is shooting
on location in the Amazon Rainforest. A few days into your adventure, you see a
strange temple.
'''
print(start)

user_input = input("Do you enter the temple? Type 'yes' or 'no'")
if user_input == "yes":
    user_input = input("As you walk into the temple, you hear something growl. Do you shine your flashlight to see what's going or do you run away? Type shine or run.")
    if user_input == "shine":
        print("You see the monster, and you are chased and killed. The game show canceled following your death. You're eliminated! End game.")
    elif user_input == "run":
        user_input = input("The monster chases you, but as you run through the temple and enter a peaceful courtyard, it stops at the entrance. You realize it can't leave the temple. Do you fight the monster to show your strength to viewers or do you continue running? Type fight or flight.")
        if user_input == "fight":
            print("You boost the show's ratings but are then told by producers that you've won by default because everyone else was eliminated by the monster. Congratulations! End game.")
        elif user_input == "flight":
            user_input = input("You run away and arrive at a clearing. You see a pile of wood and a sign that says 'Build a shelter.' Producers radio in to tell you that you can call a friend. You immediately think of 3 people:your dad, your engineer coworker Bob, and your best friend Sally. Type dad, Bob, or Sally.")
            if user_input == "dad":
                print("You didn't tell him you went on the show. He demands that you come back and starts to cry. You are forced to leave the show. End game.")
            elif user_input == "Bob":
                print("He tells you to assemble a frame and get some roof shingles. You don't have roof shingles, so the call is wasted. You've eliminated.")
            elif user_input == "Sally":
                print("She Googles it for you and goes on Wikihow. You successfully build a shelter and win the game. Congratulations! End game.")
        else:
            print("Please type fight or flight.")
    else:
        print("Please type shine or run.")
elif user_input == "no":
    user_input = input("You begin to walk away from the temple, and a tree falls in front of you, forcing you back to the temple's entrance. Do you enter now? Type yes or no.")
    if user_input == "yes":
        user_input = input("As you walk into the temple, you hear something growl. Do you shine your flashlight to see what's going or do you run away? Type shine or run.")
        if user_input == "shine":
            print("You see the monster, and you are chased and killed. The game show canceled following your death. You're eliminated! End game.")
        elif user_input == "run":
            user_input = input("The monster chases you, but as you run through the temple and enter a peaceful courtyard, it stops at the entrance. You realize it can't leave the temple. Do you fight the monster to show your strength to viewers or do you continue running? Type fight or flight.")
            if user_input == "fight":
                print("You boost the show's ratings but are then told by producers that you've won by default because everyone else was eliminated by the monster. Congratulations! End game.")
            elif user_input == "flight":
                user_input = input("You run away and arrive at a clearing. You see a pile of wood and a sign that says 'Build a shelter.' Producers radio in to tell you that you can call a friend. You immediately think of 3 people:your dad, your engineer coworker Bob, and your best friend Sally. Type dad, Bob, or Sally.")
                if user_input == "dad":
                    print("You didn't tell him you went on the show. He demands that you come back and starts to cry. You are forced to leave the show. End game.")
                elif user_input == "Bob":
                    print("He tells you to assemble a frame and get some roof shingles. You don't have roof shingles, so the call is wasted. You've eliminated.")
                elif user_input == "Sally":
                    print("She Googles it for you and goes on Wikihow. You successfully build a shelter and win the game. Congratulations! End game.")
            else:
                print("Please type fight or flight.")
        else:
            print("Please type shine or run.")
    elif user_input == "no":
        print("You walk into the fallen tree and get eliminated because you are trapped. End game.")
    else:
        print("Please type yes or no.")

else:
    print("Please type yes or no.")

print("Welcome to the Adventure Game!")
print("You find yourself in a dark forest. Your goal is to survive and find a way out.")

# First choice
print("\nYou see two paths ahead. One leads to the mountains, and the other into a dense jungle.")
choice1 = input("Where do you want to go? Type 'mountains' or 'jungle': ").lower()

if choice1 == "mountains":
    print("\nYou head towards the mountains. The air gets colder as you climb higher.")
    print("You see a cave and a narrow path leading further up.")
    choice2 = input("Do you enter the cave or continue up the path? Type 'cave' or 'path': ").lower()
    
    if choice2 == "cave":
        print("\nYou enter the cave and find a treasure chest filled with gold! You win!")
    elif choice2 == "path":
        print("\nYou follow the path but it leads to a steep cliff. You slip and fall. Game over.")
    else:
        print("\nInvalid choice. A rockslide occurs and you are trapped. Game over.")

elif choice1 == "jungle":
    print("\nYou venture into the jungle. It's humid and the sounds of animals surround you.")
    print("You find a river and a hut nearby.")
    choice2 = input("Do you go to the river or enter the hut? Type 'river' or 'hut': ").lower()
    
    if choice2 == "river":
        print("\nYou drink some water and rest by the river, but a crocodile appears. You run but can't escape. Game over.")
    elif choice2 == "hut":
        print("\nYou enter the hut and find a map leading out of the forest. You follow it and escape safely. You win!")
    else:
        print("\nInvalid choice. You get lost in the jungle. Game over.")

else:
    print("\nInvalid choice. You wander aimlessly in the forest and are never seen again. Game over.")


print("\nThanks for playing the Adventure Game!")
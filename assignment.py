def start_game():
    print("Welcome to the Mysterious Forest!")
    print("You find yourself standing at the edge of a dense, foggy forest.")
    print("Tall trees loom overhead, and there's a narrow path that leads into the forest.")
    print("You can go either left or right.")
    
    choice = input("Do you go left or right? (left/right): ").lower()
    
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please choose 'left' or 'right'.")
        start_game()

def left_path():
    print("\nYou decide to venture left, following the winding path.")
    print("The air grows cooler as the trees become denser, and you come across a glowing blue stone on a pedestal.")
    print("The stone hums with magical energy.")
    
    choice = input("Do you approach the stone or turn back? (approach/turn back): ").lower()
    
    if choice == "approach":
        approach_stone()
    elif choice == "turn back":
        print("\nYou turn around and walk back to the starting point.")
        start_game()
    else:
        print("Invalid choice. Please choose 'approach' or 'turn back'.")
        left_path()

def approach_stone():
    print("\nAs you approach the stone, the air around you vibrates with energy.")
    print("A large, imposing figure appears before you — a Forest Guardian.")
    print("The Guardian speaks in your mind: 'You have awakened me. I will grant you one wish, but be careful with your choice.'")
    
    choice = input("Do you ask for wisdom, power, or safe passage? (wisdom/power/safe passage): ").lower()
    
    if choice == "wisdom":
        wisdom_ending()
    elif choice == "power":
        power_ending()
    elif choice == "safe passage":
        safe_passage_ending()
    else:
        print("Invalid choice. Please choose 'wisdom', 'power', or 'safe passage'.")
        approach_stone()

def wisdom_ending():
    print("\nThe Guardian grants you profound knowledge of the world.")
    print("You feel enlightened, and the fog lifts, revealing a path to safety.")
    print("The forest becomes your sanctuary, and you live peacefully with the wisdom you have gained.")
    end_game()

def power_ending():
    print("\nThe Guardian grants you immense strength. You feel invincible!")
    print("But with great power comes an insatiable hunger for more.")
    print("You rule over the forest for eternity, but you are forever searching for something greater.")
    end_game()

def safe_passage_ending():
    print("\nThe Guardian grants you safe passage out of the forest.")
    print("The fog lifts, and the trees part, revealing a path leading to freedom.")
    print("You emerge safely from the forest, forever grateful for the Guardian's mercy.")
    end_game()

def right_path():
    print("\nYou decide to head right, following a wider trail.")
    print("The trees become less dense, and the sunlight filters through the canopy.")
    print("Soon, you arrive at a small stream with a bridge made of old, weathered wood.")
    
    choice = input("Do you cross the bridge or look for another way around? (cross/look around): ").lower()
    
    if choice == "cross":
        cross_bridge()
    elif choice == "look around":
        look_around_stream()
    else:
        print("Invalid choice. Please choose 'cross' or 'look around'.")
        right_path()

def cross_bridge():
    print("\nYou cross the bridge. It creaks under your weight, but you make it safely to the other side.")
    print("There is a stone doorway hidden by ivy on the other side.")
    
    choice = input("Do you enter the doorway or examine the bridge markings? (enter/examine): ").lower()
    
    if choice == "enter":
        doorway_ending()
    elif choice == "examine":
        print("\nYou study the markings on the bridge, but they seem to be indecipherable.")
        print("The air feels heavy with magic, and you decide to proceed cautiously.")
        doorway_ending()
    else:
        print("Invalid choice. Please choose 'enter' or 'examine'.")
        cross_bridge()

def doorway_ending():
    print("\nYou enter the stone doorway, and it leads you to a hidden world full of magic.")
    print("You find yourself in a land filled with strange creatures and powerful forces.")
    print("You must decide whether to stay and explore this new world or return to your own.")
    end_game()

def look_around_stream():
    print("\nYou decide not to cross the bridge and look for another path around the stream.")
    print("After walking for a while, you discover a narrow path that follows the stream.")
    print("You soon find a hidden cave behind a waterfall.")
    
    choice = input("Do you enter the cave or turn back to cross the bridge? (enter/turn back): ").lower()
    
    if choice == "enter":
        cave_ending()
    elif choice == "turn back":
        cross_bridge()
    else:
        print("Invalid choice. Please choose 'enter' or 'turn back'.")
        look_around_stream()

def cave_ending():
    print("\nInside the cave, you find ancient treasures, but it feels dark and ominous.")
    print("The deeper you go, the more you feel like you may never find your way out.")
    print("You gain riches but at the cost of your freedom. The cave becomes your prison.")
    end_game()

def end_game():
    print("\nThe adventure ends here. Thanks for playing!")
    replay = input("Would you like to play again? (yes/no): ").lower()
    
    if replay == "yes":
        start_game()
    else:
        print("Goodbye!")

# Start the game
start_game()

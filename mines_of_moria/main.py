
from art import *

should_play = True
while should_play == True:
    print(logo)
    print("Gandalf in the Mines Of Moria\n")
    print(f"Before you is the entrance to the Mines of Moria. \nIts door is shut.\n\n")
    i = 0
    while i == 0:

        response = input("Above the door is carved the following: 'Speak friend, and enter.'\nYou think that a password must be spoken. What do you say?\n")
        response = response.lower()
        if response == "friend" or response == "beloch" or response == "belloch":
            i += 1
            print("The door opens. You may enter the mines.\nThis riddle is indeed from a simpler time!\n\n")



        else:
            print("The door remains shut.\n \n")

    while i == 1:
        corridor_1 = input("You are in an enormous, darkened chamber. Dwarven skeletons are scattered throughout the room. You can see a corridor to the left, and another to the right. \nWhich do you choose?\n")
        corridor_1 = corridor_1.lower()

        if corridor_1 == "left":
            corridor_1Choice = input("\n\nYou hear the sound of an approaching army. It sounds like orcs, or perhaps goblins. Do you continue, or do you go back?\n")
            corridor_1Choice = corridor_1Choice.lower()
            if corridor_1Choice == "continue":
                print("\n\nThe goblin army easily overwhelms your small band. The fellowship is defeated, your friends are killed, and the Ring of Power eventually finds its way to its master, Sauron.")
                i += 4
            elif corridor_1Choice == "go back":
                print("\n\nYou are back in the entry hall.")

            else:
                corridor_1Choice = input("I cannot understand you. Please enter 'continue' or 'go back'.\n")
                if corridor_1Choice == "continue":
                    print("\n\nThe goblin army easily overwhelms your small band. The fellowship is defeated, your friends are killed, and the Ring of Power eventually finds its way to its master, Sauron.")
                    i += 4
                elif corridor_1Choice == "go back":
                    print("\n\nYou are back in the entry hall.")
        if corridor_1 == "right":
            print("\n\nYou can hear the sounds of an army crashing in the distance. You seem to have avoided certain destruction for now.")

            i += 1
    if i == 2:
        print("\n\nThis dark corridor seems to go on forever. You are not sure you remember the way.")
        
        while i == 2:

            corridor_2Choice = input("\n\nSuddenly, you hear the sound of an army approaching from behind. Do you turn and fight, or do you run? (Enter 'fight' or 'run')\n")

            corridor_2Choice = corridor_2Choice.lower()

            if corridor_2Choice == "fight":
                i += 3 
                print("\n\nYour small band is easily overwhelmed by the goblin army. The fellowship is defeated, your friends are killed, and the Ring of Power eventually finds its way to its master, Sauron.")

            elif corridor_2Choice == "run":
                i += 1
                print("\n\nYou are able to stay ahead of the marauding force. As you cross a narrow stone bridge, you hear a deafening roar from the depths beneath. You suspect it may be the ancient evil known as the Balrog, a foe you had hoped never to face.")

            else:
                print("\n\nSorry, I cannot understand you. Please enter 'fight' or 'run'.")

    while i == 3:
        bridgeChoice = input("\n\nDo you turn to face this ancient evil, or do you continue to run with your friends? (Enter 'fight' or 'run')\n")
        bridgeChoice = bridgeChoice.lower()
        if bridgeChoice == "fight":
            i += 1
            print("\n\nYou turn to face the enormous, fiery demon. You steel yourself for battle, shouting grimly 'You shall not pass!' The Balrog's whip catches your leg, and you are pulled to the depths below, where you will continue to fight. Who knows what your fate will be? \n")


        elif bridgeChoice == "run":
                i += 3
                print("\n\nYou cannot outrun the Balrog. It quickly overwhelms you, and your friends die in misery and fear. The Balrog forces you to witness their pain before finishing you off. The fellowship is defeated, and the Ring of Power eventually finds its way to its master, Sauron.")

            
        else:
                print("\n\nI cannot understand you. Please enter 'fight' or 'run'")
    if i == 4:
        print(gandalf)
        print("\n\nThe Fellowship has survived, and there is still a fool's hope that Sauron will be defeated. \n\nYou have won the game!")

        if input('Enter "y" to play again: ').lower() == "y":
            should_play = True
            continue
        else:
            print("Goodbye")
            should_play = False 
               
    if i > 4: 
        print("\n\nYour quest has failed. Game over.")
        print(orc)
        if input('Enter "y" to play again: ').lower() == "y":
            should_play = True
            continue
        else:
            print("Goodbye")
            should_play = False
           
           
"""
This is a selection game that takes you to
the Treasure depending on what choices the user chooses
"""


#Treaure Island Game

print(r'''
               ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
      ''')

print("Welcome to Treaure Island")
print("Your mission is to find the treasure! Let's go!!! ")



location = input("Enter where you want to start from, 'right' or 'left': ")


if location == "left" or location == "Left":
    print("Awesome choice! You've come to a lake. There is an island in the middle of the lake!")
    print("Do you want to Swim to cross over or Wait for a boat?")
    action = input('Type "swim" or "wait": ').lower()
    if action == "wait" :
        print("Nice!, You've arrived at the Island unharmed! ")
        print("There is a house with 3 coloured doors(Red, Yellow or Blue),\n Now tell me which door do want to go in?")
        door = input("Type red or blue or yellow: ").lower()
        if door == "yellow" :
            print("You win! you made it through without any attacks during the treasure hunt!!")
            print("Now take your Treasure!")
            print(r'''
               ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
      ''')
        elif door == "red" or door == "Red": 
            print("No! You are now burned by fire! Game Over!")
        elif door == "blue":
            print("Eaten by Beasts, Game over!")
        else:
            print("Wrong choice , game over !!")
    else:
        print("Wrong choice! you have been attacked by a trout! Game Over !")
        
else:
    print("You've fallen into a hole, Game over!!")

    
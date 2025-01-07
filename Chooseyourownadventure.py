from time import sleep

def type(text):
    for i in text :
        print(i, end = "")
        sleep(.1)
    print("")
name = input("To begin this choose your own adventure journey,\nwhat is your travelers name?\n")
print("Hello,", name,"!" "You have just woken up in the middle of the forest, confused. \nWhen you first wake up, there is a strange man on a horse.")
answer = input("Talk to him? \n(yes/yes)\n")
if answer == "yes" :
    print( name, ": Where am I??")
    sleep(1)
    print("Inconspicuous Stranger : You are in the great jungle, filled with various temples, ancient trees and beautiful waterfalls.")
    print( name, ": How do I get home?")
    print("Inconspicuous Stranger : I may deliver you home, for a price of 10 rubies")
    print("")
    

    answer = input ("Where would you like to go?" " (left/right)\n")
    if answer == "left" :
        answer = input("You see a temple, would you like to enter or keep walking?" " (enter/walk)\n")
        if answer == "enter":
            print("Upon entering, you see two staircases, one going up and down, both staircases are flooded with darkness and you cannot see anything.")
            answer = input("What to do, what to do... (up/down)\n")
            if answer == "up":
                print("You didn't see a tripwire and stepped on it. It triggered an arrow and you died. \n You Lose!")
            if answer == "down":
                    input("")
    elif answer == "right" :
        print()
    else:
        print("Invalid response! You lose..." )
else:
    print("The only answer was yes! You lose!")
   
# an object describing our player
player = { 
    "name": "p1", 
    "score": 0,
    "items" : ["milk"],
    "friends" : [],
    "location" : "start"
}

rooms = {
    "room1" : "a ocean clearing",
    "room2" : "a olympus path",
    "room3" : "a deep ocean path"
}

import random # random numbers
import sys # system stuff for exiting

def rollDice(minNum, maxNum, difficulty):
    result = random.randint(minNum,maxNum)
    print "You roll a: " + str(result) + " out of " + str(maxNum)

    if result <= difficulty:
        print "trying again...."
        
        raw_input("press enter >")
        rollDice(minNum, maxNum, difficulty)

    return result

def gameOver():

    print "-------------------------------"
    print "to be continued!"
    print "name: " + player["name"]
    print "score: " + str(player["score"])
    return #why is there a be friends w mermaid?

def printGraphic(name):
    if (name == "title"):
		print ' ____ |  | ___.__. _____ ______  __ __  ______. ' 
		print ' /  _ \|  |<   |  |/     \\____ \|  |  \/  ___/ '
		print '(  <_> )  |_\___  |  Y Y  \  |_> >  |  /\___ \  '
		print ' \____/|____/ ____|__|_|  /   __/|____//____  >.'
		print '            \/          \/|__|              \/  '

def oceanClearing():
    print "You stand in the Ocean abyss."
    print "There is a castle ahead of you and the deep ocean to the right."
    print "Your options: [ olympus path, deep ocean path, exit ]"

    pcmd = raw_input(">") 

    if (pcmd == "olympus path"):
        print "You take the olympus path."
        raw_input("press enter >")
        olympusPath() # path 1

    elif (pcmd == "deep ocean path"):
        print "You take the other, deep ocean path."
        raw_input("press enter >")
        deepOceanPath() # path 2

    elif (pcmd == "exit"):
        print "you exit."
        return # exit the application

    else:
        print "I don't understand that"
        oceanClearing() # the beginning

def deepOceanPath():
    print "The ocean is filled with creepy critters, but you move forward anyway..."
    print "You stop when you notice something stuck in the coral."
    printGraphic("tree")
    raw_input("press enter >")

    print "You consider your options."
    print "options: [ grab object , back to clearing]"

    pcmd = raw_input(">")

    if (pcmd == "grab object"): 
        print "You grab the object..."
        print "Let's roll a dice to see what happens next!"
        raw_input("press enter to roll >")

        difficulty = 10
        roll = rollDice(0, 20, difficulty)
        
        if (roll >= difficulty):
            print "It looks like a tritan!"
            print "Do you take the tritan?"
        else:
            print "Turns out it's nothing... oh well."
            deepOceanPath()

        pcmd = raw_input("yes or no >")

       	if (pcmd == "no"):
            print "You leave it there."
            deepOceanPath()

        elif (pcmd == "yes"):
            print "You pick it up and a Greek God strikes you with lightning."
            player["score"] +- 100
  
            gameOver()

        else:
            print "You leave it there."
            oceanClearing()

    elif (pcmd == "back to clearing"):
        print "You decide to go back."
        pcmd = raw_input(">")
        oceanClearing()

    else:
        print "You can't do that!"
        strangePath()


def olympusPath():
    print "The olympus path leads you to a castle in the ocean."
    print "It is a sight to see."
    raw_input("press enter >")

    print "You walk for a while and see a mermaid"
    print "from the castle. 'Who travels in my castle?', says the mermaid."
    print "...She can talk!"
    raw_input("press enter >")
    
    print "You consider your options."
    print "Options: [ go back, talk to mermaid, run ]"

    pcmd = raw_input(">")

    # option 1: go back
    if (pcmd == "go back"):
        print "You go back..."
        oceanClearing() # try again
    
    # option 2: talk to mermaid
    elif (pcmd == "talk to mermaid"):
        print "You try and talk to the mermaid!"
        print "Let's roll a dice to see what happens next!"
        raw_input("press enter to roll >")

        difficulty = 5
        chanceRoll = rollDice(0,20,difficulty) # roll a dice between 0 and 20

        # if the roll is higher than 5 - 75% chance
        if (chanceRoll >= difficulty):
            print "It's you're lucky day! She want's to be your friend."
            player["score"] += 50
        else:
        	print "You try to talk to the mermaid, but she swims away."
        	olmypusPath()
        
        # nested actions and ifs
        pcmd = raw_input("be friends with the mermaid? yes or no >")

        # yes
        if (pcmd == "yes"):

            print "The mermaid becomes your friend!"

            player["friends"].append("mermaid")
            player["score"] = int(player["score"]) + 100 # conversion
            print "Your score increased to: " + str(player["score"])
            gameOver()

        # no
        elif (pcmd == "no"):
            print "The mermaid swims away!"
            olympusPath()
        
        # try again
        else:
            olympusPath()

    # option 3: run
    elif (pcmd == "run"):
        print "You run!"
        oceanClearing() # back to start

    # try again
    else:
        print "I don't understand."
        olympusPath() # Olympus path

def introStory():
		print "Good to meet you! What should I call you?"
		player["name"] = raw_input ("Please enter your name >")

		print "Welcome to the ocean" + player["name"] + "!"
		print "The story so far..."
		print "You were scuba diving with friends."
		print "On the swim, you found a sparkly spot in the distance."
		print "You're curious. Do you go for it?"

		pcmd = raw_input("please choose yes or no >")

		if (pcmd == "yes"):
			print "You swim to the sparkly spot, it leads into an ocean cleaing."
			raw_input ("press enter >")
			oceanClearing()
		else:
			print "No?...That doesn't work here."
			pcdm = raw_input ("press enter >")
			introStory()

def main():
	printGraphic("title")
	introStory()

main()

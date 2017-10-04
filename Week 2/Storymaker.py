# let the user know what's going on
print ("Welcome to MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
distance1 = raw_input ("Enter an adjective describing distance: ")
adjective1 = raw_input("Enter an adjective: ")
adjective2 = raw_input("Enter another adjective: ")
number1 = raw_input("Enter a number: ")
adjective3 = raw_input("Enter one last adjective: ")
color1 = raw_input("Enter your favorite color: ")
animal1 = raw_input("Enter your favorite animal now: ")
country1 = raw_input("Enter a country you like visiting: ")
badadjective = raw_input("Enter a negative descriptive word: ")
grossanimal1 = raw_input("Enter an animal you don't like: ")
horribleplace1 = raw_input("What's a horrible place?: ")
malebodypart = raw_input ("What's a male body part?: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "Once upon a time, in a " + distance1 + " land, a(n) " + adjective1 + " girl encountered a(n) " + adjective2 + " " \
"witch. This witch offered the " + adjective1 + " girl a free wish. The girl asked for " + number1 + " " \
"wishes, and the witch grew " + adjective3 + " . She said, 'No, you get one!' The " + adjective1 + " girl wished to turn into a(n) " \
"" + color1 + " " + animal1 + " and then be transported to " + country1 + " . The witch, now angry at the girl's greediness, " \
"instead turned her into a(n) " + badadjective + " " + grossanimal1 + "and transported her to " + horribleplace1 + " . " \
"The lesson here is don't be a(n) " + malebodypart + "."


# finally we print the story
print (story)

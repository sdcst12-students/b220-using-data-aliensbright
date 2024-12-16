#python3
import random
"""
* To create a basic program that will generate random data (eventually lots of random data) to populate a massive record that we will store offline.
* To use the random module to help us create random data
* Use a more complicated algorithm to generate data

We are going to use the handout in class and follow the basic star system generation
checklist starting with step 2 and working our way down to the end of step 6.

We will be generating
*d starport type
*d check for naval base
*d check for scout base
*d check for gas giant
*d generate a random name ( you can use a random set of numbers or create a library of words/letters.  The name of the system in the Alien movie franchise, fore example, was LV427)
*d skip step 4 (no travel zone code needed)
* generate size, atmosphere, hydrographics, population, government level, law level and tech level
* note that there are modifiers to your generated values based on some of your previous values
* 1D represents a random number from 1-6.
* 2D represents a random number from 2-12, the sum of 2 dice rolls
* DM represents a modifer to the dice roll, either adding or subtracting values

Assignment Expected Output
Your program for today should generate a dictionary that stores the data you generate.

What comes next?
You will be using a while or for loop to generate multiple data entries to store in a list that we will eventually be writing to a file in JSON format so that we can open and decode it later.
"""

world = {'starport':'','navalBase':'','scoutBase':'','gasGiant':'','name':'','size':'','atmosphere':'','hydrographics':'','population':'','government level':'','law level':'','tech level':'',}

starport  = ['A'  ,'A'  ,'A'  ,'B'  ,'B'  ,'C'  ,'C'  ,'D'  ,'E ' ,'E ' ,'X']
navalBase = ['no' ,'no' ,'no' ,'no' ,'no' ,'no' ,'yes','yes','yes','yes','yes']
scoutBase = ['no' ,'no' ,'no' ,'no' ,'no' ,'yes','yes','yes','yes','yes','yes']
gasGiant  = ['yes','yes','yes','yes','yes','yes','yes','yes','no' ,'no' ,'no']
values = (starport,navalBase,scoutBase,gasGiant)
valuesDict = ('starport','navalBase','scoutBase','gasGiant')
namestring = 'POIUYTREWQASDFGHJKLMNBVCXZ0987654321'

def getsystemcontents():
    for i in range(4):
        val = values[i]
        dictThing = valuesDict[i]
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        totalindex = roll1 + roll2 - 2
        world[dictThing] = val[totalindex]

def generateName():
    name = ''
    for i in range(5):
        x = random.randint(0,35)
        stringval = namestring[x]
        name += stringval
    return name

worldName = generateName()

print(world)




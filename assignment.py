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
'''
starport  = ('A'  ,'A'  ,'A'  ,'B'  ,'B'  ,'C'  ,'C'  ,'D'  ,'E ' ,'E ' ,'X')
navalBase = ('no' ,'no' ,'no' ,'no' ,'no' ,'no' ,'yes','yes','yes','yes','yes')
scoutBase = ('no' ,'no' ,'no' ,'no' ,'no' ,'yes','yes','yes','yes','yes','yes')
gasGiant  = ('yes','yes','yes','yes','yes','yes','yes','yes','no' ,'no' ,'no')
size = ('Asteroid/Planetoid','1,600 km','3,200 km','4,800 km','6,400 km','8,000 km','9,600 km','11,200 km','12,800 km','14,400 km','16,000 km')
atmosphere = ('None.','Trace.','Very thin, tainted.','Very thin.','Thin, tainted.','Thin.','Standard.','Standard, tainted.','Dense.','Dense, tainted.','Exotic.','Corrosive.','Insidious.','Dense, high.','Elipsoid.','Thin, low.')
hydrographics = ('No free standing Water.','10% Water','20% Water','30% Water','40% Water','50% Water','60% Water','70% Water','80% Water','90% Water','No Land Masses.',)
population = ('None.','10s','100s','1,000s','10,000s','100,000s','1,000,000s','10,000,000s','100,000,000s','1,000,000,000s','10,000,000,000s')
governmentLevel = ('No Government Structure.','Company/Corporation.','Participating Democracy.','Self-Perpetuating Oligarchy.','Representative Democracy.','Feudal Technocracy.','Captive Government.','Balkanization.','Civil Service Bureaucracy.','Impersonal Bureaucracy.','Charismatic Dictator.','Non-Charismatic Leader.','Charismatic Oligarchy.','Religious Dictatorship.')
lawLevel = ('No Prohibitions.','Body Pistols, Explosives, and Poison Gas Prohibited.','Portable Energy Weapons Prohibited.','Military Weapons Prohibited.','Light Assault Weapons Prohibited.','Concealable Firearms Prohibited.','Most Firearms Prohibited.','Shotguns Prohibited.','Open Possession of Long Bladed Weapons Prohibited.','Open Possession of any Weapon Prohibited.','Weapon Possession Prohibited.','','','','','','','','')
techLevel = ('Stone Age. Primitive.','Bronze Age to Middle Ages.','Circa 1400 to 1700','Circa 1700 to 1860','Circa 1860 to 1900','Circa 1900 to 1939','Circa 1940 to 1969','Circa 1970 to 1979','Circa 1980 to 1989','Circa 1990 to 2000','Interstellar community','Average Imperial.','Average Imperial.','Above Average Imperial.','Above Average Imperial.','Technical Maximum Imperial.','Occasional non-Imperial.')
'''
starport  = ('A'  ,'A'  ,'A'  ,'B'  ,'B'  ,'C'  ,'C'  ,'D'  ,'E ' ,'E ' ,'X')
navalBase = ('no' ,'no' ,'no' ,'no' ,'no' ,'no' ,'yes','yes','yes','yes','yes')
scoutBase = ('no' ,'no' ,'no' ,'no' ,'no' ,'yes','yes','yes','yes','yes','yes')
gasGiant  = ('yes','yes','yes','yes','yes','yes','yes','yes','no' ,'no' ,'no')
size = (0,1,2,3,4,5,6,7,8,9,'A')
atmosphere = (0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F')
hydrographics = (0,1,2,3,4,5,6,7,8,9,'A')
population = (0,1,2,3,4,5,6,7,8,9,'A')
governmentLevel = (0,1,2,3,4,5,6,7,8,9,'A+')
lawLevel = (0,1,2,3,4,5,6,7,8,9,'A','B','C','D')
techLevel = (0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G')

values = (starport,navalBase,scoutBase,gasGiant)
valuesDict = ('starport','navalBase','scoutBase','gasGiant')
namestring = 'POIUYTREWQASDFGHJKLMNBVCXZ0987654321'

def getsystemcontents():
    for i in range(4):
        val = values[i]
        dictThing = valuesDict[i]
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        totalindex = roll1 + roll2 - 2  #-2 so that is goes to the right index value
        world[dictThing] = val[totalindex]

def generateName():
    name = ''
    for i in range(5):
        x = random.randint(0,35)
        stringval = namestring[x]
        name += stringval
    return name

def generateSize():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    totalindex = roll1 + roll2 - 2
    world['size']=size[totalindex]
    return totalindex

def generateAtmosphere(sIndex):
    if sIndex==0:
        world['atmosphere']=atmosphere[0]
        return 0
    else:
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        totalindex = roll1 + roll2 - 7 + sIndex
        world['atmosphere'] = atmosphere[totalindex]
        return totalindex
    

def generatePopulation():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    totalindex = roll1 + roll2 - 2
    world['population'] = population[totalindex]
    return totalindex

def generateHydrographics(sIndex,aIndex):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    totalindex = roll1 + roll2 - 7 + sIndex 
    if sIndex <= 1:
        totalindex = 0
    elif aIndex <= 1 or aIndex >= 10:
        totalindex -= 4
        if totalindex < 0:
            totalindex = 0
        elif totalindex > 10:
            totalindex = 10
    world['hydrographics'] = hydrographics[totalindex] #Sill don't know what the dm are
    
    

def generateGovernment(pIndex):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    totalindex = roll1 + roll2 - 7 + pIndex 
    world['government level'] = governmentLevel[totalindex]
    return totalindex

def generateLaw(gIndex):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    totalindex = roll1 + roll2 - 7 + gIndex 
    world['law level']= lawLevel[totalindex]
    return totalindex

def generateTech():
    totalindex = random.randint(1,6)
    if world['starport']=='A':
        totalindex += 6
    if world['starport']=='B':
        totalindex += 4
    if world['starport']=='C':
        totalindex += 2
    if world['starport']=='X':
        totalindex -= 4
    if world['size'] <= 1:
        totalindex += 2
    if 1 < world['size'] <= 4:
        totalindex += 1
    if world['atmosphere'] <= 3 or 10 <= atindex <= 14:
        totalindex += 1
    if world['hydrographics'] == 9:
        totalindex += 1
    if world['hydrographics'] == 'A':
        totalindex += 2
    if 1 <= world['population'] <= 5:
        totalindex += 1
    if world['population'] == 9:
        totalindex += 2
    if world['population'] == 'A':
        totalindex += 4
    if world['government level'] == 0 or world['government level'] == 5:
        totalindex += 1
    if world['government level'] == 'D':
        totalindex -= 2
    world['tech level'] = techLevel[totalindex]


world['name'] = generateName()
getsystemcontents()
starportType = world['starport'] 
sizeindex = generateSize()
atindex = generateAtmosphere(sizeindex)
popindex = generatePopulation()
generateHydrographics(sizeindex,atindex)
govindex = generateGovernment(popindex)
generateLaw(govindex)
generateTech()




for i in world:
    print(' ',i,':',world[i])
print('\n\n',world)



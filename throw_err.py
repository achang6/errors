#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys, os, argparse

parser = argparse.ArgumentParser()
parser.add_argument('error_type')
args = parser.parse_args()
error_type = args.error_type

if error_type == "assertion":
    monkey = True
    if monkey:
        bananasInStock = False
    assert bananasInStock
elif error_type == "io":
    fish_scaled = True
    head_decapitated = True
    disembowel = open('Pictures/Fish_Belly/Bisected_Fish.gif')
elif error_type == "import":
    import wild_cats_gone_wild
elif error_type == "index":
    dungeon_doors = range(1,100,2)
    hidden_boss_door = 101
    print(dungeon_doors[hidden_boss_door])
elif error_type == "key":
    mortal_enemies = {'worst': 'time',
            'worse': 'work',
            'bad'  : 'laws of physics',
            'not-so-bad': 'the sun'
            }
    print(mortal_enemies['alright'])
elif error_type == "name":
    def appettite_inducing_ray_gun():
        print(hungry)

    print('Are you hungry?')
    appettite_inducing_ray_gun()

elif error_type == "os":
    fishtank = range(0,10,1)
    for fishinMate in fishtank:
        print(fishinMate, os.ttyname(fishinMate))

elif error_type == "type":
    print('Hello There')
    print('1 +' + 1 + ' does not equal 2')

elif error_type == "value":
    monkey = 'z'
    print(str(int(monkey)+1))
elif error_type == "zerodivision":
    andyPythonProjectProgress = 0
    timeToWorkOnProject = 0
    dailyWorkAllocation = (1 - andyPythonProjectProgress) / timeToWorkOnProject

    print('Andy Q.Q')

else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()

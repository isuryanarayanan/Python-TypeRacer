from words import _WORDS
import time as t
import random

def game(wordlist):
    points = 0
    random.shuffle(wordlist)
    totalTimeStart = t.time()
    for word in wordlist:
        start ,end ,elapsed = 0 ,0 ,0
        print("TYPE "+word+"\n")
        start = t.time()
        answer = input(">>")
        end = t.time()
        elapsed = end - start
        if answer == word:
            points += 1
            print("Right\tpoints : "+str(points)+" in "+str(elapsed)+" \n---------")
        else:
            print("Wrong\tpoints : "+str(points)+" in "+str(elapsed)+" \n---------")
    totalTimeEnd = t.time()
    totalTime = totalTimeEnd - totalTimeStart
    print("\nResults\n")
    print("\nPoints : "+str(points))
    print("\nTime : "+str(totalTime))

def menu(choice):
    
    # Start the game
    if choice == 's' or choice == 'S':
        print("----------------")
        print("\nGame Starting\n")
        limit = 0
        limit = input("Enter limit:")
        random.shuffle(_WORDS)
        game(_WORDS[0:int(limit)])
    # Exit the game    
    elif choice == 'e' or choice == 'E':
        print("\nExit\n")
        exit()

while(True):
    print("\n \nTYPE RACER \n")
    choice = input("Enter \'S\' to start and \'E\' to exit \n>>")
    menu(choice)

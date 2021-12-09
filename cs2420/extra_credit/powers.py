import random
import sys
import time

def Powers():
    

    powers = ['1' ,'2' , '4' , '8' , '16' , '32' , '64' , '128' , '256' , '512' ,
                 '1k', '2k', '4k', '8k', '16k', '32k', '64k', '128k', '256k', '512k',
                 '1m', '2m', '4m', '8m', '16m', '32m', '64m', '128m', '256m', '512m',
                 '1b', '2b', '4b', '8b', '16b', '32b', '64b', '128b', '256b', '512b',
                 '1t', '2t', '4t', '8t', '16t', '32t', '64t', '128t', '256t', '512t',]
    answered = []

    startTime = time.time()

    while len(answered)!=50:
        question = random.randint(0,49)
        if question in answered:
            continue
        else:
            answered.append(question)
            text = "What is the base 2 of " + str(question) + "? " 
            answer = input(text)
            while answer!= powers[question]:
                answer = input("Wrong! Please Try again: ")
    print("\nYour total time was" , int(time.time()-startTime),"seconds.")


def main():
    print("Hello! This excercise tests a users understanding of the base powers of 2!")
    print("The program will ask the user a base power of 2.")
    print("For example: What is the base power 2 of 34?")
    print("The user does not need to know the exact number except for numbers up to 9")
    print("instead we use k for thousand,m for million,b for billion,and t for trillion")
    print("so in our example of base power 2 of 34. The user would input 16b.")
    print("If the user inputs a wrong number. A message will appear saying. Wrong! Please Try again:")
    print("and the user will have the oppurtunity to answer again.")
    print("if you are ready to start type yes, if you still need some time, take some time,if you wish to quit type quit ")
    if input() == "yes":
        Powers()
    if input() == "quit":
        sys.exit()

main()
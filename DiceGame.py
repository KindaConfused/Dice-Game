from random import randint as rgn

# Dice Game: (the Easy-to-code version™)
# you both roll over and over and whoever gets 50 wins. . .

def Diced():
    print("If you get a 1 you Lose 20 Points!\n")

    score = 0 # Every die roll adds to this
    under_score = 0 # best variable name
    while True:
        roll = 0
    
        print(f"\n\nYour Total: {score}\nPig's Total: {under_score}") # info-nation wya
    
        input_roll = str(input("Press ENTER to roll: ")) # this does absolutely nothing but pauses what happens to the player chooses when to roll
        #Roll
        roll = rgn(1,6)
        if roll == 1:
            score -= 21 # skill issue
        score += roll
        
        #Check
        if score >= 50:
            print(f"\n\nYour WINNING: Total: {score}\nPig's Total: {under_score}")
            print("\nGAME OVER\n\nYou Win the 100% skill game!!!")
            goAgain()
        
        #Roll... but not for me
        roll = rgn(1,6)
        if roll == 1:
            under_score -= 21 # Computation issue (L pc)
        under_score += roll
        
        # Another check (I might as well be a doctor if I'm doing this many check ups)
        if under_score >= 50:
            print(f"\n\nYour Sucky Total: {score}\nPig's Total: {under_score}")
            print("\nGAME OVER\n\nYou lost the 100% skill game smh (skill issue)")
            goAgain()
        if score < 0:
            score = 0
        if under_score < 0:
            under_score = 0

def goAgain():
    choice = input("\nWant to go again?\nY/N: ").lower()
    if choice == "y":
        PigDiced()
    exit()

Diced()
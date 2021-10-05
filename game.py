print("𝘾𝘼𝙏 𝙇𝙄𝙁𝙀")

defaultcat = '''            |\___/|
            )     (
           =\     /=
             )===(
            /     |
            |     |
           /   猫  \     
           \       /     
            \__  _/
              ( (
               ) )
              (_(
'''

simplecat = '''ฅ^•ﻌ•^ฅ'''

caf = '''                           ====
                           !!!!
      ==========================
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  ||      _____          _____    ||
  ||      | | |          | | |    ||
  ||      |-|-|          |-|-|    ||
  ||      #####          #####    ||
  ||                              ||
  ||      _____   ____   _____    ||
  ||      | | |   @@@@   | | |    ||
  ||      |-|-|   @@@@   |-|-|    ||
  ||      #####   @@*@   #####    ||
  ||              @@@@            ||
******************____****************
**************************************'''

otw = '''
　　|＼＿／|
　　|―　―|
　　∧_∧_ノ_＿＿／/
　 (･ω･`)ﾆｬｰ　　　/
　 O[transporting...]⊂|　 ＿　　ヽ
　 ＯＯノ_／｣/_／＼｣
'''

#HP AA
fhp = '''HP[■■■■■■■■■■]FULL/10'''
ninehp = '''HP[■■■■■■■■■ ]9/10'''
eighthp = '''HP[■■■■■■■■  ]8/10'''
sevenhp = '''HP[■■■■■■■   ]7/10'''
sixhp = '''HP[■■■■■■    ]6/10'''
fivehp = '''HP[■■■■■     ]5/10'''
fourhp = '''HP[■■■■      ]4/10'''
threehp = '''HP[■■■       ]3/10'''
twohp = '''HP[■■        ]2/10'''
onehp = '''HP[■         ]1/10'''
zerohp = '''HP[          ]0/10'''

#code

#Brief explimation of game
print("welcome".upper())
print(defaultcat)
print("You are a cat lost in Karuizawa. You find yourself wandering around ISAK")

#Introduction:1 talk to cat
print("You find another cat on campus. Does you want to talk to the cat? (Y/N)(Y for yes,N for no):")
answer = input("[talk to the cat?]").upper()
print(f"you said {answer}")

while answer not in "Y":
    print(f"{simplecat} *stares :The cat is staring at you. You are in an awkward situation...")
    print("[Hint]Answers must be inputted with Y or N. Y meaning yes, N meaning no")
    print(f"{simplecat} < *staring")
    answer = input("[talk to the cat?]").upper()

if answer == "Y":
    print(f"{simplecat} <Hi there! I think I never seen you around here.Whats your name?")
    name = input("[Enter your name]".upper()).title()
    print(f"{simplecat} < your name is {name}. Right?")
    confirm = input("[Start game with this name?] enter Y if Yes").upper()
    while confirm not in "YN":
        print("wrong input!! Answer with Y(yes) or N(no).")
        confirm = input(f"Start game with this name?{name}").upper()


while confirm not in "Y":
    name = input("[What is your name?]").title()
    confirm = input("[Are you sure?] answer Y if yes").upper()



#move to caf
print(f"{simplecat} so your name is {name}...")
print(f"{simplecat} < well {name}... you seem lost and hungry I'll show you around")
print(otw)
import time
time.sleep(5)


#Read from the database file
with open("database.txt","a") as file:
    file.write(f"{name},{0},{0}\n")
#read from the same database file
with open("database.txt","r") as file:
    for line in file.readlines():
        name,score,time =line.split(',')
        print(name)
        print(score)
        print(time)
story = int(input("Enter the story you want(1or2)"))
with open (f"story_{story}.txt","r") as file:
    print(file.readline())


#Introduction:2 caf(HP)
print(f"{simplecat} < First is the cafeteria. This is where humans make and eat food. I live under the caf back entrance")
time.sleep(3)
print(caf)
time.sleep(4)

#HP
print(f"{simplecat}< Oh! theres a piece of fish on the caf floor!. Does {name} want to pick it up (Y?N): ")
answer = input("pickup?".upper()).upper()
print(f"{name} said {answer}")

while answer not in "YN":
    answer = input("wrong input!!! enter Y for yes, N for No: ").upper()

if answer == "Y":
    print(f"{name} has a (piece of fish)")
    print(f"{simplecat} < eat it!!")
    answer = input("[EAT?]").upper()
    while answer not in "Y":
        print(f"{simplecat} ...")
        time.sleep(3)
        print(f"{simplecat} < eat it")
        time.sleep(1)
        print(f"{simplecat} < eat it")
        time.sleep(1)
        print(f"{simplecat} < eat it")
        answer = input("[EAT?]").upper()
    if answer == "Y":
        print(threehp)
        print(f"{simplecat} < That was your HP")
        print(f"{simplecat} < Because you ate it, your HP changes")
        time.sleep(3)
        print(sixhp)
        print(f"{simplecat} < That's your HP right now! (piece of fish) recovers your HP by (3)")
        time.sleep(2)
        print(f"{simplecat} < You can also keep your stuff in your (bag) to use later")
        time.sleep(1)
        print(f"{simplecat} < Oh... Why I didn't say that earlier? Cuz your HP was too low. You were about to die")
        print(f"{simplecat} < anyways...")

        #Instructions
        print("Loading game instructions...")
        time.sleep(3)
        print("[Instructions]")
        time.sleep(1)
        print("[When your HP is 0, game over]")
        time.sleep(1)
        print("[Survive on this campus, until your owner finds you]")
        time.sleep(1)
        print("You can explore places in ISAK only")
        time.sleep(1)
        print("Yes No question should be answered with Y or N")
        time.sleep(1)
        print("You will encounter people.")
        time.sleep(1)
        print("Your goal is to not die")
        time.sleep(1)
        print("good luck")
        time.sleep(1)
        print("[This game is fictional, and has no relation between the names used.]")
        print("[There is no intention to criticize anyone mentioned in this game.]")
        time.sleep(1)
        print(f"Did {name} read and understand the instructions and is ready to start? Y?N ")
        answer = input("[START GAME?]").upper()
        if answer == "Y":
            print(f"{name} said {answer}")
        else:
            while answer not in "Y":
                print(f"When {name} is done reading the instructions and is ready, game will start")
                answer = input("[START GAME?]").upper()
                print(f"{name} said {answer}")
else:
    print(f"{simplecat}< What?! You're not having it?? Well then I'll have it thanks!")
    time.sleep(1)
    print(f"{simplecat} <...")
    print(f"{simplecat}< ... hm")
    print(f"{simplecat} < I'll be nice. Here.")

    answer = input("[Receive the (piece of fish?)]".upper()).upper()
    if answer == "Y":
        print(f"{simplecat} < Here u go,{name}")
        print(f"{name} has a (piece of fish)")

        #instruction
        print(f"{simplecat} < eat it!!")
        answer = input("[EAT?]").upper()
        while answer not in "Y":
            print(f"{simplecat} ...")
            time.sleep(3)
            print(f"{simplecat} < eat it")
            time.sleep(1)
            print(f"{simplecat} < eat it")
            time.sleep(1)
            print(f"{simplecat} < eat it")
            answer = input("[EAT?]").upper()
        if answer == "Y":
            print(threehp)
            print(f"{simplecat} < That was your HP")
            print(f"{simplecat} < Because you ate it, your HP changes")
            time.sleep(3)
            print(sixhp)
            print(f"{simplecat} < That's your HP right now! (piece of fish) recovers your HP by (3)")
            time.sleep(2)
            print(f"{simplecat} < You can also keep your stuff in your (bag) to use later")
            time.sleep(1)
            print(f"{simplecat} < Oh... Why I didn't say that earlier? Cuz your HP was too low. You were about to die")
            print(f"{simplecat} < anyways...")

            # Instructions
            print("Loading game instructions...")
            time.sleep(3)
            print("[Instructions]")
            time.sleep(1)
            print("[When your HP is 0, game over]")
            time.sleep(1)
            print("[Survive on this campus, until your owner finds you]")
            time.sleep(1)
            print("You can explore places in ISAK only")
            time.sleep(1)
            print("Yes No question should be answered with Y or N")
            time.sleep(1)
            print("You will encounter people.")
            time.sleep(1)
            print("Your goal is to not die")
            time.sleep(1)
            print("good luck")
            time.sleep(1)
            print("[This game is fictional, and has no relation between the names used.]")
            print("[There is no intention to criticize anyone mentioned in this game.]")
            time.sleep(1)
            print(f"Did {name} read and understand the instructions and is ready to start? Y?N ")
            answer = input("[START GAME?]").upper()
            if answer == "Y":
                print(f"{name} said {answer}")
            else:
                while answer not in "Y":
                    print(f"When {name} is done reading the instructions and is ready, game will start")
                    answer = input("[START GAME?]").upper()
    else:
        print(f"{simplecat} < what is wrong with you...")
        print(f"{simplecat} < eat it!!")
        answer = input("[EAT?]").upper()
        while answer not in "Y":
            print(f"{simplecat} ...")
            time.sleep(3)
            print(f"{simplecat} < eat it")
            time.sleep(1)
            print(f"{simplecat} < eat it")
            time.sleep(1)
            print(f"{simplecat} < eat it")
            answer = input("[EAT?]").upper()
        if answer == "Y":
            print(threehp)
            print(f"{simplecat} < That was your HP")
            print(f"{simplecat} < Because you ate it, your HP changes")
            time.sleep(3)
            print(sixhp)
            print(f"{simplecat} < That's your HP right now! (piece of fish) recovers your HP by (3)")
            time.sleep(2)
            print(f"{simplecat} < You can also keep your stuff in your (bag) to use later")
            time.sleep(1)
            print(f"{simplecat} < Oh... Why I didn't say that earlier? Cuz your HP was too low. You were about to die")
            print(f"{simplecat} < anyways...")

            # Instructions
            print("Loading game instructions...")
            time.sleep(3)
            print("[Instructions]")
            time.sleep(1)
            print("[When your HP is 0, game over]")
            time.sleep(1)
            print("[Survive on this campus, until your owner finds you]")
            time.sleep(1)
            print("You can explore places in ISAK only")
            time.sleep(1)
            print("Yes No question should be answered with Y or N")
            time.sleep(1)
            print("You will encounter people.")
            time.sleep(1)
            print("Your goal is to not die")
            time.sleep(1)
            print("good luck")
            time.sleep(1)
            print("[This game is fictional, and has no relation between the names used.]")
            print("[There is no intention to criticize anyone mentioned in this game.]")
            time.sleep(1)
            print(f"Did {name} read and understand the instructions and is ready to start? Y?N ")
            answer = input("[START GAME?]").upper()
            if answer == "Y":
                print(f"{name} said {answer}")
            else:
                while answer not in "Y":
                    print(f"When {name} is done reading the instructions and is ready, game will start")
                    answer = input("[START GAME?]").upper()

print(f"{simplecat} < Starting game")

#Game start chapter 1
time.sleep(3)
print("Before we start this game: input the difficulty of the game.")
print(f"{simplecat} < I recommend entering 1 as your difficulty if it is your first time playing this game")
difficulty = int(input())
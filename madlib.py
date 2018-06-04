# thanks to pyCharm nw my code is organized

# materials
y_n = ["yes", "y", "Y", "no", "n", "N"]
y = y_n[0:3]
n = y_n[3:]
# this variable for difficulty choosing
answer = 0
q1 = "when the extension is .py the language which the file wrote with is ---1---"
q2 = "Type the semi semicolon ---2---"
q3 = "---3--- is the next world ruler      ... it's 'ahmed' but don't say that I told U ;) "
q4 = "python is a ---4--- level language"
q5 = "python is a case ---1--- language"
q6 = "---2--- loop repeats a statement or group of statements"
q7 = "---3--- terminates the loop statement and transfers execution to the statement immediately following the loop"
q8 = "---4--- is a block of organized, reusable code that is used to perform a single, related action."
q9 = "Function blocks begin with the keyword ---1--- followed by the function name and parentheses ( ( ) )"
q10 = "---2--- is a general-purpose interpreted, interactive, object-oriented, and high-level programming language."
q11 = "what is the number after 9 ? ---3--- "
q12 = "so and what is the number before 9? ---4---"

# s for split
q1split = q1.split()
q2split = q2.split()
q3split = q3.split()
q4split = q4.split()
q5split = q5.split()
q6split = q6.split()
q7split = q7.split()
q8split = q8.split()
q9split = q9.split()
q10split = q10.split()
q11split = q11.split()
q12split = q12.split()
# I found dictionary on internet and it's so useful
question1 = {1: q1split, 2: q2split, 3: q3split, 4: q4split}
question2 = {1: q5split, 2: q6split, 3: q7split, 4: q8split}
question3 = {1: q9split, 2: q10split, 3: q11split, 4: q12split}
answer1 = {1: "python", 2: ";", 3: "ahmed", 4: "high"}
answer2 = {1: "sensitive", 2: "while", 3: "break", 4: "function"}
answer3 = {1: "def", 2: "python", 3: "10", 4: "8"}


# to find the blank space
def blank_find(blank):
    count = 0
    for word in blank:
        if "---" in word:
            break
        count = count + 1
    return count


# the game process
def game(chose):
    if chose in ["1", "2", "3", "4"]:
        ans = raw_input("type your answer ---> ")
        select = int(chose)
        if answer == "1":
            while ans != answer1[select]:
                ans = raw_input("It's so easy type '" + answer1[select] + "' Type it --> ")
            question1[select][blank_find(question1[select])] = ans
        if answer == "2":
            while ans != answer2[select]:
                ans = raw_input("It's so easy type '" + answer2[select] + "' Type it --> ")
            question2[select][blank_find(question2[select])] = ans
        if answer == "3":
            while ans != answer3[select]:
                ans = raw_input("It's so easy type '" + answer3[select] + "' Type it --> ")
            question3[select][blank_find(question3[select])] = ans


# questions
def questions():
    if answer == "1":
        print ""
        print ""
        print " ".join(q1split)
        print " ".join(q2split)
        print " ".join(q3split)
        print " ".join(q4split)
    elif answer == "2":
        print ""
        print ""
        print " ".join(q5split)
        print " ".join(q6split)
        print " ".join(q7split)
        print " ".join(q8split)
    elif answer == "3":
        print ""
        print ""
        print " ".join(q9split)
        print " ".join(q10split)
        print " ".join(q11split)
        print " ".join(q12split)


# check for validation function
def check(word, check_list):
    for valid in check_list:
        if valid == word:
            return True


# a code I found in the internet to draw a heart
def heart():
    print " "
    print "<3"
    print " "


# a code for drawing superman
def superman():
    print("")
    print "S   <--- Superman LOGO"
    print("")


# welcome
print ""
print "WELCOME TO MY GAME"
difficulty = raw_input(
        "Please choose a difficulty level. Press 1 for easy, 2 for medium and 3 for hard then hit enter")
while difficulty not in ["1", "2", "3"]:
    difficulty = raw_input(
        "Please choose a difficulty level. Press 1 for easy, 2 for medium and 3 for hard then hit enter")
if difficulty in ["1", "2", "3"]:
    answer = difficulty
name = raw_input("so... what is your name?   ")
print ""
print ""
print "Okay..", name, ":) I wish you wrote your name correctly because this a stupid program, " \
                    "can't define the wrong name and I wish not calling you MR:BANANA :o"
print "let`s do it", name
print ""
ready = raw_input("Are You ready " + name + " ?   " + "(Y/N) Y = yes N = no  ")


# check if the user put valid input
while not check(ready, y_n):
    print ""
    print ""
    print name, "!!! this a simple yes or no question please give me your attention"
    ready = raw_input("Are You ready " + name + "  (Y/N) Y = yes N = no  ")
    if check(ready, y_n):
        break

# check if the user is ready

# if not ready
if check(ready, n):
    print ""
    print ""
    print "aha okay .... I'm waiting ... ha ? aha I'm okay here waiting for you boss..... "
    print "."
    print ".."
    print "..."
    print "...."
    print "....."
    print ":( I'm not okay"
    print ""
    ready1 = raw_input("when U ready type 'I love U bot' because I need love now <3  " + name + " " + "->")
    if ready1 == "I love U bot":
        print " "
        print "I LOVE YOU MORE"
        heart()
    while ready1 != "I love U bot":
        print ""
        ready1 = raw_input("I'm sad nw if you want to complete type I love U bot" + " " + "->")
        if ready1 == "I love U bot":
            print " "
            print "I LOVE YOU MORE"
            heart()
# if ready
ready2 = "c"
if check(ready, y):
    print " "
    print "so you are ready!"
    print "are you ready to take the risk ?"
    print "to be a hero !!"
    superman()
    ready2 = raw_input("IF U R READY TYPE  c  ---> THEN HIT THE ENTER WITH ALL YOUR SUPERPOWERS :)  ")

while ready2 != "c":
    print ""
    print "It's easy U can do it"
    ready2 = raw_input("IF U R READY TYPE  c  ---> THEN HIT THE ENTER WITH ALL YOUR SUPERPOWERS :)  ")

print ""
print "okay this a fill the blank game"
print "you R not going to be a superhero"
print "You have been deceived"
print ""
emo = "^_^ "
print emo * 10
print ""
print "I was not funny I know"
print "but they said that is a game and I love games :) :) :)"
print "so if U hated me I understand"
print ""
ready3 = raw_input("If U wish to continue press  c  with UR normal power and if not it is oky I feel U type  x ---->  ")

# if want to exit
if ready3 == "x":
    print "bye :("
    exit()

# if want to continue
elif ready3 == "c":
    print ""
    print "so this an easy one"
    print "I'm not good at making questions"
    print "so it will be easy don't worry"
    print "answer that!"
    questions()
    print ""
    print ""
    choose = raw_input("choose the number you want to edit or type  x  to close and show your answer ---> ")

    # ans
    while choose != "x":
        game(choose)

        # after the answer
        print " "
        print ""
        questions()
        print " "
        print ""
        choose = raw_input("choose the number you want to edit or type  x  to close and show your answer ---> ")

    # if want to close
    print "the answers was"
    print answer1
    print "and this ur answer"
    questions()
    print "bye ^_^"

# ^_^
else:
    print ""
    print "I think U hated me"
    print "I feel that U destroyed the keyboard"
    print "I know ... I understand"
    print ""
    print emo * 10
    print ""
    print "bye ^_^"

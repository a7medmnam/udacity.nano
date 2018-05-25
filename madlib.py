#matrials
y_n = ["yes", "y", "Y", "no", "n", "N"]
y = y_n[0:3]
n = y_n[3:]
q1 = "when the extention is .py the langauage which the file wrote with is ---1---"
q2 = "Type the simi semicolon ---2---"
q3 = "---3--- is the next world ruler      ... it's 'ahmed' but don't say that I told U ;) "
q4 = "python is a ---4--- level langauage"
q5 = "python is a case ---5--- language"
q1s = q1.split()
q2s = q2.split()
q3s = q3.split()
q4s = q4.split()
q5s = q5.split()
answer = ["python", ";", "ahmed", "high", "sensitive"]

#questions
def questions():
	print ""
	print ""
	print " ".join(q1s)
	print " ".join(q2s)
	print " ".join(q3s)
	print " ".join(q4s)
	print " ".join(q5s)

#chek for validation function
def check(word,check_list):
	for x in check_list:
		if x == word:
			return True
			break

#a code I found in the internet to draw a heart
def heart():
	x="love";print"   x    x\nx xx x\nx   x   x".replace("x",x)
	for i in range(5):print" "*i+x+" "*(9-i*2),x
	print" "*6,x

#a code for drawing superman
def super():
	print("")
	print("     *****************")
	print("    ***$$$$$$$$$$$$$$**")
	print("   ** $$         $$ $ **")
	print("  ** $$            $$$ **")
	print("  ** $$$               **")
	print("  *$$$$$$$$$           **")
	print("   *$$$$$$$$$$$$$$    **")
	print("    **$$$$$$$$$$$$$$$**")
	print("     **      $$$$$$$**")
	print("      **         $$**")
	print("       **$$$    $$**")
	print("        *$$$$$$$$**")
	print("         **     **")
	print("          **   **")
	print("           ** **")
	print("            ***")
	print("             *")
	print("")

#welcome
print ""
print "WELCOME TO MY GAME"
name = raw_input("so... what is your name?   ")
print ""
print ""
print "Okay..",name,":) I wish you wrote your name correctly because this a stuped program, can't define the wrong name and I wish not calling you MR:BANANA :o"
print "let`s do it",name
print ""
ready = raw_input("Are You ready " + name + " ?   " + "(Y/N) Y = yes N = no  ")

# check if the user put valid input
while check(ready, y_n) != True:
	print ""
	print ""
	print name,"!!! this a simple yes or no question please give me your attention"
	ready = raw_input("Are You ready " + name + "  (Y/N) Y = yes N = no  ")
	if check(ready, y_n) == True:
		break

# check if the user is ready

#if not ready
if check(ready, n) == True:
	print ""
	print ""
	print "ahaa okay .... I'm waitng ... ha ? ahaa I'm okay here waitng for you boss..... "
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
		ready1 = raw_input("I'm sad nw if you want to comblete type I love U bot" + " " + "->")
		if ready1 == "I love U bot":
			print " "
			print "I LOVE YOU MORE"
			heart()

# if ready
if check(ready, y) == True:
	print " "
	print "so you are ready!"
	print "are you ready to take the risk ?"
	print "to be a hero !!"
	super()
	ready2 = raw_input("IF U R READY TYPE  c  ---> THEN HIT THE ENTER WITH ALL YOUR SUPERPOWERS :)  ")

while  ready2 != "c":
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

#if want to exit
if ready3 == "x":
	print "bye :("
	exit()

#if want to continue
elif ready3 == "c":
	print ""
	print "so this an easy one"
	print "I'm not good at making quezes"
	print "so it will be easy don't worry"
	print "answer that!"
	questions()
	print ""
	print ""
	choose = raw_input("choose the number you want to edit or type  x  to close and show your answer ---> " )
	
#ans
	while choose != "x":
		if choose == "1":
			ans1 = raw_input("type your answer ---> ")
			while ans1 != answer[0]:
				ans1 = raw_input("It's so easy type 'python' Type it --> ")
			q1s[13] = answer[0]

		if choose == "2":
			ans1 = raw_input("type your answer ---> ")
			while ans1 != answer[1]:
				ans1 = raw_input("It's so easy type ';' Type it --> ")
			q2s[4] = answer[1]
		
		if choose == "3":
			ans1 = raw_input("type your answer ---> ")
			while ans1 != answer[2]:
				ans1 = raw_input("It's so easy type 'ahmed' Type it --> ")
			q3s[0] = answer[2]

		if choose == "4":
			ans1 = raw_input("type your answer ---> ")
			while ans1 != answer[3]:
				ans1 = raw_input("It's so easy type 'high' Type it --> ")
			q4s[3] = answer[3]
		
		if choose == "5":
			ans1 = raw_input("type your answer ---> ")
			while ans1 != answer[4]:
				ans1 = raw_input("It's so easy type 'sensitive' Type it --> ")
			q5s[4] = answer[4]

#		else:
#			print ""
#			print "Now U should type the question number or x for close"
#			choose = raw_input("choose the number you want to edit or type  x  to close and show your answer ---> " )

		#after the answer
		print " "
		print ""
		questions()
		print " "
		print ""
		choose = raw_input("choose the number you want to edit or type  x  to close and show your answer ---> " )
	
	#if want to close
	print "the answes was"
	print answer
	print "and this ur answe"
	questions()
	print "bye ^_^"
		
#^_^
else:
	print ""
	print "I think U hated me"
	print "I feel that U destroyed the keyboard"
	print "I know ... I understand"
	print ""
	print emo * 10
	print ""
	print "bye ^_^"
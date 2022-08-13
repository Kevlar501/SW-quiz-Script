import time

print("Welcome to Kevin's Star Wars Quiz!")

name = input ("Enter your name: ")
print(f"hello {name}!")

playing = input("Would you like to take the quiz? ")

if playing.upper() != "YES":
    quit()
time.sleep(1)

print("Ok, here we go!")
score = 0 
time.sleep(1)

answer = input("Question 1: What is Darth Vader's real name? ")
if answer.upper() == "ANAKIN SKYWALKER":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
time.sleep(1)

answer = input("Question 2: Help Me Obi-Wan Kenobi, you're my only _____ ")
if answer.upper() == "HOPE":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
time.sleep(1)

answer = input("Question 3: Which Order did Palpatine issue to brand the Jedi traitors and mark them for execution?(type full answer) ")
if answer.upper() == "ORDER 66":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
time.sleep(1)

answer = input("Question 4: What is the name of the Mandalorian foundling rescued by Din Djarin? ")
if answer.upper() == "GROGU":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
time.sleep(1)

answer = input("Question 5: What was the name of Anakin Skywalker's apprentice?(full name) ")
if answer.upper() == "AHSOKA TANO":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
time.sleep(1)

answer = input("Question 6: How many stars does Tatooine orbit around? ")
if answer == "2":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
time.sleep(1)

answer = input("Question 7: What was the name of the Grand Master of the Jedi Order prior to the rise of the Galactic Empire?(name only, no title) ")
if answer.upper() == "YODA":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
time.sleep(1)

answer = input("Question 8: What planet were the clones of the Grand Army of the Republic created on? ")
if answer.upper() == "KAMINO":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
time.sleep(1)

answer = input("Question 9:PEACE IS A LIE, THERE IS ONLY _____ ")
if answer.upper() == "PASSION":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
time.sleep(1)

answer = input("Question 10: What is the name of Star Wars' most iconic Astromech Droid?(use the hyphon!) ")
if answer.upper() == "R2-D2":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
time.sleep(1)

print("Congratulations! You've finished the quiz!")
time.sleep(1)
print("Your score is " + str(score) + " out of 10!")
time.sleep(10)

print("Thank you for playing, Goodbye!")
time.sleep(5)
quit()



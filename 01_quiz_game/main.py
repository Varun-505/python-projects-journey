print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() not in ["yes","y"]:
    quit()

print("Okay! Let's play :)")
score = 0
wrong_answer = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    wrong_answer += 1

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    wrong_answer += 1

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    wrong_answer += 1

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    wrong_answer += 1

print(f"You got {score} questions correct!")
print("Your score is", (score / 4) * 100, "%")
print(f"You got {wrong_answer} questions incorrect!")
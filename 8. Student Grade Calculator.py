def calculateGrade(av):
    grade = ""
    if(av >= 80):
        grade = "A+"
    elif(av >= 70):
        grade = "A"
    elif(av >= 60):
        grade = "B"
    elif(av >= 50):
        grade = "C"
    elif(av >= 40):
        grade = "D"        
    elif(av >= 30):
        grade = "E"
    else:
        grade = "FAIL"

    return grade

def calculateAverage(s):
    total = 0
    for x in s:
        total += x

    return total // len(s)


scores = [50,18,78,25,58,84,78]


average = calculateAverage(scores)
grade = calculateGrade(average)

print("**-ORIGINAL EXAM--**\n")
print ("YOUR GRADE: {}".format(grade))

#resit
print("\n**--RESIT--**\n")


scores[1] *= 2
#bitwise shift operation
#(basically just doubles)
scores[3] <<= 1

average2 = calculateAverage(scores)
grade2 = calculateGrade(average2)

print ("YOUR GRADE: {}".format(grade2))

if(grade2 is not grade):
    print("you did differently this time!")
else:
    print("you got the same grade as before!")
if(18 not in scores):
    print("looks like you resat your worst score from last time")




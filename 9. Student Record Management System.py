#student records
student1 = ("Jim", 29, "A")
student2 = ("Bob", 64, "B")
student3 = ("Jim", 67, "C")
student4 = ("Barry",34, "D")
students = (student1,student2,student3,student4)

studentIds = {487653,487654,487655,487656}
courses = {"Maths", "Physics", "Computer Science", "English", "Science", "Art"}



#search for specific terms in student records
searchTerm = input("What would you like to search for in student records?: ")
amountFound = 0
matches = []

for s in students:
    c = s.count(searchTerm)
    amountFound += c
    if(c > 0):        
        matches.append(s)
    

print("\nthere are {0} results in student records for '{1}'".format(amountFound,searchTerm))

for studentRecord in matches:
    resultNumber = matches.index(studentRecord)+1
    searchTermIndex = studentRecord.index(searchTerm)
    print("\nResult {0}:\nIndex of '{1}': {2}\nStudent Record: {3}".format(resultNumber,searchTerm,searchTermIndex,studentRecord))




#Its coming to the end of the academic year 1983!
#Lets log which courses have been completed, new students arriving and old students leaving
newStudents = {487657, 487658, 487659, 487660}
studentsLeaving = {487653,487654}

studentIds = studentIds.union(newStudents)
studentIds = studentIds.difference(studentsLeaving)

#The students that were here in the class of 1984 will never change! This will be stored for the archives
classOf84 = frozenset(studentIds)

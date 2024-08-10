firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
age = input("Please enter your age: ")
city = input("Please enter the name of your city: ")
occupation = input("What is your occupation?: ")

fullName = firstName + " " + lastName
fullName = fullName.title()

description = " \"a {0} year old\n{1} from {2}\" ".format(age,occupation.title(),city.title())


print("\n"+fullName +"\n\n"+ description)

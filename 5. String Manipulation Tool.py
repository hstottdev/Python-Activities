def sliceString(string):
    start = int(input("enter start index: "))
    end = int(input("enter end index: "))

    return string[start:end]

def main():
    userString = str(input("Please enter a string to manipulate: "))
    option = 0
    while(option < 1 or option > 5):
        option = input("""

    Please select a string manipulation option:

    1. Convert to uppercase
    2. Convert to lowercase
    3. Slice the string from a start index to an end index
    4. Calculate the length of a string
    5. Loop through each character and display it on a new line

        """)      
        try:
            option = int(option)
            if(option < 1 or option > 5):
                print("Please enter a valid number!".upper())
        except:
            print("Please enter a valid number!".upper())
            option = 0
            
    if(option == 1):
        print("Result: \n")
        print(userString.upper())
    if(option == 2):
        print("Result: \n")
        print(userString.lower())
    if(option == 3):
        sliced = sliceString(userString)
        print("Result: \n")
        print(sliced)
    if(option == 4):
        print("Length of {0}:{1}".format(userString, len(userString)))
    if(option == 5):
        print("Result: \n")
        for c in userString:
            print(c)
                
main()

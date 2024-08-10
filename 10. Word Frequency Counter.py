def isEmptyString(st):
    uniqueWords = set(st.split(' '))
    return (len(uniqueWords) == 1) and list(uniqueWords)[0] == ""
    
def getStringInput():
    s = "  "
    while(isEmptyString(s)):
        s = input("Enter some text in order to count the word frequency: ")
    return s.lower()   

        
string = getStringInput()
words = string.split(" ")
wordFrequencies = {}

for i in range(0,len(words)):
    currentCount = wordFrequencies.get(words[i])
    
    #if this is the first instance of a word
    if(currentCount == None):
        #cannot use assignment operator because it won't exist
        wordFrequencies[words[i]] = 1
    else:
        #otherwise you can safely add one
        wordFrequencies[words[i]] = currentCount + 1

print(wordFrequencies)
    

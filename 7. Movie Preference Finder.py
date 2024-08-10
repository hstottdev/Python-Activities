def wordToBool(word):
    if(word[0] == 'y'):
        return True
    else:
        return False

scary = input("Do you like movies that are scary?: ")
scary = wordToBool(scary)

gory = input("Do you like movies that are gory?: ")
gory = wordToBool(gory)

funny = input("Do you like movies that make you laugh?: ")
funny = wordToBool(funny)

action = input("Do you like explosions and fight scenes?: ")
action = wordToBool(action)

adventure = input("Do you like movies where characters go on a journey?: ")
adventure = wordToBool(adventure)

scifi = input("Do you like movies with advanced hypothetical technology?: ")
scifi = wordToBool(scifi)

family = input("Are you looking for something to watch with the whole family?: ")
family = wordToBool(family)

mystery = input("Do you enjoy a good mystery?: ")
mystery = wordToBool(mystery)

superhero = input("Do you like superheroes?: ")
superhero = wordToBool(superhero)

romance = input("Finally, do enjoy a good romance!: ")
romance = wordToBool(romance)

genre = ""
movies = ""


if(family and superhero):
    genre += "Family Superhero\n"
    movies += "\nThe Incredibles \nMegamind"
if(family and adventure):
    genre += "Family Adventure\n"
    movies += "\nPirates of the Caribbean \nRatatouille \nTangled"
if(funny and (scary or gory) and not family):
    genre += "Comedy Horror\n"
    movies += "\nShaun of the Dead \nScary Movie \nHappy Death Day "
if(action and (scary or gory) and not family):
    genre += "Action Horror\n"
    movies += "\nWorld War Z \n28 Days Later \nThe Meg \nCloverfield "
if(scary and scifi and not family):
    genre += "Scifi Horror\n"
    movies += "\nAlien \nA Quiet Place \nBird Box"
if(action and adventure and not family):
    genre += "Action Adventure\n"
    movies += "\nLord of The Rings \nMission Impossible 7 \nFast and Furious 10 "
if(funny and action and not family):
    genre += "Action Comedy\n"
    movies += "\nHot Fuzz \nJonny English: Reborn"
if(scifi and adventure):   
    genre += "Scifi Adventure\n"
    movies += "\nStar Wars: Return of the Jedi \nInterstellar"
if(scifi and funny):   
    genre += "Scifi Comedy\n"
    movies += "\nThe World's End \nGuardians of the Galaxy"
if(mystery and (scary or gory) and not family):
    genre += "Horror Mystery\n"
    movies += "\nScream \nThe Cabin in the Woods"
if(superhero):
    genre += "Superhero\n"
    movies += "\nAvengers Assemble \nSpider-man 2\nJustice League: Snyder Cut"
if(romance and scifi):
    genre += "Scifi Romance\n"
    movies += "\nPassengers \nAbout Time"
if(romance):
    genre += "Romance\n"
    movies += "\nThe Fault In Our Stars \n50 First Dates \nThe Notebook "



if(movies == ""):
    print("Unfortunately I have no reccomendations based on your answers")
else:
    print("Here are some movies I can reccomend: \n\nYOUR MOVIES:{1}  \n\nYOUR PREFERRED GENRES:\n{0}".format(genre,movies))

import os

#Directory path that needs to be created
NewDirectory = r"C:/Users/brand/OneDrive/Desktop/ANIM-T380/anim-t380-2022-assignments/Assignment 3/assets/$asset/maya/"

#this is the name of the new directory to add and the command to do it
directory = "scenes"
path = os.path.join(NewDirectory, directory)
os.makedirs(path)


#this gets the filepath for the aliases file location and makes the variable name
filepath = os.path.join(r"C:\Users/brand\OneDrive\Desktop\ANIM-T380/anim-t380-2022-assignments\Assignment 3\etc", "asset.alias")

#this puts the environment file into an alias and creates the file at the location of the filepath
alias = open(filepath, "w")

#write the word "alias" in the file
alias.write("asset")
alias.close()


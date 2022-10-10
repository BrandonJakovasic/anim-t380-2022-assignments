import maya.standalone
import maya.cmds as cmds


#Open file that was created in the other python file and get the name
file = open(r"C:\Users/brand\OneDrive\Desktop\ANIM-T380/anim-t380-2022-assignments\Assignment 3\etc/asset.alias")
NewName = file.read()


#start Maya
maya.standalone.initialize()

#Create a null group in maya and pass it the new name
cmds.group( em=True, name=NewName)

#save and close maya
cmds.file(rename=r"C:/Users/brand/OneDrive/Desktop/ANIM-T380/anim-t380-2022-assignments/Assignment 3/assets/$asset/maya/scenes/Assignemt3.ma")
cmds.file(save=True, type="mayaAscii")
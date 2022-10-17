import maya.cmds as cmds
import os
import sys

#This code uses the MEL command in Maya to save and increment the scene
#It creates a folder for the backup files to be saved with the specific iteration it is
def CreateBackupFile():
    mel.eval("incrementalSaveScene;")
CreateBackupFile()
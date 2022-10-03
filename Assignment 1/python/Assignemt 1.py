import argparse
import maya.standalone
import maya.cmds

parser = argparse.ArgumentParser(description='This script creates a bunch of helices.')

parser.add_argument('num_helices', type=int, help="Number of helices")

args = parser.parse_args()



maya.standalone.initialize()


print("Creating {} helix(s)...".format(args.num_helices))

for i in range(args.num_helices):

    print("Created helix #{}"

    .format(i))

    maya.cmds.polyHelix()


print("Meshes in the Maya scene:")

print(maya.cmds.ls(geometry=True))

maya.cmds.file(save=True, type='mayaAscii')

maya.standalone.uninitialize()
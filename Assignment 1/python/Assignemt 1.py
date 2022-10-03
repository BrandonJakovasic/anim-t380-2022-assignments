import argparse

parser = argparse.ArgumentParser(description='This script creates a bunch of helices.')

parser.add_argument('num_helices', type=int, help="Number of helices")

args = parser.parse_args()

import maya.standalone

maya.standalone.initialize()

import maya.cmds

print("Creating {} helix(s)...".format(args.num_helices))

for i in range(args.num_cubes):

    print("Created helix #{}"

    .format(i))

    maya.cmds.polyHelix()


print("Meshes in the Maya scene:")

print(maya.cmds.ls(geometry=True))

file -save

maya.standalone.uninitialize()
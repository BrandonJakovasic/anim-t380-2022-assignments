import bpy
import os



#Select all the meshes in the scene
bpy.ops.object.select_all(action='SELECT')


#Apply the location, rotation, and scale of the objects
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


#Toggle edit mode
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_all(action='SELECT')


#Recalculate the normals on the ouside of the object
bpy.ops.mesh.normals_make_consistent(inside=False)


#Clear sharp edges on mesh for export
bpy.ops.object.editmode_toggle()


#Export .FBX to blender file location
basedir = os.path.dirname(bpy.data.filepath)


#Check to see if the base directory is there
if not basedir:
    raise Exception("Blend file is not saved")


#View objects and Selection
view_layer = bpy.context.view_layer
obj_active = view_layer.objects.active
selection = bpy.context.selected_objects


#Deselect Objects
bpy.ops.object.select_all(action='DESELECT')


#Get objects in scene ready to be exported
for obj in selection:

    obj.select_set(True)


    # Some exporters only use the active object
    view_layer.objects.active = obj
    name = bpy.path.clean_name(obj.name)
    fn = os.path.join(basedir, name)  


    #Export object with it's name in the scene as an .FBX
    bpy.ops.export_scene.fbx(filepath=fn + ".fbx", use_selection=True)
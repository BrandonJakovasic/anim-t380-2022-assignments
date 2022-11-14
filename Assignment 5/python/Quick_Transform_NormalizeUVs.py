import bpy
from bpy.types import (Panel, Operator)


#This code is used to create buttons on the 3D viewer of blender that will
#quickly apply the transform, and fix the normals of selected objects



#This is for allowing the code to be used as an addon for Blender
bl_info = {
 "name": "Quick Transforms and UVs",
 "author": "Brandon Jakovasic",
 "description": "Apply transforms and flip normals of selected objects",
 "blender": (2, 80, 0),
 "location": "3D View",
 "warning": "",
 "wiki_url": "",
 "tracker_url": "",
 "category": "Object"}




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Operators~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Apply Transform

#Define class for the transfrom operation
class TransformOperator(Operator):


    #Give the operation a name and label
    bl_idname = "object.transform_operator"
    bl_label = "Apply Transforms"

    #execute it the function
    def execute(self, context):

        #Apply the location, rotation, and scale of the objects
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        return {'FINISHED'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Recalculate Normals

#Define class for Recalculating Normals
class NormalsOperator(Operator):


    #Give the operation a name and label
    bl_idname = "object.normals_operator"
    bl_label = "Fix Normals"

    #execute it the function
    def execute(self, context):
        

        #Toggle edit mode
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')


        #Recalculate the normals on the ouside of the object
        bpy.ops.mesh.normals_make_consistent(inside=False)


        #Go out of edit mode
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Panel~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Create a class for the Panel
class QuickUI(bpy.types.Panel):
    
    bl_idname = 'VIEW3D_PT_example_panel'
    bl_label = 'Quick Transforms and UVs'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    

    #Create a a UI by drawing, and calling the classes of the functions
    def draw(self, context):
        
        layout = self.layout

        col = layout.column(align=True)


        #Get each operation that will be used for the panel
        col.operator(TransformOperator.bl_idname, text="Apply Transform", icon="ORIENTATION_CURSOR")
        col.operator(NormalsOperator.bl_idname, text="Fix Normals", icon="NORMALS_FACE")                 

#Register and Unregister the operations used in the panel

classes = (TransformOperator, NormalsOperator, QuickUI)
    
def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

if __name__ == "__main__":
    register()

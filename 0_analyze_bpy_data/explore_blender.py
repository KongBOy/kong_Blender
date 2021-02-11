import bpy

print("start")

data =  bpy.context.scene.objects["Cube"]
print(data)
print(dir(data))

bpy.context.scene.objects["Cube"].select_set(True)
#bpy.ops.object.select_all(action='DESELECT')
#bpy.ops.object.select_by_type(extend=True, type='MESH')
#bpy.ops.object.select_by_type(extend=True, type='LIGHT')
#bpy.ops.object.select_all(action='SELECT')

print("end")
import bpy 
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = None
mesh_ob = bpy.data.objects["result"]        ### 取得 物件
mesh_ob.select_set(True)
bpy.context.view_layer.objects.active = mesh_ob
bpy.ops.object.material_slot_add()

#bpy.context.view_layer.objects.active
import bpy

world = bpy.data.worlds['World']   ### 把內建的 World物件 抓出來
w_nodes = world.node_tree.nodes    ### World物件 預設nodes抓出來，預設會有 Background 和 World Output
w_links = world.node_tree.links    ### World物件 預設nodes之間的links抓出來
mapping = w_nodes.new(type='ShaderNodeMapping')       ### 建立 Mapping

print(dir(mapping))
print(mapping.inputs["Rotation"].default_value[2])
mapping.inputs["Rotation"].default_value[2] =3.14
第一行是 2.79 
第二行是 2.91

### render 切換到 GPU
bpy.context.user_preferences.addons["cycles"].preferences.compute_device_type  = "CUDA"
bpy.context.preferences.addons["cycles"].preferences.compute_device_type = "CUDA"


### 顏色管理
	scene.view_settings.view_transform = 'Default'
	scene.view_settings.view_transform = 'Standard'

	
### select/active 物件
	bpy.data.objects['Cube'].select = True
	bpy.data.objects['Cube'].select_set(True)

	bpy.context.scene.objects.active
	bpy.context.view_layer.objects.active

	

### Lamp 變成 Light
	bpy.data.lamps
	bpy.data.lights

	bpy.ops.object.add(type='LAMP', location=litpos)  ### 建立 lamp物件
	bpy.ops.object.add(type='LIGHT', location=litpos)  ### 建立 lamp物件

	Emission的強度 
		2.79：200~500
		2.91：20~50吧感覺要更小

	### world 的node 都跑到 "Shader Editor"的"World"裡面囉！
	mapping.rotation[2] = random.uniform(0, 6.28)
	mapping.inputs["Rotation"].default_value[2] = random.uniform(0, 6.28)

	

### Material 的node 都跑到"Shader Editor"的"Object"裡面囉！



### Render Layer相關的東西，node的東西 都跑到 "Compositor"裡面囉！
	bpy.ops.scene.render.layers.new("image_and_uv")
	bpy.ops.scene.view_layer_add(type='NEW')

	bpy.data.scenes['Scene'].render.layers
	bpy.data.scenes["Scene"].view_layers
    
    

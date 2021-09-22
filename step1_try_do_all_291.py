import bpy
import random
import os
import math
from mathutils import Vector, Euler

import sys
import shutil
import time
import datetime

def select_object(ob):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = None
    ob.select_set(True)
    bpy.context.view_layer.objects.active = ob

def get_rotation_around_axis_randomly(dist_range, x_rotate_range, z_rotate_range):
    ### 這段可參考 Working/2 Blender/try_mathutils.py，裡面有詳細註解！發現camera也有用這段，差別只是camera的 d設定2.3~3.3比較小、以X軸為旋轉軸轉60~120 角度不同而已
    dist = random.uniform(dist_range[0], dist_range[1])     ### 設定 燈 以原點為準 往y正方向的距離2.3~3.3
    x_rotate_rand = random.uniform(math.radians(x_rotate_range[0]), math.radians(x_rotate_range[1]))
    z_rotate_rand = random.uniform(math.radians(z_rotate_range[0]), math.radians(z_rotate_range[1]))
    print("x_rotate_range:", x_rotate_range, ", z_rotate_range:", z_rotate_range)
    print("x_rotate_rand:", math.degrees(x_rotate_rand), ", z_rotate_rand", math.degrees(z_rotate_rand))

    posi = Vector((0, dist, 0))            ### 設定 Blender 用的 Vector
    x_eul  = Euler((0, 0, 0), 'XYZ')       ### 設定 Blender 用的 Euler，x,z要分開，要不然共用的話，轉x軸的同時z軸也會跟著變喔！舉例 假如z轉90度，原本的x軸就變y軸了
    x_eul.rotate_axis('X', x_rotate_rand)  ### 以X軸為旋轉軸， 隨機在x_rotate_range[0]~x_rotate_range[1]度 旋轉(Y軸往右指 Z軸往上指，X軸往我們方向穿出時，以X為軸心 逆時鐘方向旋轉)
    z_eul  = Euler((0, 0, 0), 'XYZ')       ### 設定 Blender 用的 Euler，同上裡
    z_eul.rotate_axis('Z', z_rotate_rand)  ### 以Z軸為旋轉軸， 隨機在z_rotate_range[0]~z_rotate_range[0]度 旋轉(X軸往右指 Y軸往上指，Z軸往我們方向穿出時，以Z為軸心 逆時鐘方向旋轉)
    ### 注意順序有差！要先 轉x 再轉z
    posi.rotate(x_eul)                     ### 在Blender內把上面的操作換算成相對應的 (x,y,z) 座標，print不出來喔 因為是專門給Blender用的物件，要blender --python try_do.py 才看的到
    posi.rotate(z_eul)                     ### 在Blender內把上面的操作換算成相對應的 (x,y,z) 座標，print不出來喔 因為是專門給Blender用的物件，要blender --python try_do.py 才看的到
    return posi, dist
    # eul  = Euler((0, 0, 0), 'XYZ')  ### 設定 Blender 用的 Euler
    # ### 很重要，轉一定要注意順序 先Z 再X！反過來不相等喔！
    # eul.rotate_axis('Z', z_rotate_rand)  ### 以Z軸為旋轉軸， 隨機在z_rotate_range[0]~z_rotate_range[0]度 旋轉(X軸往右指 Y軸往上指，Z軸往我們方向穿出時，以Z為軸心 逆時鐘方向旋轉)
    # eul.rotate_axis('X', x_rotate_rand)  ### 以X軸為旋轉軸， 隨機在x_rotate_range[0]~x_rotate_range[1]度 旋轉(Y軸往右指 Z軸往上指，X軸往我們方向穿出時，以X為軸心 逆時鐘方向旋轉)
    # posi.rotate(eul)             ### 在Blender內把上面的操作換算成相對應的 (x,y,z) 座標，print不出來喔 因為是專門給Blender用的物件，要blender --python try_do.py 才看的到
    # return posi, dist

def step_0_remove_default_object():
    # only worry about data in the startup scene
    for bpy_data_iter in (bpy.data.meshes, bpy.data.lights, bpy.data.images, bpy.data.materials, bpy.data.worlds):
        for id_data in bpy_data_iter:
            bpy_data_iter.remove(id_data, do_unlink=True)


def step_0_prepare_scene():
    scene = bpy.data.scenes['Scene']
    scene.render.engine = 'CYCLES'
    scene.display_settings.display_device = 'sRGB'
    if random.random() > 0.5:
        scene.view_settings.view_transform = 'Filmic'
    else:
        scene.view_settings.view_transform = 'Standard'


def step_0_prepare_rendersettings():
    # bpy.context.preferences.addons["cycles"].preferences.compute_device_type = "CUDA"   ### 少這個下面改GPU也沒用喔！相當於進 Preference -> System -> 切換到 CUDA，好像執行一次後面都適用，但還是留著以免哪時候重新安裝Blender之類的情況
    scene = bpy.data.scenes['Scene']
    scene.cycles.device = 'GPU'   ### "CPU"
    scene.render.resolution_x = 512  ### int(1080 * 0.7)
    scene.render.resolution_y = 512  ### int(1080 * 0.7)
    scene.render.resolution_percentage = 100
    scene.cycles.samples = 128
    scene.cycles.use_square_samples = False



def step_1_get_obj_and_set_init_position(obj_path):
    bpy.ops.import_scene.obj(filepath=obj_path)  ### import 物件近來
    mesh_name = bpy.data.meshes[0].name          ### 取得 物件名字
    mesh_ob = bpy.data.objects[mesh_name]        ### 取得 物件
    mesh_ob.rotation_euler = [0.0, 0.0, 0.0]     ### 物件預設import近來 都會被預設轉 90度，把它反轉回來
    return mesh_ob


def step2_add_lighting(env_paths, point_light_rate=1.0):
    if random.random() <= point_light_rate:  # point light
        ###############################################################################################################################
        litpos, _ = get_rotation_around_axis_randomly(dist_range=(3, 5), x_rotate_range=(90, 90 + 45), z_rotate_range=(0, 360))
        ### Lamp物件
        bpy.ops.object.add(type='LIGHT', location=litpos)  ### 建立 lamp物件
        lamp = bpy.data.lights[0]                          ### 把建立的 lamp物件 抓出來
        lamp.use_nodes = True                             ### lamp物件 使用node 模式 來設定
        lamp_nodes = lamp.node_tree.nodes                 ### lamp物件 預設nodes抓出來，預設會有 Lamp Output 和 Emission，不用擔心 如果同Blender重複使用第二次以上，會有前次建立的 BlackBody，因為最一開始 step0 會刪掉 前一次的Lamp！本次新增的就不會有前次的東西囉！
        lamp_links = lamp.node_tree.links                 ### lamp物件 預設nodes之間的links抓出來

        ### Lamp物件 裡面的 Emission_node，來設定光的強度
        lamp_stren = lamp_nodes["Emission"]               ### 抓出預設建立的 Emission_node
        strngth = random.uniform(20, 50)                ### lamp光的強度設定值
        lamp_stren.inputs[1].default_value = strngth      ### lamp光的強度設定值 給 Emission_node

        ### Lamp物件 裡面的 Blackbody_node，來設定光的色溫，希望可以更貼近 自然光
        bbody = lamp_nodes.new(type='ShaderNodeBlackbody')      ### lamp的色溫node
        color_temper = random.uniform(2700, 10200)              ### lamp的色溫：淡黃~白~淡藍
        bbody.inputs[0].default_value = color_temper            ### lamp的色溫 設定給 Blackbody_node
        lamp_links.new(bbody.outputs[0], lamp_stren.inputs[0])  ### Blackbody -> Emission 連接上

    else:  # hdr world lighting
        print("hdr world light")
        ### World物件
        bpy.ops.world.new()                ### 建立 World物件
        world = bpy.data.worlds['World']   ### 把內建的 World物件 抓出來
        world.use_nodes = True             ### World物件 使用node 模式 來設定
        w_nodes = world.node_tree.nodes    ### World物件 預設nodes抓出來，預設會有 Background 和 World Output
        w_links = world.node_tree.links    ### World物件 預設nodes之間的links抓出來

        ### World物件 裡面的 Environment_Texture_node，可以 決定要用哪個.hdr當背景
        envnode = w_nodes.new(type='ShaderNodeTexEnvironment')  ### 建立 Environment_Texture_node
        idx = random.randint(0, len(env_paths) - 1)             ### 隨機取一個 env_index
        env_path = env_paths[idx]                               ### 隨機取一個 env_path
        print("env_path", env_path)
        envnode.image = bpy.data.images.load(env_path)          ### load env_path.hdr 進 blender

        ### World物件 裡面的 Texture_Coordinate_node，可以 調背景轉的角度 和
        texcoord = w_nodes.new(type='ShaderNodeTexCoord')     ### 建立 Texture_Coordinate_node
        mapping = w_nodes.new(type='ShaderNodeMapping')       ### 建立 Mapping
        mapping.inputs["Rotation"].default_value[2] = random.uniform(0, 6.28)  ###  ### 背景z：0~720度之間隨機轉個角度
        # mapping.rotation[2] = random.uniform(0, 6.28)         ### 背景0~720度之間隨機轉個角度


        ### World物件 裡面的 Background_node，可以 調背景強度
        bg_node = w_nodes['Background']                         ### 抓出預設建立的 Background_node
        envstr = 1  ### int(envp[1])，我看 DewarpNet 他們的 env.csv，第二個參數都設1，這裡乾脆直接指定囉~~
        bg_node.inputs[1].default_value = random.uniform(0.4 * envstr, 0.6 * envstr)  ### Background 的強度

        ### 把上面的 nodes 連起來
        w_links.new(texcoord.outputs[0], mapping.inputs[0])     ### Texture_Coordinate 的 Generated -> Mapping 的 Vector
        w_links.new(mapping.outputs[0] , envnode.inputs[0])     ### Mapping 的 Vector -> Environment_Texture 的 Vector
        w_links.new(envnode.outputs[0] , bg_node.inputs[0])     ### Environment_Texture 的 Color -> Background 的 C

        ## Blender 套用 上面 建好的 World物件
        bpy.context.scene.world = world

def step3_reset_camera():
    # bpy.ops.object.select_all(action='DESELECT')
    camera = bpy.data.objects['Camera']
    bpy.data.cameras['Camera'].lens = random.randint(40, 43)  ### ### focal length
    # cam position ### 原始 ### dist_range=(2.3, 3.3), x_rotate_range(90 - 30, 90 + 30), z_rotate_range=(0, 360)
    campos, dist = get_rotation_around_axis_randomly(dist_range=(0.4, 0.5), x_rotate_range=(90, 90 + 30), z_rotate_range=(0, 360))
    camera.location = campos

    # look at pos
    # st = (dist - 2.3) / 1.0 * 0.2 + 0.3
    # lookat = Vector((random.uniform(-st, st), random.uniform(-st, st), 0))
    lookat = Vector((0, 0, 0))  ### 先簡單的固定看原點
    eul = Euler((0, 0, 0), 'XYZ')  ### 這個eul 就要 x,y 共用了！get_rotation_around_axis_randomly 不一樣喔！
    x_angle = math.atan2(lookat.y - campos.y, campos.z)  ### 正方向 和 我們要轉的方向 相反 -(cam-look)
    y_angle = math.atan2(campos.x - lookat.x, campos.z)  ### 正方向 和 我們要轉的方向 相同   cam-look
    eul.rotate_axis('X', x_angle)  ### 以x軸為軸心(forward向我們)轉的正方向 和 我們要轉的方向 相反 -(cam-look)
    eul.rotate_axis('Y', y_angle)  ### 以y軸為軸心(forward向我們)轉的正方向 和 我們要轉的方向 相同   cam-look
    # st = (dist - 2.3) / 1.0 * 15 + 5.  ### 覺得目前先不用 以z軸為軸心 來轉，有餘力再寫
    # eul.rotate_axis('Z', random.uniform(math.0(-90 - st), math.radians(-90 + st)))

    print("lookat.y - campos.y", lookat.y - campos.y, ", x_angle", x_angle)
    print("campos.x - lookat.x", campos.x - lookat.x, ", y_angle", y_angle)
    print("eul", eul)

    camera.rotation_euler = eul
    # bpy.context.scene.update()


def step4_page_texture_1_image_and_uv_material(mesh_ob, tex_paths):
    select_object(mesh_ob)                        ### 一定要選到 mesh_ob 才能做 object.material_slot_add() 喔！
    bpy.ops.object.material_slot_add()            ### 相當於點  +  ，新增一個 slot，應該是texture的概念吧
    material = bpy.data.materials.new('image_and_uv')  ### 相當於點 new ，新增一個 material，命名為 image_and_uv
    mesh_ob.material_slots[0].material = material      ### slot(texture) 跟 material 關聯在一起

    material.use_nodes = True
    nodes = material.node_tree.nodes
    # clear default nodes
    for n in nodes: nodes.remove(n)
    out_node = nodes.new(type='ShaderNodeOutputMaterial')
    bsdf_node = nodes.new(type='ShaderNodeBsdfDiffuse')
    texture_node = nodes.new(type='ShaderNodeTexImage')
    ### 設定 Material node
    idx = random.randint(0, len(tex_paths) - 1)             ### 隨機取一個 tex_index
    tex_path = tex_paths[idx]                               ### 隨機取一個 tex_path
    print("tex_path", tex_path)
    texture_node.image = bpy.data.images.load(tex_path)     ### 把

    links = material.node_tree.links
    links.new(bsdf_node.outputs[0], out_node.inputs[0])
    links.new(texture_node.outputs[0], bsdf_node.inputs[0])

    bsdf_node.inputs[0].show_expanded = True
    texture_node.extension = 'EXTEND'
    texturecoord_node = nodes.new(type='ShaderNodeTexCoord')
    links.new(texture_node.inputs[0], texturecoord_node.outputs[2])




def step4_page_texture_2_wc_material(mesh_ob):
    bpy.ops.object.material_slot_add()
    material = bpy.data.materials.new("wc")
    mesh_ob.material_slots[1].material = material
    material.use_nodes = True
    wc_nodes = material.node_tree.nodes
    for n in wc_nodes: wc_nodes.remove(n)
    out_node = wc_nodes.new(type='ShaderNodeOutputMaterial')
    em_node = wc_nodes.new(type='ShaderNodeEmission')
    geometry_node = wc_nodes.new(type='ShaderNodeNewGeometry')

    wc_links = material.node_tree.links
    wc_links.new(em_node.outputs[0], out_node.inputs[0])
    wc_links.new(geometry_node.outputs[0], em_node.inputs[0])


def step5_render_pass(out_path, save_blend=False):
    scene = bpy.data.scenes['Scene']                       ### 把內建的 Scene物件 抓出來
    #############################################################################################################
    ### RenderLayer ( bpy.data.scenes['Scene'].render.layers )
    render_layers = scene.view_layers
    for l in render_layers:  ### 因為Blender本身的限制，在step0的時候無法刪除所有的RenderLayers，所以我們要手動刪除 上次執行Blender生成的Renderlayers，且要留下 預設的RenderLayer 才行喔！
        if(l.name != "View Layer"): render_layers.remove(l)  ### 除了預設的 RenderLayer 以外 的 Layer都刪掉

    rlayer_image_and_uv = render_layers.new("image_and_uv")  ### "image_and_uv"_RenderLayer 的建立
    rlayer_image_and_uv.use_pass_uv = True                   ### "image_and_uv"_RenderLayers 的 node 才能夠輸出 UV output
    rlayer_image_and_uv.material_override = bpy.data.materials["image_and_uv"]  ### "image_and_uv"_Render_Layer 套用 "image_and_uv"_Material

    rlayer_wc = render_layers.new("wc")                     ### "wc"_RenderLayer 的建立
    rlayer_wc.material_override = bpy.data.materials["wc"]  ### "wc"_RenderLayer 套用 "wc"_Material
    rlayer_wc.use_sky = False
    #############################################################################################################
    ### Render Nodes ( Render方面的node藏在 Scene物件裡喔！bpy.data.scenes['Scene'].node_tree.nodes/links)
    scene.use_nodes = True                                 ### Render方面的node藏在 Scene物件裡喔！ 先抓出 Scene 並使用node 模式 來設定
    render_nodes = scene.node_tree.nodes                   ### Render方面的node藏在 Scene物件裡喔！ Scene物件 預設nodes抓出來，預設會有 Render_Layers 和 Composite
    render_links = scene.node_tree.links                   ### Render方面的node藏在 Scene物件裡喔！ Scene物件 預設nodes之間的links抓出來
    for n in render_nodes: render_nodes.remove(n)          ### 清空所有default nodes
    ##################################################
    ### 設定 image_and_uv / wc 的 Render_Layers_node
    ##### image_and_uv 方面
    render_layers_image_and_uv_node = render_nodes.new('CompositorNodeRLayers')  ### "image_and_uv"_RenderLayer_node 的建立
    render_layers_image_and_uv_node.layer = "image_and_uv"                       ### "image_and_uv"_RenderLayer_node 套用 "image_and_uv"_RenderLayer
    ##### wc 方面
    render_layers_wc = render_nodes.new('CompositorNodeRLayers')                 ### "wc"_RenderLayer_node 的建立
    render_layers_wc.layer = "wc"                                                ### "wc"_RenderLayer_node 套用 "wc"_RenderLayer
    ##################################################
    ### 設定 File_Output_node，並且跟前面的 相對應的 RenderLayer_node連接起來
    out_node = render_nodes.new('CompositorNodeOutputFile')         ### 建立 File_Output_node
    out_node.base_path = out_path                                   ### 指定 輸出資料夾
    ##### image方面
    out_node.file_slots[0].path = "0_image-"                         ### 指定 "image" 的輸出檔名
    out_node.format.file_format = 'PNG'                             ### 指定 PNG (這是base格式)
    render_links.new(render_layers_image_and_uv_node.outputs["Image"], out_node.inputs["Image"])  ### "image_and_uv"_RenderLayer_node 的 Image -> File_Output_node 的 Image(這Image是預設的，內部操作無法改名，但顯示上 和 實際輸出 其實都是 0_image囉！)
    ##### uv方面
    uv_out_name = "1_uv-"                                           ### 多個 "-" 是因為 Blender 2.79 沒辦法設定 輸出檔名 frame_index 怎麼加，為了好看自己加個 "-" 做區隔，下面全部同理
    out_node.file_slots.new(uv_out_name)                            ### 建立 "uv" 的輸出檔名
    out_node.file_slots[1].use_node_format = False                  ### 設定 不要用 最上面base格式
    out_node.file_slots[1].format.file_format = "OPEN_EXR"          ### 指定 OPEN_EXR
    render_links.new(render_layers_image_and_uv_node.outputs["UV"], out_node.inputs[uv_out_name])  ### "image_and_uv"_RenderLayer_node 的 UV -> File_Output_node 的 1_uv
    uv_image_out_name = "1_uv_image-"
    out_node.file_slots.new(uv_image_out_name)                      ### 建立 "uv_image" 的輸出檔名，這是視覺化用的
    out_node.file_slots[2].use_node_format = False                  ### 設定 不要用 最上面base格式
    out_node.file_slots[2].format.file_format = "PNG"               ### 指定 PNG
    render_links.new(render_layers_image_and_uv_node.outputs["UV"], out_node.inputs[uv_image_out_name])  ### "image_and_uv"_RenderLayer_node 的 UV -> File_Output_node 的 1_uv_image
    ##### wc方面
    wc_out_name = "2_wc-"
    out_node.file_slots.new(wc_out_name)                            ### 建立 "wc" 的輸出檔名
    out_node.file_slots[3].use_node_format = False                  ### 設定 不要用 最上面base格式
    out_node.file_slots[3].format.file_format = "OPEN_EXR"          ### 指定 OPEN_EXR
    render_links.new(render_layers_wc.outputs["Image"], out_node.inputs[wc_out_name])  ### "wc"_RenderLayer_node 的 Image -> File_Output_node 的 2_wc
    wc_image_out_name = "2_wc_image-"
    out_node.file_slots.new(wc_image_out_name)                      ### 建立 "wc_image" 的輸出檔名，這是視覺化用的
    out_node.file_slots[4].use_node_format = False                  ### 設定 不要用 最上面base格式
    out_node.file_slots[4].format.file_format = "PNG"               ### 指定 PNG
    render_links.new(render_layers_wc.outputs["Image"], out_node.inputs[wc_image_out_name])  ### "wc"_RenderLayer_node 的 Image -> File_Output_node 的 2_wc_image
    ####################################################################################################
    bpy.ops.render.render(write_still=False)  ### Render 出影像，Blender2.79 檔名後面會自動加 frame_index 喔！

    frame_index = bpy.data.scenes["Scene"].frame_current  ### 抓出目前的 frame_index，給 .blend 當index
    if save_blend: bpy.ops.wm.save_mainfile(filepath=out_path + "/" + 'Blender_file_%04i.blend' % frame_index)  ### 將目前編輯到現在的 Blender 存一份起來

    bpy.data.scenes["Scene"].frame_current += 1  ### frame_index更新 給下次 Render用


# disk_index = "L"  ### 127.35
# disk_index = "H"  ### HP820G1
disk_index = "D"  ### 127.35 2021/09/15

sys.path.append(disk_index + r":\Working\5 Python write Blender")

env_dir = disk_index + r":\Working\2 Blender\data_dir\0_ord\env"
env_names = [env_name for env_name in os.listdir(env_dir) if ".hdr" in env_name]
env_paths = [env_dir + "/" + env_name for env_name in env_names]
# from step0_get_dtd_img_path import dtd_img_paths
# env_paths = dtd_img_paths
print(env_paths)


# tex_dir = disk_index + r":\Working\2 Blender\data_dir\0_ord\tex"
# tex_names = [tex_name for tex_name in os.listdir(tex_dir) if ".jpg" in tex_name]
# tex_paths = [tex_dir + "/" + tex_name for tex_name in tex_names]
from step0_get_os_img_paths import os_img_paths
tex_paths = os_img_paths
print(tex_paths)

# obj_dir = disk_index + r":\Working\3 RealScene_to_Blender\analyze2_image_uv_wc\result_smooth_Lamp_Camera_RenderLayer_ok"
obj_dir = disk_index + r":\Working\3 RealScene_to_Blender\analyze3_unwarp_compare_and_image_uv_wc\2 umwarp method compare"  ### 2021/09/15
obj_names = ["try1_triangle_uv1_unwarp_small",
         "try1_triangle_uv2_unwarp_big",
         "try1_triangle_uv3_project_from_view",
         "try2_square_then_prone_uv1_unwarp_small",
         "try2_square_then_prone_uv2_unwarp_big",
         "try2_square_then_prone_uv3_project_from_view"]
obj_paths = [obj_dir + "/" + obj_name + "/" + obj_name + "_remove_node.obj" for obj_name in obj_names]
# print(obj_paths)


if __name__ == "__main__":
    # blender --python try_do.py
    # out_path = obj_dir + "/" + obj_names[0]
    # out_path = r"C:\Users\TKU\Desktop\temp"
    # out_path = r"C:\Users\HP820G1\Desktop\temp"
    # out_path = r"G:\kong_render_os_book_no_bg_768_testGPU"
    out_path = r"J:\kong_render_os_book_all_have_bg_512"
    os.makedirs(out_path, exist_ok=True)
    python_code = __file__.split("\\")[-1]
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copy(python_code, out_path + "/" + python_code.replace(".py", f"_{current_time}.py"))

    obj_path = obj_paths[0]
    print("obj_path~~~", obj_path)
    # for obj_path in obj_paths[:]:
    start_time = time.time()
    for _ in range(1000):
        step_0_remove_default_object()   # 刪掉Blender預設的 Cubic 和 Lamp 之類的東西
        step_0_prepare_scene()           # 設定 基礎環境
        step_0_prepare_rendersettings()  # 設定 Render參數

        mesh_ob = step_1_get_obj_and_set_init_position(obj_path=obj_path)  # 把物件放平

        step2_add_lighting(env_paths, point_light_rate=0.0)
        step3_reset_camera()
        step4_page_texture_1_image_and_uv_material(mesh_ob, tex_paths)
        step4_page_texture_2_wc_material(mesh_ob)
        step5_render_pass(out_path, save_blend=True)
    print("cost_time:", time.time() - start_time)  ### cost_time: 8341.265739917755


import bpy
import random
import math
from mathutils import Vector, Euler

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
    # eul.rotate_axis('X', x_rotate_rand)  ### 以X軸為s旋轉軸， 隨機在x_rotate_range[0]~x_rotate_range[1]度 旋轉(Y軸往右指 Z軸往上指，X軸往我們方向穿出時，以X為軸心 逆時鐘方向旋轉)
    # posi.rotate(eul)             ### 在Blender內把上面的操作換算成相對應的 (x,y,z) 座標，print不出來喔 因為是專門給Blender用的物件，要blender --python try_do.py 才看的到
    # return posi, dist

### 把上次的 point light 刪掉
for light in (bpy.data.lights): bpy.data.lights.remove(light)

litpos, _ = get_rotation_around_axis_randomly(dist_range=(0.5, 0.5), x_rotate_range=(90, 90 + 45), z_rotate_range=(0, 360))
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

'''
設定 各個 obj 的來源
'''
from step0_disk_index import Working_disk_index

# obj_dir = f"{Working_disk_index}:/Working/3 RealScene_to_Blender/analyze2_image_uv_wc/result_smooth_Lamp_Camera_RenderLayer_ok"
obj_dir = f"{Working_disk_index}:/Working/3 RealScene_to_Blender/analyze3_unwarp_compare_and_image_uv_wc/2 umwarp method compare"  ### 2021/09/15

obj_names = ["try1_triangle_uv1_unwarp_small",
         "try1_triangle_uv2_unwarp_big",
         "try1_triangle_uv3_project_from_view",
         "try2_square_then_prone_uv1_unwarp_small",
         "try2_square_then_prone_uv2_unwarp_big",
         "try2_square_then_prone_uv3_project_from_view"]

obj_paths = []
obj_paths += [obj_dir + "/" + obj_name + "/" + obj_name + "_remove_node.obj" for obj_name in obj_names]

if __name__ == '__main__':
    print("obj_paths", obj_paths)

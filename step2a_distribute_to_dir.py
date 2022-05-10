#############################################################################################################################################################################################################
#############################################################################################################################################################################################################
### 把 kong_model2 加入 sys.path
import os
code_exe_path = os.path.realpath(__file__)                   ### 目前執行 step10_b.py 的 path
code_exe_path_element = code_exe_path.split("\\")            ### 把 path 切分 等等 要找出 kong_model 在第幾層
kong_layer = code_exe_path_element.index("kong_model2")      ### 找出 kong_model2 在第幾層
kong_model2_dir = "\\".join(code_exe_path_element[:kong_layer + 1])  ### 定位出 kong_model2 的 dir
import sys                                                   ### 把 kong_model2 加入 sys.path
sys.path.append(kong_model2_dir)
# print(__file__.split("\\")[-1])
# print("    code_exe_path:", code_exe_path)
# print("    code_exe_path_element:", code_exe_path_element)
# print("    kong_layer:", kong_layer)
# print("    kong_model2_dir:", kong_model2_dir)
#############################################################################################################################################################################################################
from kong_util.util import get_dir_certain_file_names
from kong_util.build_dataset_combine import Check_dir_exist_and_build
import shutil
from step0_disk_index import render_out_dir

image_ord_dir     = render_out_dir
uv_ord_dir        = render_out_dir
uv_visual_ord_dir = render_out_dir
wc_ord_dir        = render_out_dir
wc_visual_ord_dir = render_out_dir
image_dst_dir     = render_out_dir + "/" + "0_image"
uv_dst_dir        = render_out_dir + "/" + "1_uv"
uv_visual_dst_dir = render_out_dir + "/" + "1_uv_visual"
wc_dst_dir        = render_out_dir + "/" + "2_wc"
wc_visual_dst_dir = render_out_dir + "/" + "2_wc_visual"

def grab_ord_dir_certain_file_to_dst_dir(ord_dir, certain_word, certain_ext, dst_dir, print_msg=False):
    Check_dir_exist_and_build(dst_dir)  ### 建立 dst_dir， 不可以用 build_new_dir 喔！ 要不然執行第二次以上 dst_dir 的東西就會被刪掉

    file_names = get_dir_certain_file_names(ord_dir=ord_dir, certain_word=certain_word, certain_ext=certain_ext)
    for file_name in file_names:
        ord_path = ord_dir + "/" + file_name
        dst_path = dst_dir + "/" + file_name
        shutil.move(ord_path, dst_path)
        if(print_msg): print(ord_path, "->", dst_path, "finish~")

def blender_render_result_split_to_dir(render_out_dir):
    grab_ord_dir_certain_file_to_dst_dir(ord_dir=image_ord_dir,     certain_word="0_image",    certain_ext=".png", dst_dir=image_dst_dir,     print_msg=True)
    grab_ord_dir_certain_file_to_dst_dir(ord_dir=uv_ord_dir,        certain_word="1_uv",       certain_ext=".exr", dst_dir=uv_dst_dir,        print_msg=True)
    grab_ord_dir_certain_file_to_dst_dir(ord_dir=uv_visual_ord_dir, certain_word="1_uv_image", certain_ext=".png", dst_dir=uv_visual_dst_dir, print_msg=True)
    grab_ord_dir_certain_file_to_dst_dir(ord_dir=wc_ord_dir,        certain_word="2_wc",       certain_ext=".exr", dst_dir=wc_dst_dir,        print_msg=True)
    grab_ord_dir_certain_file_to_dst_dir(ord_dir=wc_visual_ord_dir, certain_word="2_wc_image", certain_ext=".png", dst_dir=wc_visual_dst_dir, print_msg=True)


if(__name__ == "__main__"):
    blender_render_result_split_to_dir(render_out_dir)

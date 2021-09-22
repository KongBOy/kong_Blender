import sys
sys.path.append("../kong_util")

from blender_util import get_dir_blends_and_extract_texture_image_file_name
from util import get_dir_certain_file_name
from build_dataset_combine import Check_dir_exist_and_build
import shutil

def grab_ord_dir_certain_file_to_dst_dir(ord_dir, certain_word, certain_ext, dst_dir, print_msg=False):
    Check_dir_exist_and_build(dst_dir)  ### 建立 dst_dir， 不可以用 build_new_dir 喔！ 要不然執行第二次以上 dst_dir 的東西就會被刪掉

    file_names = get_dir_certain_file_name(ord_dir=ord_dir, certain_word=certain_word, certain_ext=certain_ext)
    for file_name in file_names:
        ord_path = ord_dir + "/" + file_name
        dst_path = dst_dir + "/" + file_name
        shutil.move(ord_path, dst_path)
        if(print_msg): print(ord_path, "->", dst_path, "finish~")

def blender_render_result_split_to_dir(root_dir):
    image_ord_dir = root_dir
    image_dst_dir = root_dir + "/" + "0_image"
    grab_ord_dir_certain_file_to_dst_dir(ord_dir=image_ord_dir, certain_word="0_image", certain_ext=".png", dst_dir=image_dst_dir, print_msg=True)

    uv_ord_dir = root_dir
    uv_dst_dir = root_dir + "/" + "1_uv"
    grab_ord_dir_certain_file_to_dst_dir(ord_dir=uv_ord_dir, certain_word="1_uv", certain_ext=".exr", dst_dir=uv_dst_dir, print_msg=True)

    uv_visual_ord_dir = root_dir
    uv_visual_dst_dir = root_dir + "/" + "1_uv_visual"
    grab_ord_dir_certain_file_to_dst_dir(ord_dir=uv_visual_ord_dir, certain_word="1_uv_image", certain_ext=".png", dst_dir=uv_visual_dst_dir, print_msg=True)

    wc_ord_dir = root_dir
    wc_dst_dir = root_dir + "/" + "2_wc"
    grab_ord_dir_certain_file_to_dst_dir(ord_dir=wc_ord_dir, certain_word="2_wc", certain_ext=".exr", dst_dir=wc_dst_dir, print_msg=True)

    wc_visual_ord_dir = root_dir
    wc_visual_dst_dir = root_dir + "/" + "2_wc_visual"
    grab_ord_dir_certain_file_to_dst_dir(ord_dir=wc_visual_ord_dir, certain_word="2_wc_image", certain_ext=".png", dst_dir=wc_visual_dst_dir, print_msg=True)


if(__name__ == "__main__"):
    # root_dir = "J:/kong_render_os_book_have_bg_512"
    root_dir = "J:/kong_render_os_book_all_have_bg_512"

    blender_render_result_split_to_dir(root_dir)

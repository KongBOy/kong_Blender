import sys
sys.path.append("../kong_util")

from blender_util import get_dir_blends_and_extract_texture_image_file_name

if(__name__ == "__main__"):
    '''
    執行的時候要在cmd裡面打指令：blender --background --python blender_util.py
    '''

    # root_dir = "J:/kong_render_os_book_no_bg_768"
    # root_dir = "J:/kong_render_os_book_have_bg_512"
    root_dir = "J:/kong_render_os_book_all_have_bg_512"

    get_dir_blends_and_extract_texture_image_file_name(page_ord_dir="J:/0 data_dir/datasets/type7_cut_os_book/produce_straight/01_page_num_ok",
                                                       blender_ord_dir=root_dir,
                                                       dst_dir=root_dir + "/0_image_ord")

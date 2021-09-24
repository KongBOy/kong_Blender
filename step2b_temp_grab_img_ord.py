import sys
sys.path.append("../kong_util")

from blender_util import get_dir_blends_and_extract_texture_image_file_name

if(__name__ == "__main__"):
    '''
    執行的時候要在cmd裡面打指令：blender --background --python step2b_temp_grab_img_ord.py
    '''
    from step0_disk_index import render_out_dir

    get_dir_blends_and_extract_texture_image_file_name(page_ord_dir="J:/0 data_dir/datasets/type7_cut_os_book/produce_straight/01_page_num_ok",
                                                       blender_ord_dir=render_out_dir,
                                                       dst_dir=render_out_dir + "/0_image_ord")

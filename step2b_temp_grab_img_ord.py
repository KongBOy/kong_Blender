import sys
sys.path.append(".")
sys.path.append("../kong_util")

from kong_util.blender_util import get_dir_blends_and_extract_texture_image_file_name

if(__name__ == "__main__"):
    '''
    執行的時候要在cmd裡面打指令：blender --background --python step2b_temp_grab_img_ord.py
    '''
    from step0_disk_index import render_out_dir

    get_dir_blends_and_extract_texture_image_file_name(blender_ord_dir=render_out_dir,
                                                       dst_dir=render_out_dir + "/0_image_ord")

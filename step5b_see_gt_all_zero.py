#############################################################################################################################################################################################################
### 把 kong_model2 加入 sys.path
import os
code_exe_path = os.path.realpath(__file__)                   ### 目前執行 step10_b.py 的 path
code_exe_path_element = code_exe_path.split("\\")            ### 把 path 切分 等等 要找出 kong_model 在第幾層
kong_layer = code_exe_path_element.index("kong_model2")      ### 找出 kong_model2 在第幾層
kong_model2_dir = "\\".join(code_exe_path_element[:kong_layer + 1])    ### 定位出 kong_model2 的 dir
import sys                                                   ### 把 kong_model2 加入 sys.path
sys.path.append(kong_model2_dir)
# print(__file__.split("\\")[-1])
# print("    code_exe_path:", code_exe_path)
# print("    code_exe_path_element:", code_exe_path_element)
# print("    kong_layer:", kong_layer)
# print("    kong_model2_dir:", kong_model2_dir)
#############################################################################################################################################################################################################
sys.path.append(kong_model2_dir + "/kong_util")
#############################################################################################################################################################################################################
from build_dataset_combine import  Save_npy_dir_as_knpy, Check_dir_exist_and_build
import numpy as np

def save_all_zero_gt_flow(datasets_dir, gt_size, ch=3, repeat=1, comment="see_gt_is_real_photo_has_no_gt_flow"):
    Check_dir_exist_and_build(datasets_dir)
    all_zero = np.zeros(shape=(gt_size, gt_size, ch), dtype=np.float32)
    for i in range(repeat):
        np.save(datasets_dir + "/" + f"0_{comment}(all_zero_size{gt_size})_{i + 1}", all_zero)
        Save_npy_dir_as_knpy(datasets_dir, datasets_dir)

###################################################
# save_all_zero_gt_flow(datasets_dir = "J:/kong_render_os_book_no_bg_768/datasets/blender_os_hw768/see",        gt_size=512, ch=3, repeat= 4, comment="see_gt_is_real_photo_has_no_gt_flow")
# save_all_zero_gt_flow(datasets_dir = "J:/kong_render_os_book_all_have_bg_512/datasets/blender_os_hw512/see",  gt_size=512, ch=3, repeat= 4, comment="see_gt_is_real_photo_has_no_gt_flow")
# save_all_zero_gt_flow(datasets_dir = "J:/kong_render_os_book_all_have_bg_512/datasets/blender_os_hw512_have_bg/test", gt_size=512, ch=3, repeat=16, comment="test_gt_use_real_photo_has_no_gt_flow")
save_all_zero_gt_flow(datasets_dir = "K:/kong_render_os_book_and_paper_all_have_dtd_hdr_mix_bg_512/os_and_paper_hw512_dtd_hdr_mix_bg_I_to_W/os_and_paper_hw512_dtd_hdr_bg_I_to_W", gt_size=512, ch=4, repeat=4, comment="test_gt_use_real_photo_has_no_gt_W")

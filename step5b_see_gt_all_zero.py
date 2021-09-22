import numpy as np
import sys
sys.path.append("../kong_util")

from build_dataset_combine import  Save_npy_as_knpy, Check_dir_exist_and_build


def save_all_zero_gt_flow(datasets_dir, gt_size, repeat=1, comment="see_gt_is_real_photo_has_no_gt_flow"):
    Check_dir_exist_and_build(datasets_dir)
    all_zero = np.zeros(shape=(gt_size, gt_size, 3), dtype=np.float32)
    for i in range(repeat):
        np.save(datasets_dir + "/" + f"0_{comment}(all_zero_size{gt_size})_{i + 1}", all_zero)
        Save_npy_as_knpy(datasets_dir, datasets_dir)

###################################################
# save_all_zero_gt_flow(datasets_dir = "J:/kong_render_os_book_no_bg_768/datasets/blender_os_hw768/see",        gt_size=512, repeat= 4, comment="see_gt_is_real_photo_has_no_gt_flow")
# save_all_zero_gt_flow(datasets_dir = "J:/kong_render_os_book_all_have_bg_512/datasets/blender_os_hw512/see",  gt_size=512, repeat= 4, comment="see_gt_is_real_photo_has_no_gt_flow")
save_all_zero_gt_flow(datasets_dir = "J:/kong_render_os_book_all_have_bg_512/datasets/blender_os_hw512_have_bg/test", gt_size=512, repeat=16, comment="test_gt_use_real_photo_has_no_gt_flow")

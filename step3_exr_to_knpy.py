import sys
sys.path.append("../kong_util")

from build_dataset_combine import Save_exr_as_npy, Save_npy_as_knpy


def dir_exr_to_npy_to_knpy(exr_ord_dir, npy_dst_dir, knpy_dst_dir):
    Save_exr_as_npy(exr_ord_dir, npy_dst_dir)
    Save_npy_as_knpy(npy_dst_dir, knpy_dst_dir)

if(__name__ == "__main__"):
    # root_dir = r"G:\kong_render_os_book_no_bg"          ### 在 2T Doc3D 硬碟裡
    # root_dir = r"G:\kong_render_os_book_no_bg_768"      ### 在 2T Doc3D 硬碟裡
    root_dir = r"J:\kong_render_os_book_all_have_bg_512"  ### 在 2T Doc3D 硬碟裡 2021/09/19

    uv_name = "1_uv"
    uv_exr_ord_dir  = root_dir + "/" + uv_name
    uv_npy_dst_dir  = root_dir + "/" + uv_name + "_npy"
    uv_knpy_dst_dir = root_dir + "/" + uv_name + "_knpy"
    dir_exr_to_npy_to_knpy(uv_exr_ord_dir, uv_npy_dst_dir, uv_knpy_dst_dir)

    wc_name = "2_wc"
    wc_exr_ord_dir  = root_dir + "/" + wc_name
    wc_npy_dst_dir  = root_dir + "/" + wc_name + "_npy"
    wc_knpy_dst_dir = root_dir + "/" + wc_name + "_knpy"
    dir_exr_to_npy_to_knpy(wc_exr_ord_dir, wc_npy_dst_dir, wc_knpy_dst_dir)

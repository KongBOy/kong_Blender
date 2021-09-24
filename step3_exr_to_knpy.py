import sys
sys.path.append("../kong_util")

from build_dataset_combine import Save_exr_as_npy, Save_npy_as_knpy


def dir_exr_to_npy_to_knpy(exr_ord_dir, npy_dst_dir, knpy_dst_dir):
    Save_exr_as_npy(exr_ord_dir, npy_dst_dir)
    Save_npy_as_knpy(npy_dst_dir, knpy_dst_dir)

if(__name__ == "__main__"):
    from step0_disk_index import render_out_dir

    uv_name = "1_uv"
    uv_exr_ord_dir  = render_out_dir + "/" + uv_name
    uv_npy_dst_dir  = render_out_dir + "/" + uv_name + "_npy"
    uv_knpy_dst_dir = render_out_dir + "/" + uv_name + "_knpy"
    dir_exr_to_npy_to_knpy(uv_exr_ord_dir, uv_npy_dst_dir, uv_knpy_dst_dir)

    wc_name = "2_wc"
    wc_exr_ord_dir  = render_out_dir + "/" + wc_name
    wc_npy_dst_dir  = render_out_dir + "/" + wc_name + "_npy"
    wc_knpy_dst_dir = render_out_dir + "/" + wc_name + "_knpy"
    dir_exr_to_npy_to_knpy(wc_exr_ord_dir, wc_npy_dst_dir, wc_knpy_dst_dir)

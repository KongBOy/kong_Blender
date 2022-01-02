import sys
sys.path.append("kong_util")
from step0_disk_index import render_out_dir
from build_dataset_combine import Save_exr_as_npy2, Save_npy_dir_as_knpy, Check_dir_exist_and_build

import os
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def dir_exr_to_npy_to_knpy(exr_ord_dir, npy_dst_dir, knpy_dst_dir):
    Save_exr_as_npy2(exr_ord_dir, npy_dst_dir)
    Save_npy_dir_as_knpy(npy_dst_dir, knpy_dst_dir)

if(__name__ == "__main__"):

    '''exr -> npy -> knpy'''
    uv_name = "1_uv"
    uv_exr_ord_dir  = render_out_dir + "/" + uv_name
    uv_npy_dst_dir  = render_out_dir + "/" + uv_name + "_npy"
    uv_knpy_dst_dir = render_out_dir + "/" + uv_name + "_knpy"
    # dir_exr_to_npy_to_knpy(uv_exr_ord_dir, uv_npy_dst_dir, uv_knpy_dst_dir)

    '''exr -> npy -> add_M -> knpy'''
    wc_name = "2_wc"
    wc_exr_ord_dir  = f"{render_out_dir}/{wc_name}"
    wc_npy_dst_dir  = f"{render_out_dir}/{wc_name}_npy"  ### exr   -> npy
    wc_w_M_dst_dir  = f"{render_out_dir}/{wc_name}_w_M_npy"  ### npy   -> add_M 
    wc_knpy_dst_dir = f"{render_out_dir}/{wc_name}_knpy" ### add_M -> knpy
    # Save_exr_as_npy2(wc_exr_ord_dir, wc_npy_dst_dir)  ### exr -> npy

    Check_dir_exist_and_build(wc_w_M_dst_dir)
    for uv_filename, wc_filename in tqdm(zip( os.listdir(uv_npy_dst_dir), os.listdir(wc_npy_dst_dir) ) ):
        uv_path = f"{uv_npy_dst_dir}/{uv_filename}"
        wc_path = f"{wc_npy_dst_dir}/{wc_filename}"
        uv = np.load(uv_path)
        wc = np.load(wc_path)
        mask = uv[..., 0]
        wc[..., 3] = mask

        ### 視覺化一下看看有沒有寫錯
        # fig, ax = plt.subplots(1, 4, figsize=(20, 5))
        # ax[0].imshow(wc[..., 0])
        # ax[1].imshow(wc[..., 1])
        # ax[2].imshow(wc[..., 2])
        # ax[3].imshow(wc[..., 3])
        # plt.show()
        # print(wc.shape)

        dst_path = f"{wc_w_M_dst_dir}/{wc_filename}"
        np.save(dst_path, wc)


    Save_npy_dir_as_knpy(wc_w_M_dst_dir, wc_knpy_dst_dir)



    # uv_name = "1_uv"
    # uv_npy_dst_dir  = "H:/Doc3D" + "/" + uv_name + "_npy"
    # uv_knpy_dst_dir = "H:/Doc3D" + "/" + uv_name + "_knpy"
    # for i in range(1, 21 + 1):
    #     start_time = time.time()
    #     uv_exr_ord_dir  = f"J:/swat3D/uv/{i}"
    #     Save_exr_as_npy2(uv_exr_ord_dir, uv_npy_dst_dir)
    #     print("one dir Save_exr_as_npy2 cost time:", time.time() - start_time)
    # Save_npy_dir_as_knpy(uv_npy_dst_dir, uv_knpy_dst_dir, core_amount=30)

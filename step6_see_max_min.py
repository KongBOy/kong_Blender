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
sys.path.append(kong_model2_dir + "/kong_util")
# print(__file__.split("\\")[-1])
# print("    code_exe_path:", code_exe_path)
# print("    code_exe_path_element:", code_exe_path_element)
# print("    kong_layer:", kong_layer)
# print("    kong_model2_dir:", kong_model2_dir)
#############################################################################################################################################################################################################
from kong_util.util import get_dir_npys
from step0_disk_index import render_out_dir

from step3_exr_to_knpy import uv_npy_dst_dir, wc_w_M_dst_dir, uv_name
render_out_uv_npy_dir = uv_npy_dst_dir  ### f"{render_out_dir}/1_uv_npy"
render_out_wc_npy_dir = wc_w_M_dst_dir  ### f"{render_out_dir}/2_wc_w_M_npy"
''' 注意！ 要把Mask 排除在外 來看 max 才是準的， 因為 Mask 的 max 一定是一， 這樣就看不到 data 的 max 了！'''
uvs = get_dir_npys(render_out_uv_npy_dir)
Cs = uvs[:, :, :, 1:3]
M  = uvs[:, :, :, 0:1]
Cy = uvs[:, :, :, 1:2]  ### 0.0 ~ 0.9980217
Cx = uvs[:, :, :, 2:3]  ### 0.0 ~ 0.9757899

#############################################################
WM = get_dir_npys(render_out_wc_npy_dir)
Ws  = WM[:, :, :, :3]   ### -0.13539262 ~ 0.1357405
Wz = WM[:, :, :, 0:1]  ###  0.0        ~ 0.039187048
Wy = WM[:, :, :, 1:2]  ### -0.13532962 ~ 0.1357405
Wx = WM[:, :, :, 2:3]  ### -0.08075158 ~ 0.07755918
M  = WM[:, :, :, 3:4]

from step2a_distribute_to_dir import uv_visual_dst_dir, wc_visual_dst_dir
from kong_util.util import get_dir_certain_file_names
from kong_util.build_dataset_combine import Check_dir_exist_and_build
import cv2
import numpy as np
uv_npy_file_names = get_dir_certain_file_names(render_out_uv_npy_dir, certain_word=".npy")
wc_npy_file_names = get_dir_certain_file_names(render_out_wc_npy_dir, certain_word=".npy")
uv_ch_visual_dst_dir = uv_visual_dst_dir + f"/ch_visual"
wc_ch_visual_dst_dir = wc_visual_dst_dir + f"/ch_visual"
Check_dir_exist_and_build(uv_ch_visual_dst_dir)
Check_dir_exist_and_build(wc_ch_visual_dst_dir)
# uv_max = Cs.max()
# uv_mub = Cs.min()
# wc_max = Ws.max()
# wc_mub = Ws.min()
uv_max = 0.9980217
uv_mub = 0.0
wc_max = 0.1357405
wc_min = -0.13539262
Cx_visual = (Cx * 255).astype(np.uint8)
Cy_visual = (Cy * 255).astype(np.uint8)
W_visual  = ( ( (Ws - wc_min) / (wc_max - wc_min) ) * M * 255 ).astype(np.uint8)
Wz_visual = ( ( (Wz - wc_min) / (wc_max - wc_min) ) * M * 255 ).astype(np.uint8)
Wy_visual = ( ( (Wy - wc_min) / (wc_max - wc_min) ) * M * 255 ).astype(np.uint8)
Wx_visual = ( ( (Wx - wc_min) / (wc_max - wc_min) ) * M * 255 ).astype(np.uint8)
for go_name, _ in enumerate(uv_npy_file_names):
    name = uv_npy_file_names[go_name].split(".")[0]
    cx_name = uv_ch_visual_dst_dir + f"/{name}_Cx.jpg"
    cy_name = uv_ch_visual_dst_dir + f"/{name}_Cy.jpg"
    wx_name = wc_ch_visual_dst_dir + f"/{name}_Wx.jpg"
    wy_name = wc_ch_visual_dst_dir + f"/{name}_Wy.jpg"
    wz_name = wc_ch_visual_dst_dir + f"/{name}_Wz.jpg"
    wc_name = wc_ch_visual_dst_dir + f"/{name}_Wc.jpg"
    cv2.imwrite(cx_name, Cx_visual[go_name])
    cv2.imwrite(cy_name, Cy_visual[go_name])
    cv2.imwrite(wx_name, Wx_visual[go_name])
    cv2.imwrite(wy_name, Wy_visual[go_name])
    cv2.imwrite(wz_name, Wz_visual[go_name])
    cv2.imwrite(wc_name, W_visual[go_name])

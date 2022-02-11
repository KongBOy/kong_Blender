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
# print(__file__.split("\\")[-1])
# print("    code_exe_path:", code_exe_path)
# print("    code_exe_path_element:", code_exe_path_element)
# print("    kong_layer:", kong_layer)
# print("    kong_model2_dir:", kong_model2_dir)
#############################################################################################################################################################################################################
from kong_util.util import get_dir_npys

from step0_disk_index import render_out_dir

render_out_uv_npy_dir = f"{render_out_dir}/1_uv_npy"
render_out_wc_npy_dir = f"{render_out_dir}/2_wc_w_M_npy"
''' 注意！ 要把Mask 排除在外 來看 max 才是準的， 因為 Mask 的 max 一定是一， 這樣就看不到 data 的 max 了！'''
uvs = get_dir_npys(render_out_uv_npy_dir)
C = uvs[:, :, :, 1:3]
M  = uvs[:, :, :, 0:1]
Cy = uvs[:, :, :, 1:2]  ### 0.0 ~ 0.9980217
Cx = uvs[:, :, :, 2:3]  ### 0.0 ~ 0.9757899

#############################################################
WM = get_dir_npys(render_out_wc_npy_dir)
W  = WM[:, :, :, :3]   ### -0.13539262 ~ 0.1357405
Wz = WM[:, :, :, 0:1]  ###  0.0        ~ 0.039187048
Wy = WM[:, :, :, 1:2]  ### -0.13532962 ~ 0.1357405
Wx = WM[:, :, :, 2:3]  ### -0.08075158 ~ 0.07755918
M  = WM[:, :, :, 3:4]

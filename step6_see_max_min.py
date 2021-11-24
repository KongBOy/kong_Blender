import sys
sys.path.append(r"C:\Users\CVML\Desktop\kong_model2\kong_util")

from util import get_dir_npys

from step0_disk_index import render_out_dir

render_out_uv_npy_dir = f"{render_out_dir}/1_uv_npy"
render_out_wc_npy_dir = f"{render_out_dir}/2_wc_npy"

uvs = get_dir_npys(render_out_uv_npy_dir)
print(uvs[:900].max())
print(uvs[:900].min())
wcs = get_dir_npys(render_out_wc_npy_dir)
print(wcs[:900].max())
print(wcs[:900].min())

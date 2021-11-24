#############################################################################################################################################################################################################
### 把 current_dir 轉回到 kong_model 裡面
import os
import sys
curr_path = os.getcwd()
curr_layer = len(curr_path.split("\\")) - 1                ### 看 目前執行python的位置在哪一層， -1 是 因為 為了配合下面.index() 從0開始算
kong_layer = curr_path.split("\\").index("kong_model2")    ### 看kong_model2 在哪一層
back_to_kong_layer_amount = curr_layer - kong_layer        ### 看 目前執行python的位置在哪一層 到 kong_model2 差幾層
for _ in range(back_to_kong_layer_amount): os.chdir("..")  ### 看差幾層 往前跳 幾次dir
sys.path.append("./kong_util")                                       ### 把 kong_model2/kong_util 加進 sys.path

from build_dataset_combine import build_datasets

#####################################################################################################################################################
### blender_os_hw512
# db_name = "blender_os_hw512_have_bg"
# build_datasets(src_in_dir   = "J:/kong_render_os_book_all_have_bg_512/0_image",
#                src_gt_dir   = "J:/kong_render_os_book_all_have_bg_512/1_uv_knpy",
#                src_in_word  = ".png",
#                src_gt_word  = ".knpy",
#                dst_db_dir   = "J:/kong_render_os_book_all_have_bg_512",
#                db_name      = db_name,
#                db_in_name   = "dis_imgs",
#                db_gt_name   = "flows",
#                train_amount = 900,
#                src_rec_hope_dir="J:/kong_render_os_book_all_have_bg_512/0_image_ord",
#                src_rec_hope_word=".jpg")
#########################################################################################
# ### blender_os_hw512
# db_name = "blender_os_and_paper_hw512_have_bg"
# build_datasets(src_in_dir   = "J:/kong_render_os_book_and_paper_all_have_bg_512/0_image",
#                src_gt_dir   = "J:/kong_render_os_book_and_paper_all_have_bg_512/1_uv_knpy",
#                src_in_word  = ".png",
#                src_gt_word  = ".knpy",
#                dst_db_dir   = "J:/kong_render_os_book_and_paper_all_have_bg_512",
#                db_name      = db_name,
#                db_in_name   = "dis_imgs",
#                db_gt_name   = "flows",
#                train_amount = 900,
#                src_rec_hope_dir="J:/kong_render_os_book_and_paper_all_have_bg_512/0_image_ord",
#                src_rec_hope_word=".jpg")
#########################################################################################
### blender_os_hw512
# db_name = "blender_os_and_paper_hw512_have_dtd_bg"
# build_datasets(src_in_dir   = "J:/kong_render_os_book_and_paper_all_have_dtd_bg_512/0_image",
#                src_gt_dir   = "J:/kong_render_os_book_and_paper_all_have_dtd_bg_512/1_uv_knpy",
#                src_in_word  = ".png",
#                src_gt_word  = ".knpy",
#                dst_db_dir   = "J:/kong_render_os_book_and_paper_all_have_dtd_bg_512",
#                db_name      = db_name,
#                db_in_name   = "dis_imgs",
#                db_gt_name   = "flows",
#                train_amount = 900,
#                src_rec_hope_dir="J:/kong_render_os_book_and_paper_all_have_dtd_bg_512/0_image_ord",
#                src_rec_hope_word=".jpg")
#########################################################################################
### blender_os_hw512
from step0_disk_index import render_out_dir, render_name

db_out_disk = "J"
db_name = "blender_os_and_paper_hw512_have_dtd_hdr_mix_bg"
db_out_dir =  f"{db_out_disk}:/{render_name}/{db_name}"
build_datasets(src_in_dir   = f"{render_out_dir}/0_image",
               src_gt_dir   = f"{render_out_dir}/1_uv_knpy",
               src_in_word  = ".png",
               src_gt_word  = ".knpy",
               dst_db_dir   = db_out_dir,
               db_name      = db_name,
               db_in_name   = "dis_imgs",
               db_gt_name   = "flows",
               train_amount = 900,
               src_rec_hope_dir=f"{render_out_dir}/0_image_ord",
               src_rec_hope_word=".jpg")

'''
設定 128G隨身碟 磁碟代號 ， 因為我Working放隨身碟裡
'''
# Working_disk_index = "L"  ### 127.35
# Working_disk_index = "H"  ### HP820G1
# Working_disk_index = "D"  ### 127.35 2021/09/15
# Working_disk_index = "H"  ### 127.23 2021/11/17
# Working_disk_index = "K"  ### 127.23 2021/11/26
# Working_disk_index = "J"  ### 127.23 2022/01/28
Working_disk_index = "C"  ### 127.23 2022/02/25

'''
設定 Render 到 2T Doc3D 硬碟 內 哪個資料夾
'''

# render_name = "kong_render_os_book_no_bg"                                  ### 最一開始 try 的吧，嘗試 render 出來的 uv 是否真能 recover image，結論是沒問題可recover！ 沒有拿來train
# render_name = "kong_render_os_book_no_bg_768"                              ### 純 os_book， 全部黑背景， 有拿來train
# render_name = "kong_render_os_book_have_bg_512"                            ###  純 os_book， 一半有背景 一半黑背景， 沒有拿來train， 只是 try的概念
# render_name = "kong_render_os_book_all_have_bg_512"                        ### 純 os_book， 全部都有背景， 有拿來train
# render_name = "kong_render_os_book_and_paper_all_have_bg_512"              ### os_book + paper 頁面， 全部都有背景， 有拿來train
# render_name = "kong_render_os_book_and_paper_all_have_dtd_bg_512"          ### os_book + paper 頁面， 全部都有背景， 有拿來train
# render_name = "kong_render_try_image_ord_dir"                              ### os_book + paper 頁面， 全部都有背景， 有拿來train
# render_name = "kong_render_os_book_and_paper_all_have_dtd_hdr_mix_bg_512"  ### os_book + paper 頁面， 全部都有背景， 有拿來train
render_name = "Users/CVML/Desktop/see001_manually/kong_render_os_book_and_paper_all_have_dtd_hdr_mix_bg_512"  ### os_book + paper 頁面， 全部都有背景， 有拿來train

render_out_dir = f"{Working_disk_index}:/{render_name}"

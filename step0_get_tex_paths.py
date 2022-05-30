'''
設定 各個 tex 的來源
'''
from step0_disk_index import Working_disk_index
import sys
sys.path.append("../kong_util")
import os
from kong_util.util import get_dir_img_paths

class OS_book:
    def __init__(self):
        self.root = r"J:\0 data_dir\datasets\type7_cut_os_book\produce_straight\01_page_num_ok"
        self.img_paths = []

    def get_img_paths(self):
        for img_name in os.listdir(self.root):
            self.img_paths.append(self.root + "/" + img_name)
        return self.img_paths

os_img_paths = OS_book().get_img_paths()
dewarpnet_tex_paths = get_dir_img_paths(f"{Working_disk_index}:/Working/2 Blender/data_dir/0_ord/tex")
paper_img_paths     = get_dir_img_paths(f"C:/Users/TKU/Desktop/collect_pdf/result")




if __name__ == '__main__':
    import cv2
    print(os_img_paths)
    img = cv2.imread(os_img_paths[1])
    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    print("tex_paths", tex_paths)

'''
設定 各個 env 的來源
'''
from step0_disk_index import Working_disk_index
import sys
sys.path.append("../kong_util")
import os

from util import get_dir_certain_file_paths

class DTD:
    def __init__(self):
        self.dtd_root = r"J:\dtd"
        self.img_root = self.dtd_root + "/" + "images"
        self.img_paths = []

    def get_img_paths(self):
        categories = os.listdir(self.img_root)
        img_dirs = []
        for category in categories:
            img_dirs.append(self.img_root + "/" + category)

        for img_dir in img_dirs:
            for img_name in os.listdir(img_dir):
                self.img_paths.append(img_dir + "/" + img_name)
        return self.img_paths


dtd_img_paths       = DTD().get_img_paths()
dewarpnet_env_paths = get_dir_certain_file_paths(f"{Working_disk_index}:/Working/2 Blender/data_dir/0_ord/env", certain_word=".hdr")


if __name__ == '__main__':
    import cv2
    print("len(dtd_img_paths)", len(dtd_img_paths))
    print("len(dewarpnet_env_paths)", len(dewarpnet_env_paths))
    img = cv2.imread(dtd_img_paths[-15])
    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    print("dewarpnet_env_paths", dewarpnet_env_paths)
    print("env_paths", env_paths)

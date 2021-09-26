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

def Get_env_weights(*envs):
    # env1 = dtd_img_paths
    # env2 = dewarpnet_env_paths
    # env_db_amount = 2
    # env1_weight = 1 / (len(env1) * env_db_amount)
    # env2_weight = 1 / (len(env2) *env_db_amount )
    # env_weights = [env1_weight] * len(env1) + [env2_weight] * len(env2)
    # print(env_weights)
    # print("env1_weight", env1_weight)
    # print("env2_weight", env2_weight)

    env_db_amount = len(envs)
    # print(f"env_db_amount={env_db_amount}")

    env_path_amounts = [len(env) for env in envs]
    # print(f"env_path_amounts={env_path_amounts}")

    env_weights_values = [1 / (env_db_amount * env_path_amount) for env_path_amount in env_path_amounts]
    # print(f"env_weights_values={env_weights_values}")

    env_weights = []
    for go_env, env_path_amount in enumerate(env_path_amounts):
        env_weights += [env_weights_values[go_env]] * env_path_amount
    # print("len(env_weights)=", len(env_weights))
    return env_weights


dtd_img_paths       = DTD().get_img_paths()
dewarpnet_env_paths = get_dir_certain_file_paths(f"{Working_disk_index}:/Working/2 Blender/data_dir/0_ord/env", certain_word=".hdr")


if __name__ == '__main__':
    # import cv2
    # print("len(dtd_img_paths)", len(dtd_img_paths))
    # print("len(dewarpnet_env_paths)", len(dewarpnet_env_paths))
    # img = cv2.imread(dtd_img_paths[-15])
    # cv2.imshow("img", img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    # print("dewarpnet_env_paths", dewarpnet_env_paths)
    env_paths = []
    env_paths += dtd_img_paths
    env_paths += dewarpnet_env_paths
    env_log = []
    for _ in range(1000):
        env_weights = Get_env_weights(dtd_img_paths, dewarpnet_env_paths)
        import random
        env_path = random.choices(env_paths, weights=env_weights, k=1)[0]
        env_log.append(env_path)
        print(env_path)
    
    hdr_amount = 0
    dtd_amount = 0
    for env_path in env_log:
        if(".hdr" in env_path): hdr_amount += 1
        else: dtd_amount += 1
    print(f"hdr_amount={hdr_amount}, dtd_amount={dtd_amount}")

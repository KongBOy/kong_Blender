import os

class DTD:
    def __init__(self):
        self.dtd_root = r"G:\dtd"
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


dtd_img_paths = DTD().get_img_paths()
if __name__ == '__main__':
    import cv2
    print(dtd_img_paths)
    img = cv2.imread(dtd_img_paths[-15])
    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

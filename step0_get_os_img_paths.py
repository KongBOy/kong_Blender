import os

class OS_book:
    def __init__(self):
        self.root = r"J:\0 data_dir\datasets\type7_cut_os_book\produce_straight\01_page_num_ok"
        self.img_paths = []

    def get_img_paths(self):
        for img_name in os.listdir(self.root):
            self.img_paths.append(self.root + "/" + img_name)
        return self.img_paths


os_img_paths = OS_book().get_img_paths()
if __name__ == '__main__':
    import cv2
    print(os_img_paths)
    img = cv2.imread(os_img_paths[1])
    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

import cv2
import numpy as np
from skimage import morphology
from skimage import img_as_ubyte
import copy
from IPython import embed

np.set_printoptions(threshold=np.nan)

class Skeletonizer(object):
    def __init__(self, pic=None):
        self._img = pic or None
        self._skel_img = None

        #self.cut_x_offset =

        self.offset_x = 0
        self.offset_y = 0

        self.fish_offset_x = 100
        self.fish_offset_y = 100

        self.spine = []

    def skeletonize(self, input_img, ellipse):
        if ellipse is None:
            return

        self.img = input_img

        self.cut_img(ellipse)

        self.skel_img = copy.copy(self.img)
        # self.skel_img = cv2.cvtColor(self.skel_img, cv2.COLOR_BGR2GRAY)
        # self.skel_img = cv2.threshold(self.skel_img, 0, 255, cv2.THRESH_OTSU)[1]

        # skeletonize
        self.skel_img = morphology.skeletonize(self.skel_img > 1)

        # medial axis (may be better due to possibility to set mask!
        # self.skel_img = morphology.medial_axis(self.skel_img > 1)

        # change back to cv2 image
        self.skel_img = img_as_ubyte(self.skel_img)

        self.get_spine()

        self.show_skeleton()

    def show_skeleton(self):
        # cv2.imwrite("/home/madai/Pictures/test_skel.png", self.skel_img)
        if self.skel_img is None:
            return
        cv2.imshow("skeleton", self.skel_img)
        return

    def cut_img(self, ellipse):
        center_x = ellipse[0][0]
        center_y = ellipse[0][1]

        cut_x_1 = center_x - self.fish_offset_x
        cut_x_2 = center_x + self.fish_offset_x
        cut_y_1 = center_y - self.fish_offset_y
        cut_y_2 = center_y + self.fish_offset_y

        cuts = [cut_x_1, cut_x_2, cut_y_1, cut_y_2]
        for i in range(0, len(cuts), 1):
            if cuts[i] < 0:
                cuts[i] = 0

        self.offset_x = int(cuts[0])
        self.offset_y = int(cuts[2])

        self.img = copy.copy(self.img[cuts[2]:cuts[3], cuts[0]:cuts[1]])

    def get_spine(self):
        # x, y = np.nonzero(self.skel_img)
        #
        # self.spine = zip(y + self.offset_x, x + self.fish_offset_y)
        self.spine = []
        for row in range(0, len(self.skel_img), 1):
            for column in range(0, len(self.skel_img[row]), 1):
                if self.skel_img[row][column] != 0:
                    self.spine.append((column + self.offset_x, row + self.offset_y))

    def draw_spine(self, img):
        for point in self.spine:
            cv2.circle(img, point, 1, (0, 255, 0), 1)


    @property
    def img(self):
        return self._img
    @img.setter
    def img(self, pic):
        self._img = pic

    @property
    def skel_img(self):
        return self._skel_img
    @skel_img.setter
    def skel_img(self, pic):
        self._skel_img = pic

#if __name__ == '__main__':
#    skltnzr = Skeletonizer()
#    skltnzr.img = cv2.imread("test.png")
#    print (skltnzr.img.shape)
#    #skltnzr.skeletonize()
#    #skltnzr.show_skeleton()

import cv2
import numpy as np
from skimage import morphology
from skimage import img_as_ubyte
import copy

np.set_printoptions(threshold=np.nan)

class Skeletonizer(object):
    def __init__(self, pic=None):
        self._img = pic or None
        self._skel_img = None

    def skeletonize(self):
        if self.img is None:
            print "image is None"
            return
        self.skel_img = copy.copy(self.img)
        # self.skel_img = cv2.cvtColor(self.skel_img, cv2.COLOR_BGR2GRAY)
        # self.skel_img = cv2.threshold(self.skel_img, 0, 255, cv2.THRESH_OTSU)[1]

        # skeletonize
        # self.skel_img = morphology.skeletonize(self.skel_img > 1)

        # medial axis (may be better due to possibility to set mask!
        self.skel_img = morphology.medial_axis(self.skel_img > 1)

        # change back to cv2 image
        self.skel_img = img_as_ubyte(self.skel_img)

    def show_skeleton(self):
        # cv2.imwrite("/home/madai/Pictures/test_skel.png", self.skel_img)
        cv2.imshow("skeleton", self.skel_img)
        return

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

# if __name__ == '__main__':
#     skltnzr = Skeletonizer()
#     skltnzr.img = cv2.imread("/home/madai/Pictures/test.png")
#     skltnzr.skeletonize()
#     skltnzr.show_skeleton()
import cv2
import numpy as np
from skimage import morphology
from skimage import img_as_ubyte
import copy

np.set_printoptions(threshold=np.nan)

class Sceletonizer(object):
    def __init__(self, pic=None):
        self._img = pic or None
        self._scel_img = None

    def sceletonize(self):
        if self.img is None:
            print "image is None"
            return
        self.scel_img = copy.copy(self.img)
        # self.scel_img = cv2.cvtColor(self.scel_img, cv2.COLOR_BGR2GRAY)
        # self.scel_img = cv2.threshold(self.scel_img, 0, 255, cv2.THRESH_OTSU)[1]
        self.scel_img = morphology.skeletonize(self.scel_img > 1)
        self.scel_img = img_as_ubyte(self.scel_img)

    def show_sceleton(self):
        # cv2.imwrite("/home/madai/Pictures/test_scel.png", self.scel_img)
        cv2.imshow("sceleton", self.scel_img)
        return

    @property
    def img(self):
        return self._img
    @img.setter
    def img(self, pic):
        self._img = pic

    @property
    def scel_img(self):
        return self._scel_img
    @scel_img.setter
    def scel_img(self, pic):
        self._scel_img = pic

# if __name__ == '__main__':
#     scltnzr = Sceletonizer()
#     scltnzr.img = cv2.imread("/home/madai/Pictures/test.png")
#     scltnzr.sceletonize()
#     scltnzr.show_sceleton()
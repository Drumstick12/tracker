import cv2
from skimage import morphology
import copy

class Sceletonizer(object):
    def __init__(self, pic=None):
        self._img = pic or None
        self._scel_img = None

    def sceletonize(self):
        self.scel_img = copy.copy(self.img)
        self.scel_img = cv2.cvtColor(self.scel_img, cv2.COLOR_BGR2GRAY)
        self.scel_img = cv2.threshold(self.scel_img, 0, 255, cv2.THRESH_OTSU)[1]
        self.scel_img = morphology.skeletonize(self.scel_img > 0)

    def show_sceleton(self):
        cv2.imshow("sceleton", self.scel_img)

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
__author__ = 'Lorand Madai-Tahy'

import numpy as np
# np.set_printoptions(threshold=np.nan)


class ROI(object):
    number_of_roi = 0

    def __init__(self, x_1, y_1, x_2, y_2, name):
        self._name = name

        self.__x_1 = x_1
        self.__y_1 = y_1
        self.__x_2 = x_2
        self.__y_2 = y_2

        type(self).number_of_roi += 1

    def __del__(self):
        type(self).number_of_roi -= 1

    def import_cfg_values(self, cfg):
        self.x1 = cfg.getint('roi', 'x1')
        self.x2 = cfg.getint('roi', 'x2')
        self.y1 = cfg.getint('roi', 'y1')
        self.y2 = cfg.getint('roi', 'y2')

    @property
    def name(self):
        return self._name

    @property
    def x1(self):
        return self.__x_1

    @x1.setter
    def x1(self, value):
        self.__x_1 = value

    @property
    def y1(self):
        return self.__y_1

    @y1.setter
    def y1(self, value):
        self.__y_1 = value

    @property
    def x2(self):
        return self.__x_2

    @x2.setter
    def x2(self, value):
        self.__x_2 = value

    @property
    def y2(self):
        return self.__y_2

    @y2.setter
    def y2(self, value):
        self.__y_2 = value


class ROIColor(ROI):
    def __init__(self, x_1, y_1, x_2, y_2, name):
        super(ROIColor, self).__init__(x_1, y_1, x_2, y_2, name)

        self.mean_color = None

    def get_mean_color(self, img):
        new_img = img[self.y1:self.y2, self.x1:self.x2]
        self.mean_color = tuple(np.mean(np.mean(new_img, 0), 0))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tracker_ui.ui'
#
# Created: Mon Dec  1 12:45:22 2014
#      by: PyQt4 UI code generator 4.10.4

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_tracker_main_widget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, tracker_main_widget):
        #main widget
        tracker_main_widget.setObjectName(_fromUtf8("tracker_main_widget"))
        tracker_main_widget.resize(1059, 835)
        tracker_main_widget.setMinimumSize(QtCore.QSize(900, 770))

        # main vertical layout
        self.vertLO_main = QtGui.QVBoxLayout(tracker_main_widget)
        self.vertLO_main.setObjectName(_fromUtf8("vertLO_main"))
        # horizontal layout video + options
        self.hoLO_video_plus_options = QtGui.QHBoxLayout()
        self.hoLO_video_plus_options.setObjectName(_fromUtf8("hoLO_video_plus_options"))
        # graphical output viewer
        self.graphic_output_viewer = QtGui.QGraphicsView(tracker_main_widget)
        self.graphic_output_viewer.setObjectName(_fromUtf8("graphic_output_viewer"))
        self.hoLO_video_plus_options.addWidget(self.graphic_output_viewer)

        # options tab widget
        self.tab_widget_options = QtGui.QTabWidget(tracker_main_widget)
        self.tab_widget_options.setObjectName(_fromUtf8("tab_widget_options"))

        # file tab
        self.tab_file = QtGui.QWidget()
        self.tab_file.setWhatsThis(_fromUtf8(""))
        self.tab_file.setObjectName(_fromUtf8("tab_file"))
        # vertLO file tab
        self.vertLO_tab_file = QtGui.QVBoxLayout(self.tab_file)
        self.vertLO_tab_file.setObjectName(_fromUtf8("vertLO_tab_file"))
        # spacer
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vertLO_tab_file.addItem(spacerItem)
        # line
        self.line = QtGui.QFrame(self.tab_file)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.vertLO_tab_file.addWidget(self.line)
        # label file path
        self.lbl_file_path = QtGui.QLabel(self.tab_file)
        self.lbl_file_path.setObjectName(_fromUtf8("lbl_file_path"))
        self.vertLO_tab_file.addWidget(self.lbl_file_path)
        # line edit file path
        self.lnEdit_file_path = QtGui.QLineEdit(self.tab_file)
        self.lnEdit_file_path.setObjectName(_fromUtf8("lnEdit_file_path"))
        self.vertLO_tab_file.addWidget(self.lnEdit_file_path)
        # button browse file
        self.btn_browse_file = QtGui.QPushButton(self.tab_file)
        self.btn_browse_file.setObjectName(_fromUtf8("btn_browse_file"))
        self.vertLO_tab_file.addWidget(self.btn_browse_file)
        # line
        self.line_2 = QtGui.QFrame(self.tab_file)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.vertLO_tab_file.addWidget(self.line_2)
        # spacer
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vertLO_tab_file.addItem(spacerItem1)
        # complete file tab
        self.tab_widget_options.addTab(self.tab_file, _fromUtf8(""))

        # roi tab
        self.tab_roi = QtGui.QWidget()
        self.tab_roi.setObjectName(_fromUtf8("tab_roi"))
        # vertical layout roi tab
        self.vertLO_tab_roi = QtGui.QVBoxLayout(self.tab_roi)
        self.vertLO_tab_roi.setObjectName(_fromUtf8("vertLO_tab_roi"))
        # spaccer
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vertLO_tab_roi.addItem(spacerItem2)
        # line
        self.line_3 = QtGui.QFrame(self.tab_roi)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.vertLO_tab_roi.addWidget(self.line_3)
        # label region of interest
        self.lbl_roi = QtGui.QLabel(self.tab_roi)
        self.lbl_roi.setObjectName(_fromUtf8("lbl_roi"))
        self.vertLO_tab_roi.addWidget(self.lbl_roi)
        # graphics viewer roi
        self.grView_roi = QtGui.QGraphicsView(self.tab_roi)
        self.grView_roi.setMinimumSize(QtCore.QSize(0, 350))
        self.grView_roi.setObjectName(_fromUtf8("grView_roi"))
        self.vertLO_tab_roi.addWidget(self.grView_roi)
        # grid layout set roi
        self.gridLO_set_roi = QtGui.QGridLayout()
        self.gridLO_set_roi.setObjectName(_fromUtf8("gridLO_set_roi"))
        # spin box x start
        self.spinBox_x_start = QtGui.QSpinBox(self.tab_roi)
        self.spinBox_x_start.setMaximum(9999)
        self.spinBox_x_start.setObjectName(_fromUtf8("spinBox_x_start"))
        self.gridLO_set_roi.addWidget(self.spinBox_x_start, 0, 1, 1, 1)
        # label y end
        self.lbl_roi_y_end = QtGui.QLabel(self.tab_roi)
        self.lbl_roi_y_end.setObjectName(_fromUtf8("lbl_roi_y_end"))
        self.gridLO_set_roi.addWidget(self.lbl_roi_y_end, 1, 2, 1, 1)
        # spin box y end
        self.spinBox_y_end = QtGui.QSpinBox(self.tab_roi)
        self.spinBox_y_end.setMaximum(9999)
        self.spinBox_y_end.setObjectName(_fromUtf8("spinBox_y_end"))
        self.gridLO_set_roi.addWidget(self.spinBox_y_end, 1, 3, 1, 1)
        # spin box y start
        self.spinBox_y_start = QtGui.QSpinBox(self.tab_roi)
        self.spinBox_y_start.setMaximum(9999)
        self.spinBox_y_start.setObjectName(_fromUtf8("spinBox_y_start"))
        self.gridLO_set_roi.addWidget(self.spinBox_y_start, 1, 1, 1, 1)
        # label x end
        self.lbl_roi_x_end = QtGui.QLabel(self.tab_roi)
        self.lbl_roi_x_end.setObjectName(_fromUtf8("lbl_roi_x_end"))
        self.gridLO_set_roi.addWidget(self.lbl_roi_x_end, 0, 2, 1, 1)
        # label x start
        self.lbl_roi_x_start = QtGui.QLabel(self.tab_roi)
        self.lbl_roi_x_start.setObjectName(_fromUtf8("lbl_roi_x_start"))
        self.gridLO_set_roi.addWidget(self.lbl_roi_x_start, 0, 0, 1, 1)
        # label y start
        self.lbl_roi_y_start = QtGui.QLabel(self.tab_roi)
        self.lbl_roi_y_start.setObjectName(_fromUtf8("lbl_roi_y_start"))
        self.gridLO_set_roi.addWidget(self.lbl_roi_y_start, 1, 0, 1, 1)
        # spin box x end
        self.spinBox_x_end = QtGui.QSpinBox(self.tab_roi)
        self.spinBox_x_end.setMaximum(9999)
        self.spinBox_x_end.setObjectName(_fromUtf8("spinBox_x_end"))
        self.gridLO_set_roi.addWidget(self.spinBox_x_end, 0, 3, 1, 1)
        # add grid_layout_set_roi to vertical layout of tab
        self.vertLO_tab_roi.addLayout(self.gridLO_set_roi)
        # line
        self.line_4 = QtGui.QFrame(self.tab_roi)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.vertLO_tab_roi.addWidget(self.line_4)
        # spacer
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vertLO_tab_roi.addItem(spacerItem3)
        # complete roi tab
        self.tab_widget_options.addTab(self.tab_roi, _fromUtf8(""))

        # adv tab
        self.tab_adv = QtGui.QWidget()
        self.tab_adv.setObjectName(_fromUtf8("tab_adv"))
        # vertical layout adv tab
        self.vertLO_tab_adv = QtGui.QVBoxLayout(self.tab_adv)
        self.vertLO_tab_adv.setObjectName(_fromUtf8("vertLO_tab_adv"))
        # spacer
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vertLO_tab_adv.addItem(spacerItem4)
        # line
        self.line_10 = QtGui.QFrame(self.tab_adv)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.vertLO_tab_adv.addWidget(self.line_10)
        # spacer
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vertLO_tab_adv.addItem(spacerItem5)
        # horizontal layout frame waittime
        self.hoLO_frame_waittime = QtGui.QHBoxLayout()
        self.hoLO_frame_waittime.setObjectName(_fromUtf8("hoLO_frame_waittime"))
        # label frame waittime
        self.lbl_frame_waittime = QtGui.QLabel(self.tab_adv)
        self.lbl_frame_waittime.setObjectName(_fromUtf8("lbl_frame_waittime"))
        self.hoLO_frame_waittime.addWidget(self.lbl_frame_waittime)
        # spin box frame waittime
        self.spinBox_frame_waittime = QtGui.QSpinBox(self.tab_adv)
        self.spinBox_frame_waittime.setMinimum(1)
        self.spinBox_frame_waittime.setMaximum(1000)
        self.spinBox_frame_waittime.setObjectName(_fromUtf8("spinBox_frame_waittime"))
        self.hoLO_frame_waittime.addWidget(self.spinBox_frame_waittime)
        self.vertLO_tab_adv.addLayout(self.hoLO_frame_waittime)
        # spacer
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vertLO_tab_adv.addItem(spacerItem6)
        # line
        self.line_5 = QtGui.QFrame(self.tab_adv)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.vertLO_tab_adv.addWidget(self.line_5)
        # label start area
        self.lbl_start_area = QtGui.QLabel(self.tab_adv)
        self.lbl_start_area.setObjectName(_fromUtf8("lbl_start_area"))
        self.vertLO_tab_adv.addWidget(self.lbl_start_area)
        # graphics view starting area
        self.grView_starting_area = QtGui.QGraphicsView(self.tab_adv)
        self.grView_starting_area.setMinimumSize(QtCore.QSize(0, 350))
        self.grView_starting_area.setObjectName(_fromUtf8("grView_starting_area"))
        self.vertLO_tab_adv.addWidget(self.grView_starting_area)
        # grid layout set starting area
        self.gridLO_start_area = QtGui.QGridLayout()
        self.gridLO_start_area.setObjectName(_fromUtf8("gridLO_start_area"))
        # spinbox starting_x end
        self.spinBox_starting_x_end = QtGui.QSpinBox(self.tab_adv)
        self.spinBox_starting_x_end.setMaximum(9999)
        self.spinBox_starting_x_end.setObjectName(_fromUtf8("spinBox_starting_x_end"))
        self.gridLO_start_area.addWidget(self.spinBox_starting_x_end, 0, 3, 1, 1)
        # spinbox starting_x start
        self.spinBox_starting_x_start = QtGui.QSpinBox(self.tab_adv)
        self.spinBox_starting_x_start.setMaximum(9999)
        self.spinBox_starting_x_start.setObjectName(_fromUtf8("spinBox_starting_x_start"))
        self.gridLO_start_area.addWidget(self.spinBox_starting_x_start, 0, 1, 1, 1)
        # label starting_x end
        self.lbl_start_x_end = QtGui.QLabel(self.tab_adv)
        self.lbl_start_x_end.setObjectName(_fromUtf8("lbl_start_x_end"))
        self.gridLO_start_area.addWidget(self.lbl_start_x_end, 0, 2, 1, 1)
        # label starting_y start
        self.lbl_start_y_start = QtGui.QLabel(self.tab_adv)
        self.lbl_start_y_start.setObjectName(_fromUtf8("lbl_start_y_start"))
        self.gridLO_start_area.addWidget(self.lbl_start_y_start, 1, 0, 1, 1)
        # label starting_y end
        self.lbl_start_y_end = QtGui.QLabel(self.tab_adv)
        self.lbl_start_y_end.setObjectName(_fromUtf8("lbl_start_y_end"))
        self.gridLO_start_area.addWidget(self.lbl_start_y_end, 1, 2, 1, 1)
        # spinbox starting_y end
        self.spinBox_starting_y_end = QtGui.QSpinBox(self.tab_adv)
        self.spinBox_starting_y_end.setMaximum(9999)
        self.spinBox_starting_y_end.setObjectName(_fromUtf8("spinBox_starting_y_end"))
        self.gridLO_start_area.addWidget(self.spinBox_starting_y_end, 1, 3, 1, 1)
        # spinbox starting_y start
        self.spinBox_starting_y_start = QtGui.QSpinBox(self.tab_adv)
        self.spinBox_starting_y_start.setMaximum(9999)
        self.spinBox_starting_y_start.setObjectName(_fromUtf8("spinBox_starting_y_start"))
        self.gridLO_start_area.addWidget(self.spinBox_starting_y_start, 1, 1, 1, 1)
        # label starting_x start
        self.lbl_start_x_start = QtGui.QLabel(self.tab_adv)
        self.lbl_start_x_start.setObjectName(_fromUtf8("lbl_start_x_start"))
        self.gridLO_start_area.addWidget(self.lbl_start_x_start, 0, 0, 1, 1)
        # add starting are selection grid layout to tab layout
        self.vertLO_tab_adv.addLayout(self.gridLO_start_area)
        # line
        self.line_6 = QtGui.QFrame(self.tab_adv)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.vertLO_tab_adv.addWidget(self.line_6)
        # spacer
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vertLO_tab_adv.addItem(spacerItem7)
        # horizontal layout set start orientation
        self.hoLO_start_ori = QtGui.QHBoxLayout()
        self.hoLO_start_ori.setObjectName(_fromUtf8("hoLO_start_ori"))
        # label start orientation
        self.lbl_start_orientation = QtGui.QLabel(self.tab_adv)
        self.lbl_start_orientation.setObjectName(_fromUtf8("lbl_start_orientation"))
        self.hoLO_start_ori.addWidget(self.lbl_start_orientation)
        # spinbox set start orientation
        self.spinBox_start_orientation = QtGui.QSpinBox(self.tab_adv)
        self.spinBox_start_orientation.setObjectName(_fromUtf8("spinBox_start_orientation"))
        self.hoLO_start_ori.addWidget(self.spinBox_start_orientation)
        # add start orientation layout to tab layout
        self.vertLO_tab_adv.addLayout(self.hoLO_start_ori)
        # spacer
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vertLO_tab_adv.addItem(spacerItem8)
        # line
        self.line_9 = QtGui.QFrame(self.tab_adv)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.vertLO_tab_adv.addWidget(self.line_9)
        # spacer
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vertLO_tab_adv.addItem(spacerItem9)
        # grid layout fishsize threshold
        self.gridLO_fishsize_th = QtGui.QGridLayout()
        self.gridLO_fishsize_th.setObjectName(_fromUtf8("gridLO_fishsize_th"))
        # label fishsize threshold
        self.lbl_fishsize_threshold = QtGui.QLabel(self.tab_adv)
        self.lbl_fishsize_threshold.setObjectName(_fromUtf8("lbl_fishsize_threshold"))
        self.gridLO_fishsize_th.addWidget(self.lbl_fishsize_threshold, 0, 0, 1, 1)
        # spinbox fishsize threshold
        self.spinBox_fish_threshold = QtGui.QSpinBox(self.tab_adv)
        self.spinBox_fish_threshold.setObjectName(_fromUtf8("spinBox_fish_threshold"))
        self.gridLO_fishsize_th.addWidget(self.spinBox_fish_threshold, 0, 1, 1, 1)
        # label maximum fishsize threshold
        self.lbl_max_fishsize_threshold = QtGui.QLabel(self.tab_adv)
        self.lbl_max_fishsize_threshold.setObjectName(_fromUtf8("lbl_max_fishsize_threshold"))
        self.gridLO_fishsize_th.addWidget(self.lbl_max_fishsize_threshold, 1, 0, 1, 1)
        # spinbox maximum fishsize threshold
        self.spinBox_fish_max_threshold = QtGui.QSpinBox(self.tab_adv)
        self.spinBox_fish_max_threshold.setObjectName(_fromUtf8("spinBox_fish_max_threshold"))
        self.gridLO_fishsize_th.addWidget(self.spinBox_fish_max_threshold, 1, 1, 1, 1)
        # add fishsize layout to tab layout
        self.vertLO_tab_adv.addLayout(self.gridLO_fishsize_th)
        # checkbox enable maximum size threshold
        self.cbx_enable_max_size_thresh = QtGui.QCheckBox(self.tab_adv)
        self.cbx_enable_max_size_thresh.setObjectName(_fromUtf8("cbx_enable_max_size_thresh"))
        self.vertLO_tab_adv.addWidget(self.cbx_enable_max_size_thresh)
        # spacer
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vertLO_tab_adv.addItem(spacerItem10)
        # complete advanced tab
        self.tab_widget_options.addTab(self.tab_adv, _fromUtf8(""))

        # visuals tab
        self.tab_visual = QtGui.QWidget()
        self.tab_visual.setObjectName(_fromUtf8("tab_visual"))
        # vertical layout visuals tab
        self.vertLO_tab_visual = QtGui.QVBoxLayout(self.tab_visual)
        self.vertLO_tab_visual.setObjectName(_fromUtf8("vertLO_tab_visual"))
        # spacer
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vertLO_tab_visual.addItem(spacerItem11)
        # line
        self.line_7 = QtGui.QFrame(self.tab_visual)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.vertLO_tab_visual.addWidget(self.line_7)
        # label image morphing
        self.lbl_img_morphing = QtGui.QLabel(self.tab_visual)
        self.lbl_img_morphing.setObjectName(_fromUtf8("lbl_img_morphing"))
        self.vertLO_tab_visual.addWidget(self.lbl_img_morphing)
        # grid layout image morphing
        self.gridLO_img_morphing = QtGui.QGridLayout()
        self.gridLO_img_morphing.setObjectName(_fromUtf8("gridLO_img_morphing"))
        # label erosion factor
        self.lbl_erosion = QtGui.QLabel(self.tab_visual)
        self.lbl_erosion.setObjectName(_fromUtf8("lbl_erosion"))
        self.gridLO_img_morphing.addWidget(self.lbl_erosion, 1, 1, 1, 1)
        # label dilation factor
        self.lbl_dilation = QtGui.QLabel(self.tab_visual)
        self.lbl_dilation.setObjectName(_fromUtf8("lbl_dilation"))
        self.gridLO_img_morphing.addWidget(self.lbl_dilation, 4, 1, 1, 1)
        # spinbox set dilation factor
        self.spinBox_dilation = QtGui.QSpinBox(self.tab_visual)
        self.spinBox_dilation.setMinimum(1)
        self.spinBox_dilation.setObjectName(_fromUtf8("spinBox_dilation"))
        self.gridLO_img_morphing.addWidget(self.spinBox_dilation, 4, 2, 1, 1)
        # spinbox set erosion factor
        self.spinBox_erosion = QtGui.QSpinBox(self.tab_visual)
        self.spinBox_erosion.setMinimum(1)
        self.spinBox_erosion.setObjectName(_fromUtf8("spinBox_erosion"))
        self.gridLO_img_morphing.addWidget(self.spinBox_erosion, 1, 2, 1, 1)
        # add grid layout image morphing
        self.vertLO_tab_visual.addLayout(self.gridLO_img_morphing)
        # line
        self.line_8 = QtGui.QFrame(self.tab_visual)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.vertLO_tab_visual.addWidget(self.line_8)
        # spacer
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vertLO_tab_visual.addItem(spacerItem12)
        # line
        self.line_13 = QtGui.QFrame(self.tab_visual)
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.vertLO_tab_visual.addWidget(self.line_13)
        # label image processing steps
        self.lbl_img_proc_steps = QtGui.QLabel(self.tab_visual)
        self.lbl_img_proc_steps.setObjectName(_fromUtf8("lbl_img_proc_steps"))
        # vertical layout show processing steps enable
        self.vertLO_tab_visual.addWidget(self.lbl_img_proc_steps)
        # checkbox show background subtracted image
        self.cbx_show_bgsub_img = QtGui.QCheckBox(self.tab_visual)
        self.cbx_show_bgsub_img.setObjectName(_fromUtf8("cbx_show_bgsub_img"))
        self.vertLO_tab_visual.addWidget(self.cbx_show_bgsub_img)
        # checkbox show morphed image
        self.cbx_show_morph_img = QtGui.QCheckBox(self.tab_visual)
        self.cbx_show_morph_img.setObjectName(_fromUtf8("cbx_show_morph_img"))
        self.vertLO_tab_visual.addWidget(self.cbx_show_morph_img)
        # checkbox show contour image
        self.cbx_show_contour = QtGui.QCheckBox(self.tab_visual)
        self.cbx_show_contour.setObjectName(_fromUtf8("cbx_show_contour"))
        self.vertLO_tab_visual.addWidget(self.cbx_show_contour)
        # checkbox show ellipse
        self.cbx_show_ellipse = QtGui.QCheckBox(self.tab_visual)
        self.cbx_show_ellipse.setObjectName(_fromUtf8("cbx_show_ellipse"))
        self.vertLO_tab_visual.addWidget(self.cbx_show_ellipse)
        # line
        self.line_14 = QtGui.QFrame(self.tab_visual)
        self.line_14.setFrameShape(QtGui.QFrame.HLine)
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.vertLO_tab_visual.addWidget(self.line_14)
        # spacer
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vertLO_tab_visual.addItem(spacerItem13)
        # line
        self.line_11 = QtGui.QFrame(self.tab_visual)
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.vertLO_tab_visual.addWidget(self.line_11)
        # label data visualization
        self.gridLO_data_visual = QtGui.QGridLayout()
        self.gridLO_data_visual.setObjectName(_fromUtf8("gridLO_data_visual"))
        # button set circle color
        self.btn_set_circle_color = QtGui.QPushButton(self.tab_visual)
        self.btn_set_circle_color.setObjectName(_fromUtf8("btn_set_circle_color"))
        self.gridLO_data_visual.addWidget(self.btn_set_circle_color, 4, 1, 1, 1)
        # spinbox
        self.spinBox_circle_size = QtGui.QSpinBox(self.tab_visual)
        self.spinBox_circle_size.setMinimum(1)
        self.spinBox_circle_size.setMaximum(25)
        self.spinBox_circle_size.setObjectName(_fromUtf8("spinBox_circle_size"))
        self.gridLO_data_visual.addWidget(self.spinBox_circle_size, 2, 1, 1, 1)
        # label circle color
        self.lbl_circ_color = QtGui.QLabel(self.tab_visual)
        self.lbl_circ_color.setObjectName(_fromUtf8("lbl_circ_color"))
        self.gridLO_data_visual.addWidget(self.lbl_circ_color, 4, 0, 1, 1)
        # label circle size
        self.lbl_circle_size = QtGui.QLabel(self.tab_visual)
        self.lbl_circle_size.setObjectName(_fromUtf8("lbl_circle_size"))
        self.gridLO_data_visual.addWidget(self.lbl_circle_size, 2, 0, 1, 1)
        # label line offset
        self.lbl_line_offset = QtGui.QLabel(self.tab_visual)
        self.lbl_line_offset.setObjectName(_fromUtf8("lbl_line_offset"))
        self.gridLO_data_visual.addWidget(self.lbl_line_offset, 1, 0, 1, 1)
        # button set line color
        self.btn_set_line_color = QtGui.QPushButton(self.tab_visual)
        self.btn_set_line_color.setObjectName(_fromUtf8("btn_set_line_color"))
        self.gridLO_data_visual.addWidget(self.btn_set_line_color, 3, 1, 1, 1)
        # spinbox linend offset
        self.spinBox_lineend_offset = QtGui.QSpinBox(self.tab_visual)
        self.spinBox_lineend_offset.setMinimum(1)
        self.spinBox_lineend_offset.setMaximum(20)
        self.spinBox_lineend_offset.setObjectName(_fromUtf8("spinBox_lineend_offset"))
        self.gridLO_data_visual.addWidget(self.spinBox_lineend_offset, 1, 1, 1, 1)
        # label line color
        self.lbl_ln_color = QtGui.QLabel(self.tab_visual)
        self.lbl_ln_color.setObjectName(_fromUtf8("lbl_ln_color"))
        self.gridLO_data_visual.addWidget(self.lbl_ln_color, 3, 0, 1, 1)
        # label  data visualization
        self.lbl_data_visualization = QtGui.QLabel(self.tab_visual)
        self.lbl_data_visualization.setObjectName(_fromUtf8("lbl_data_visualization"))
        self.gridLO_data_visual.addWidget(self.lbl_data_visualization, 0, 0, 1, 1)
        # add data visualization layout
        self.vertLO_tab_visual.addLayout(self.gridLO_data_visual)
        # line
        self.line_12 = QtGui.QFrame(self.tab_visual)
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.vertLO_tab_visual.addWidget(self.line_12)
        # spacer
        spacerItem14 = QtGui.QSpacerItem(20, 119, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vertLO_tab_visual.addItem(spacerItem14)
        self.tab_widget_options.addTab(self.tab_visual, _fromUtf8(""))
        # add visuals tab to video_plus_options tab
        self.hoLO_video_plus_options.addWidget(self.tab_widget_options)
        # add video_plus_options tab to main widget
        self.vertLO_main.addLayout(self.hoLO_video_plus_options)

        # horizontal layout bot buttons
        self.hoLO_bot_buttons = QtGui.QHBoxLayout()
        self.hoLO_bot_buttons.setObjectName(_fromUtf8("hoLO_bot_buttons"))
        # button start tracking
        self.btn_start_tracking = QtGui.QPushButton(tracker_main_widget)
        self.btn_start_tracking.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_start_tracking.setObjectName(_fromUtf8("btn_start_tracking"))
        self.hoLO_bot_buttons.addWidget(self.btn_start_tracking)
        # button abort tracking
        self.btn_abort_tracking = QtGui.QPushButton(tracker_main_widget)
        self.btn_abort_tracking.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_abort_tracking.setObjectName(_fromUtf8("btn_abort_tracking"))
        self.hoLO_bot_buttons.addWidget(self.btn_abort_tracking)
        # add button layout to main widget layout
        self.vertLO_main.addLayout(self.hoLO_bot_buttons)

        self.retranslateUi(tracker_main_widget)
        self.tab_widget_options.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(tracker_main_widget)

    def retranslateUi(self, tracker_main_widget):
        tracker_main_widget.setWindowTitle(_translate("tracker_main_widget", "[TF]² 1.0", None))
        self.lbl_file_path.setText(_translate("tracker_main_widget", "File Path", None))
        self.btn_browse_file.setText(_translate("tracker_main_widget", "Browse File", None))
        self.tab_widget_options.setTabText(self.tab_widget_options.indexOf(self.tab_file), _translate("tracker_main_widget", "File", None))
        self.lbl_roi.setToolTip(_translate("tracker_main_widget", "<html><head/><body><p>Define the Area in which the Fish shall be detected. Point (0,0) is the upper left corner.</p></body></html>", None))
        self.lbl_roi.setText(_translate("tracker_main_widget", "Region of interest", None))
        self.lbl_roi_y_end.setText(_translate("tracker_main_widget", "Y End", None))
        self.lbl_roi_x_end.setText(_translate("tracker_main_widget", "X End", None))
        self.lbl_roi_x_start.setText(_translate("tracker_main_widget", "X Start", None))
        self.lbl_roi_y_start.setText(_translate("tracker_main_widget", "Y Start", None))
        self.tab_widget_options.setTabText(self.tab_widget_options.indexOf(self.tab_roi), _translate("tracker_main_widget", "ROI", None))
        self.lbl_frame_waittime.setText(_translate("tracker_main_widget", "Frame Waittime (ms)", None))
        self.lbl_start_area.setText(_translate("tracker_main_widget", "Starting Area", None))
        self.lbl_start_x_end.setText(_translate("tracker_main_widget", "X End", None))
        self.lbl_start_y_start.setText(_translate("tracker_main_widget", "Y Start", None))
        self.lbl_start_y_end.setText(_translate("tracker_main_widget", "Y End", None))
        self.lbl_start_x_start.setText(_translate("tracker_main_widget", "X Start", None))
        self.lbl_start_orientation.setText(_translate("tracker_main_widget", "Starting Orientation", None))
        self.lbl_fishsize_threshold.setText(_translate("tracker_main_widget", "Fish Detection min Size Threshold", None))
        self.lbl_max_fishsize_threshold.setText(_translate("tracker_main_widget", "Fish Detection max Size Threshold", None))
        self.cbx_enable_max_size_thresh.setText(_translate("tracker_main_widget", "Enable max Size Threshold", None))
        self.tab_widget_options.setTabText(self.tab_widget_options.indexOf(self.tab_adv), _translate("tracker_main_widget", "Advanced", None))
        self.lbl_img_morphing.setText(_translate("tracker_main_widget", "Image Morphing", None))
        self.lbl_erosion.setText(_translate("tracker_main_widget", "Erosion Faktor", None))
        self.lbl_dilation.setText(_translate("tracker_main_widget", "Dilation Faktor", None))
        self.lbl_img_proc_steps.setText(_translate("tracker_main_widget", "Image Processing Steps", None))
        self.cbx_show_bgsub_img.setText(_translate("tracker_main_widget", "Show Background-subtracted Image", None))
        self.cbx_show_morph_img.setText(_translate("tracker_main_widget", "Show Morphed Image", None))
        self.cbx_show_contour.setText(_translate("tracker_main_widget", "Show Contours", None))
        self.cbx_show_ellipse.setText(_translate("tracker_main_widget", "Show fitted Ellipse", None))
        self.btn_set_circle_color.setText(_translate("tracker_main_widget", "Set Color", None))
        self.lbl_circ_color.setText(_translate("tracker_main_widget", "Circle Color", None))
        self.lbl_circle_size.setText(_translate("tracker_main_widget", "Circle Size", None))
        self.lbl_line_offset.setText(_translate("tracker_main_widget", "Lineend Offset", None))
        self.btn_set_line_color.setText(_translate("tracker_main_widget", "Set Color", None))
        self.lbl_ln_color.setText(_translate("tracker_main_widget", "Line Color", None))
        self.lbl_data_visualization.setText(_translate("tracker_main_widget", "Data Visualization", None))
        self.tab_widget_options.setTabText(self.tab_widget_options.indexOf(self.tab_visual), _translate("tracker_main_widget", "Visualization", None))
        self.btn_start_tracking.setText(_translate("tracker_main_widget", "Start Tracking", None))
        self.btn_abort_tracking.setText(_translate("tracker_main_widget", "Abort Tracking", None))

if __name__ == "__main__":
    qApp = QtGui.QApplication(sys.argv)
    ui_tr = Ui_tracker_main_widget()
    ui_tr.show()
    sys.exit(qApp.exec_())
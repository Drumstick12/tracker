import numpy as np
import cv2
import math
import sys
import copy
import os
import argparse


# for debug
SAVE_FRAMES = True

# check out 2014-08-27_39.avi! put in estimated orientation algorithm!

FRAME_WAITTIME = 1

frame_counter = 0

DRAW_CONTOUR = False

DRAW_ELLIPSE = True
ellipse = None

DRAW_LINE = True
line_point_offset = 5
line = None
lx1 = 0
ly1 = 0
lx2 = 0
ly2 = 0

DRAW_TRAVEL_ORIENTATION = True
img_travel_orientation = []

DRAW_TRAVEL_ROUTE = True
img_travel_route = []
DRAW_ORIGINAL_OUTPUT = True

number_contours_per_frame = []
number_relevant_contours_per_frame = []

# set region of interest (ROI)
ROI_X1 = 15
ROI_X2 = 695
ROI_Y1 = 80
ROI_Y2 = 515


fish_size_threshold = 700

fish_started = False
starting_area_x_factor = 0.85
starting_area_y1_factor = 0.30
starting_area_y2_factor = 0.70

# init last position and lists for saving
last_pos = None
all_pos_roi = []
all_pos_original = []

# init last orientation and list for saving
last_ori = None
start_ori = 270
all_oris = []

last_frame = None
last_frame_OV_output = None

ESTIMATE_MISSING_DATA = True
estimated_pos_roi = []
estimated_pos_original = []
estimated_oris = []


output_directory = ""

# define testvideo
# path to directory
# standard:
# dir = "examples/"
# videofile_name = "2014-10-01_33"
# problem:
dir = "examples/"
videofile_name = "2014-08-27_33"

# dir = "/home/madai/Videos/"
# videofile_name = "2014-08-27_1"




video_file = dir + videofile_name + ".avi"

# sets video file to terminal-attribute path to video file
def set_video_file():
    if len(sys.argv) > 1:
        global video_file
        video_file = sys.argv[1]
    else:
        return

def extract_video_file_name_and_path():
    pointer_end = len(video_file)-1
    while video_file[pointer_end] != ".":
        pointer_end -= 1
        if pointer_end == 0:
            print "no valid file"
            return ""

    pointer_start = pointer_end
    while video_file[pointer_start-1] != "/":
        pointer_start -= 1

    return video_file[pointer_start:pointer_end], video_file[:pointer_start]




# init cap
cap = ""

# captures video defined by path stored in video file
def set_video_capture():
    global cap
    cap = cv2.VideoCapture(video_file)


# create and position windows
# cv2.namedWindow("file")
# cv2.moveWindow("file", 0, 0)
# cv2.namedWindow("ROI")
# cv2.moveWindow("ROI", 1300, 0)
# cv2.namedWindow("Background subtracted")
# cv2.moveWindow("Background subtracted", 0, 600)
#
# cv2.namedWindow("morphed")
# cv2.moveWindow("morphed", 1300, 600)
#
# cv2.namedWindow("canny")
# cv2.moveWindow("canny", 600, 70)

cv2.namedWindow("contours")
cv2.moveWindow("contours", 570, 570)


# temporary function
# show images
def show_imgs(img, roi, roi_bg_subtracted, roi_bg_subtracted_morphed, canny_edges):

    # # show original output
    # cv2.imshow('file', img)
    #
    # # show original ROI
    # cv2.imshow('ROI', roi)
    #
    # # show ROI with subtracted BG
    # cv2.imshow('Background subtracted', roi_bg_subtracted)
    #
    # # show morphed subtracted BG-img
    # cv2.imshow("morphed", roi_bg_subtracted_morphed)
    #
    # # show ROI img with canny edge detection
    # cv2.imshow("canny", canny_edges)

    # if SAVE_FRAMES and img is not None:
        # cv2.imwrite(dir + "frames/" + str(frame_counter) + "_roi_bg_sub_morph" + ".jpg", roi_bg_subtracted_morphed)
        # cv2.imwrite(dir + "frames/" + str(frame_counter) + "_roi_bg_sub" + ".jpg", roi_bg_subtracted)
        # cv2.imwrite(dir + "frames/" + str(frame_counter) + "_roi" + ".jpg", roi)
        # cv2.imwrite(dir + "frames/" + str(frame_counter) + "_img" + ".jpg", img)
        # cv2.imwrite(dir + "frames/" + str(frame_counter) + "_canny" + ".jpg", canny_edges)

    return


##########################################################################################
##########################################################################################
# serious stuff starts here

# morph given img by erosion/dilation
def morph_img(img):
    # erode img
    er_kernel = np.ones((4, 4), np.uint8)
    er_img = cv2.erode(img, er_kernel, iterations=1)
    # dilate img
    di_kernel = np.ones((4, 4), np.uint8)
    di_img = cv2.dilate(er_img, di_kernel, iterations=4)
    # thresholding to black-white
    ret, morphed_img = cv2.threshold(di_img, 127, 255, cv2.THRESH_BINARY)
    # ret, morphed_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return  ret, morphed_img



# set a threshold for area. all contours with smaller area get deleted
def del_small_contours(contour_list):
    area_threshold = fish_size_threshold
    if contour_list is not None and len(contour_list) > 0:

        counter = 0
        while counter < len(contour_list):

            popped = False

            # print "contour nr" + str(counter) + ": area  = " + str(cv2.contourArea(contour_list[counter]))
            if cv2.contourArea(contour_list[counter]) < area_threshold:
                contour_list.pop(counter)
                popped = True
            if not popped:
                # print(cv2.contourArea(contour_list[counter]))
                counter += 1
    return contour_list


# calculates distance of two given points (tuples)
def calculate_distance(p1, p2):
    x_diff = p2[0] - p1[0]
    y_diff = p2[1] - p1[1]
    dist = math.sqrt(x_diff*x_diff + y_diff*y_diff)
    return dist

# get center of contour based on fitting ellipse
def get_center(cnt):
    ellipse = cv2.fitEllipse(cnt)
    return ellipse[0]

# merge biggest contour with nearest
def merge_biggest_contour_with_nearest(contour_list):

    if contour_list is None or len(contour_list) < 2:
        return


    merge_threshold = 100
    near_cnts = []

    biggest = 0

    for i in range(0, len(contour_list)):
        if cv2.contourArea(contour_list[i]) > cv2.contourArea(contour_list[biggest]):
            biggest = i

    print "biggest area before: " + str(cv2.contourArea(contour_list[biggest]))

    # store all contours that are near the biggest one
    biggest_center = get_center(contour_list[biggest])
    counter = 0
    for cnt in contour_list:
        dist = calculate_distance(biggest_center, get_center(cnt))
        if dist < merge_threshold:
            near_cnts.append((counter, dist))
        counter += 1

    # find the nearest one
    nearest = 0
    near_counter = 0
    for entry in near_cnts:
        if entry[1] < near_cnts[near_counter][1]:
            nearest = near_counter
        near_counter += 1


    # merge biggest with nearest
    if near_cnts is not None and len(near_cnts) > 0 and biggest != near_cnts[nearest][0]:
        # print "before" + str(contour_list)
        contour_list.append(np.append(contour_list[biggest], contour_list[near_cnts[nearest][0]], axis=0))
        # print "after " + str(contour_list)
        print "biggest area after: " + str(cv2.contourArea(contour_list[len(contour_list)-1]))

    return contour_list

def save_number_of_contours(contour_list, number_cnt_list):
    if contour_list is None:
        number_cnt_list.append(0)
    else:
        number_cnt_list.append(len(contour_list))

# only keep biggest-area object in contour list
def keep_biggest_contours(contour_list):
    if contour_list is None or len(contour_list) == 0:
        return

    biggest = cv2.contourArea(contour_list[0])

    counter = 1
    while counter < len(contour_list):
        next_size = cv2.contourArea(contour_list[counter])
        if next_size < biggest:
            contour_list.pop(counter)
        elif next_size > biggest:
            biggest = next_size
            contour_list.pop(counter-1)
        else:
            counter += 1

    return contour_list




# if two or more contours (of same size) in contour_list delete which is farthest away from last pos fish was
def keep_nearest_contour(contour_list):

    global last_pos
    if last_pos is None:
        last_pos = (ROI_Y2-ROI_Y1, int((ROI_X2-ROI_X1)/2))

    cnt_center = get_center(ellipse[0])
    biggest_dist= calculate_distance(cnt_center, last_pos)

    counter = 1
    while counter < len(contour_list):
        next_center = get_center(ellipse[counter])
        next_dist = calculate_distance(next_center, last_pos)
        if next_dist < biggest_dist:
            contour_list.pop(counter)
        elif next_dist > biggest_dist:
            biggest_dist = next_dist
            contour_list.pop(counter-1)
        else:
            counter += 1

    return contour_list



# check if fish started from the right side
def check_if_fish_started(contour_list, roi):
    global starting_area_x_factor, starting_area_y1_factor, starting_area_y2_factor
    height, width, depth = roi.shape
    non_starting_area_x = int(starting_area_x_factor * width)
    non_starting_area_y1 = int(starting_area_y1_factor * height)
    non_starting_area_y2 = int(starting_area_y2_factor * height)

    if contour_list is not None:
        for i in range(0, len(contour_list)):
            cnt = contour_list[i]
            ellipse = cv2.fitEllipse(cnt)
            if ellipse[0][0] > non_starting_area_x and ellipse[0][1] > non_starting_area_y1 and ellipse[0][1] < non_starting_area_y2:
                global fish_started
                fish_started = True



# fitting ellipse onto contour
def fit_ellipse_on_contour(contour_list):
    global ellipse
    if contour_list is None or len(contour_list) == 0:
        ellipse = None
    elif contour_list is not None and len(contour_list) > 0:
        if len(contour_list) > 0:
            cnt = contour_list[0]
            ellipse = cv2.fitEllipse(cnt)
            ## center: ellipse[0]
            ## size  : ellipse[1]
            ## angle : ellipse[2]
            # print ellipse


# calculates start and endpoint for a line displaying the orientation of given ellipse (thus of the fish)
def get_line_from_ellipse():
    global ellipse

    center_x = ellipse[0][0]
    center_y = ellipse[0][1]
    grade_angle = -1 * ellipse[2]
    # print "ellipse angle: " +  str(ellipse[2])
    # print "  grade angle: " + str(grade_angle)
    angle_prop = grade_angle/180
    angle = math.pi*angle_prop
    # print "        angle: " + str(angle)

    x_dif = math.sin(angle)
    y_dif = math.cos(angle)

    x1 = int(round(center_x - line_point_offset*x_dif))
    y1 = int(round(center_y - line_point_offset*y_dif))
    x2 = int(round(center_x + line_point_offset*x_dif))
    y2 = int(round(center_y + line_point_offset*y_dif))

    return x1, y1, x2, y2

def append_to_travel_orientation(lx1, ly1, lx2, ly2):
    coordinates = (lx1, ly1, lx2, ly2)
    img_travel_orientation.append(coordinates)

def append_to_travel_route():
    global ellipse
    if ellipse is not None:
        ellipse_x = int(round(ellipse[0][0]))
        ellipse_y = int(round(ellipse[0][1]))
        point = (ellipse_x, ellipse_y)
        img_travel_route.append(point)

def set_last_pos():
    global last_pos
    global ellipse
    if ellipse is None:
        last_pos = None
        return
    else:
        last_pos = ellipse[0]

def save_fish_positions():
    global last_pos
    all_pos_roi.append(last_pos)
    if last_pos is None:
        all_pos_original.append(last_pos)
    else:
        original_x = last_pos[0]+ROI_X1
        original_y = last_pos[1]+ROI_Y1
        all_pos_original.append((original_x,original_y))

def set_last_orientation():
    global last_ori, start_ori
    global ellipse
    if not fish_started or ellipse is None:
        return

    global last_ori
    if last_ori is None:
        last_ori = start_ori

    if ellipse is None:
        return

    ell_ori = ellipse[2]
    if last_ori > ell_ori:
        ori_diff = last_ori - ell_ori
        if ori_diff > 270:
            last_ori = ell_ori
        elif ori_diff < 90:
            last_ori = ell_ori
        else:
            last_ori = (ell_ori + 180) % 360
    if last_ori < ell_ori:
        ori_diff = ell_ori - last_ori
        if ori_diff < 90:
            last_ori = ell_ori
        else:
            last_ori = (ell_ori + 180) % 360

def save_fish_orientations():
    if not fish_started:
        all_oris.append(None)
        return

    global ellipse
    if ellipse is None:
        all_oris.append(None)
        return

    global last_ori
    all_oris.append(last_ori)

def estimate_missing_pos():
    global frame_counter
    global all_pos_roi
    global estimated_pos_roi
    global estimated_pos_original
    global ROI_X1
    global ROI_Y1

    # init length of estimated-lists to amount of frames
    for x in range(0, frame_counter):
        estimated_pos_roi.append(None)
        estimated_pos_original.append(None)

    # set pointer to start of data
    pointer =  0
    while pointer < frame_counter and all_pos_roi[pointer] is None:
        pointer += 1

    while pointer < frame_counter:
        while all_pos_roi[pointer] is not None:
            pointer += 1
            if pointer >= frame_counter-1:
                return

        gap_start_pointer = pointer
        gap_end_pointer = pointer
        while gap_end_pointer < frame_counter-1 and all_pos_roi[gap_end_pointer] is None:
            gap_end_pointer += 1

        if gap_end_pointer == frame_counter-1:
            break

        start_value_x = all_pos_roi[gap_start_pointer-1][0]
        start_value_y = all_pos_roi[gap_start_pointer-1][1]
        end_value_x = all_pos_roi[gap_end_pointer][0]
        end_value_y = all_pos_roi[gap_end_pointer][1]

        pointer_diff = gap_end_pointer - (gap_start_pointer-1)
        value_diff_x = end_value_x - start_value_x
        value_diff_y = end_value_y - start_value_y
        value_diff_x_part = value_diff_x/pointer_diff
        value_diff_y_part = value_diff_y/pointer_diff


        # print "pointer diff = " + str(pointer_diff)
        first_pos_estimated = False
        while pointer < gap_end_pointer:
            if not first_pos_estimated:
                estimated_pos_roi[pointer] = ((all_pos_roi[pointer-1][0] + value_diff_x_part), (all_pos_roi[pointer-1][1] + value_diff_y_part))
                estimated_pos_original[pointer] = (estimated_pos_roi[pointer][0] + ROI_X1, estimated_pos_roi[pointer][1] + ROI_Y1)
                first_pos_estimated = True
            else:
                estimated_pos_roi[pointer] = ((estimated_pos_roi[pointer-1][0] + value_diff_x_part), (estimated_pos_roi[pointer-1][1] + value_diff_y_part))
                estimated_pos_original[pointer] = (estimated_pos_roi[pointer][0] + ROI_X1, estimated_pos_roi[pointer][1] + ROI_Y1)
            pointer += 1


def estimate_missing_ori():
    global frame_counter
    global all_oris
    global estimated_oris

    # init length of estimated-list to amount of frames
    for x in range(0, frame_counter):
        estimated_oris.append(None)

    pointer = 0
    # set pointer to start of data
    while all_oris[pointer] is None:
        pointer += 1
        if pointer >= frame_counter-1:
                return

    while pointer < frame_counter:
        while all_oris[pointer] is not None:
            pointer += 1
            if pointer >= frame_counter-1:
                return

        gap_start_pointer = pointer
        gap_end_pointer = pointer
        while gap_end_pointer < frame_counter-1 and all_oris[gap_end_pointer] is None:
            gap_end_pointer += 1

        if gap_end_pointer == frame_counter-1:
            break

        start_value = all_oris[gap_start_pointer-1]
        end_value = all_oris[gap_end_pointer]

        pointer_diff = gap_end_pointer - (gap_start_pointer-1)
        value_diff = end_value - start_value
        if start_value > end_value and abs(value_diff) > 180:
            value_diff = (end_value + 360) - start_value
        elif start_value < end_value and abs(value_diff) > 180:
            value_diff = (end_value - 360) - start_value
        value_diff_part = value_diff/pointer_diff


        # print "pointer diff = " + str(pointer_diff)
        first_pos_estimated = False
        while pointer < gap_end_pointer:
            if not first_pos_estimated:
                estimated_oris[pointer] = (all_oris[pointer-1] + value_diff_part) % 360
                first_pos_estimated = True
            else:
                estimated_oris[pointer] = (estimated_oris[pointer-1] + value_diff_part) % 360
            pointer += 1



def run_Tracker():
    global frame_counter

    # create BG subtractor
    bg_sub = cv2.BackgroundSubtractorMOG2()

    # main loop
    while cap.isOpened():


        ret, frame = cap.read()

        if frame is None:
            break

        frame_counter += 1

        # set region of interest ROI
        roi = copy.copy(frame[ROI_Y1:ROI_Y2, ROI_X1:ROI_X2])
        roi_output = copy.copy(roi)

        frame_output = copy.copy(frame)

        # subtract background fro ROI
        roi_bg_sub = bg_sub.apply(roi)

        # morph img
        ret, mo_roi_bg_sub = morph_img(roi_bg_sub)

        # detect edges of bg-deleted img
        edges = cv2.Canny(mo_roi_bg_sub, 500, 500)

        # detect edges of morphed img (not displayed)
        mo_edges = cv2.Canny(mo_roi_bg_sub, 500, 500)


        # getting contours (of the morphed img)
        ret,thresh_img = cv2.threshold(mo_roi_bg_sub,127,255,cv2.THRESH_BINARY)
        contour_list, hierarchy = cv2.findContours(thresh_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        # TODO
        # merge biggest contour with nearest
        # contour_list = merge_biggest_contour_with_nearest(contour_list)

        # save amount of contours
        global number_contours_per_frame
        save_number_of_contours(contour_list, number_contours_per_frame)

        # everything below fish_size_threshold is being ignored
        contour_list = del_small_contours(contour_list)

        # save number of remaining contours
        global number_relevant_contours_per_frame
        save_number_of_contours(contour_list, number_relevant_contours_per_frame)

        # check if fish started
        if not fish_started:
            check_if_fish_started(contour_list, roi)

        # if fish hasn't started yet, delete all contours
        if not fish_started:
            contour_list = []

        # keep only biggest contours
        contour_list = keep_biggest_contours(contour_list)


        # if two or more contours (of same size) in list delete which is farthest away from last point
        if fish_started and contour_list is not None and len(contour_list) > 1:
            contour_list = keep_nearest_contour(contour_list)


        # draw countours to ROI img and show img
        if DRAW_CONTOUR:
            cv2.drawContours(roi, contour_list, -1, (0,255,0), 3)

        # fit ellipse on contour
        fit_ellipse_on_contour(contour_list)
        # draw ellipse
        if DRAW_ELLIPSE and ellipse is not None and fish_started:
            cv2.ellipse(roi,ellipse,(0, 0, 255),2)

        # get line from ellipse
        if fish_started and ellipse is not None:
            lx1, ly1, lx2, ly2 = get_line_from_ellipse()
        # draw line
        if DRAW_LINE and ellipse is not None:
            cv2.line(roi, (lx1, ly1), (lx2, ly2), (0,0,255), 1)


        # append ellipse center to travel route
        if DRAW_TRAVEL_ROUTE:
            append_to_travel_route()

        # set last_pos to ellipse center
        set_last_pos()

        # save fish positions
        save_fish_positions()

        # set last orientation
        set_last_orientation()

        # save orientations
        save_fish_orientations()

        # append coordinates to travel_orientation
        if DRAW_TRAVEL_ORIENTATION and fish_started:
            append_to_travel_orientation(lx1, ly1, lx2, ly2)


        # draw travel route
        if DRAW_TRAVEL_ORIENTATION:
            for coordinates in img_travel_orientation:
                cv2.line(roi, (coordinates[0], coordinates[1]), (coordinates[2], coordinates[3]), (150,150,0), 1)

        # draw travel orientation
        if DRAW_TRAVEL_ROUTE:
            for point in img_travel_route:
                cv2.circle(roi, point, 2, (255, 0, 0))

        if DRAW_ORIGINAL_OUTPUT:
            for coordinates in img_travel_orientation:
                cv2.line(frame_output, (coordinates[0]+ROI_X1, coordinates[1]+ROI_Y1), (coordinates[2]+ROI_X1, coordinates[3]+ROI_Y1), (150,150,0), 1)
            for point in all_pos_original:
                if point is not None:
                    cv2.circle(frame_output, (int(round(point[0])), int(round(point[1]))), 2, (255, 0, 0))



        # show all imgs
        if DRAW_ORIGINAL_OUTPUT:
            show_imgs(frame_output, roi_output, roi_bg_sub, mo_roi_bg_sub, edges)
        else:
            show_imgs(frame, roi_output, roi_bg_sub, mo_roi_bg_sub, edges)

        # show output img
        cv2.imshow("contours", roi)
        # if SAVE_FRAMES:
        #     cv2.imwrite(dir + "frames/" + str(frame_counter) + "_contours" + ".jpg", roi)



        global last_frame
        last_frame = roi
        global last_frame_OV_output
        last_frame_OV_output = frame_output

        if cv2.waitKey(FRAME_WAITTIME) & 0xFF == 27:
            break


    cap.release()
    cv2.destroyAllWindows()


def print_data():
    print "positions region of interest: " + str(all_pos_roi)
    print "estimated positions roi:      " + str(estimated_pos_roi)
    print "positions original recording: " + str(all_pos_original)
    print "estimated positions original: " + str(estimated_pos_original)
    print "all orientations:             " + str(all_oris)
    print "estimated orientations:       " + str(estimated_oris)
    print "number of contours in frames: " + str(number_contours_per_frame)
    print "number of fish-size contours: " + str(number_relevant_contours_per_frame)
    if not len(all_pos_roi) == len(all_pos_original) == len(all_oris) == frame_counter:
        print "WARNING: Something went wrong. Length of Lists saving fish data not consistent with frame count!"

    print "All lists consistent with frame count: " + str(len(all_pos_roi) == len(all_pos_original) == len(all_oris) == len(number_contours_per_frame) == len(number_relevant_contours_per_frame) == frame_counter)

def fill_spaces(file, string):
    for i in range(0, 20-len(string)):
        file.write(" ")

def print_None_to_file(file):
    for i in range(0, 16):
        file.write(" ")
    file.write("None")



def save_data_to_files():
    global ROI_X1, ROI_X2, ROI_Y1, ROI_Y2
    global fish_size_threshold
    global start_ori

    file_name, file_directory = extract_video_file_name_and_path()

    ###
    ### save data into txt file
    ###

    global output_directory
    # define ouput directory name as file name
    output_directory = file_directory + file_name

    #check if times file in same folder as video file
    times_file_path = file_directory + file_name + "_times.dat"
    times_file = None
    if not os.path.exists(times_file_path):
        print "times file missing - data saving abortet"
        return
    else:
        times_file = open(times_file_path, 'r')

    # create directory name after video file
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    # else:
    #     print "directory exists"

    output_file_path = output_directory + "/" + file_name + ".txt"
    output_file = open(output_file_path, 'w')

    output_file.write("# Tracking parameters:\n")
    output_file.write("#     Region of Interest X-Axis         : [" + str(ROI_X1) + "," + str(ROI_X2) + "]\n")
    output_file.write("#     Region of Interest Y-Axis         : [" + str(ROI_Y1) + "," + str(ROI_Y2) + "]\n")
    output_file.write("#     Fish size threshold               : " + str(fish_size_threshold) + "\n")
    output_file.write("#     Start orientation                 : " + str(start_ori) + "\n")
    output_file.write("#     Fish starting area X-Axis factor  : " + str(starting_area_x_factor) + "\n")
    output_file.write("#     Fish starting area Y-Axis factor 1: " + str(starting_area_y1_factor) + "\n")
    output_file.write("#     Fish starting area Y-Axis factor 2: " + str(starting_area_y2_factor) + "\n")
    output_file.write("#\n")
    output_file.write("#     Orientation algorithm assumes that fish can not turn more than >> 90 << degrees from one frame to the next\n")

    output_file.write("\n#Key\n")
    output_file.write("#           frame_time               pos_roi_x               pos_roi_y           est_pos_roi_x           est_pos_roi_y          pos_original_x          pos_original_y      est_pos_original_x      est_pos_original_y            orientations        est_orientations           obj_per_frame       fishobj_per_frame\n")

    lc = 0
    spacing = 4
    for line in times_file:

        output_file.write("  ")
        line = line.strip()
        fill_spaces(output_file, line)
        output_file.write(line)
        output_file.write(" "*spacing)

        if all_pos_roi[lc] is None:
            print_None_to_file(output_file)
        else:
            rounded_x_pos_original = str(round(all_pos_roi[lc][0], 2))
            fill_spaces(output_file, rounded_x_pos_original)
            output_file.write(rounded_x_pos_original)
        output_file.write(" "*spacing)

        if all_pos_roi[lc] is None:
            print_None_to_file(output_file)
        else:
            rounded_y_pos_original = str(round(all_pos_roi[lc][1], 2))
            fill_spaces(output_file, rounded_y_pos_original)
            output_file.write(rounded_y_pos_original)
        output_file.write(" "*spacing)

        if estimated_pos_roi[lc] is None:
            print_None_to_file(output_file)
        else:
            rounded_est_x_pos_original = str(round(estimated_pos_roi[lc][0], 2))
            fill_spaces(output_file, rounded_est_x_pos_original)
            output_file.write(rounded_est_x_pos_original)
        output_file.write(" "*spacing)

        if estimated_pos_roi[lc] is None:
            print_None_to_file(output_file)
        else:
            rounded_est_y_pos_original = str(round(estimated_pos_roi[lc][1], 2))
            fill_spaces(output_file, rounded_est_y_pos_original)
            output_file.write(rounded_est_y_pos_original)
        output_file.write(" "*spacing)


        if all_pos_original[lc] is None:
            print_None_to_file(output_file)
        else:
            rounded_x_pos_original = str(round(all_pos_original[lc][0], 2))
            fill_spaces(output_file, rounded_x_pos_original)
            output_file.write(rounded_x_pos_original)
        output_file.write(" "*spacing)

        if all_pos_original[lc] is None:
            print_None_to_file(output_file)
        else:
            rounded_y_pos_original = str(round(all_pos_original[lc][1], 2))
            fill_spaces(output_file, rounded_y_pos_original)
            output_file.write(rounded_y_pos_original)
        output_file.write(" "*spacing)

        if estimated_pos_original[lc] is None:
            print_None_to_file(output_file)
        else:
            rounded_est_x_pos_original = str(round(estimated_pos_original[lc][0], 2))
            fill_spaces(output_file, rounded_est_x_pos_original)
            output_file.write(rounded_est_x_pos_original)
        output_file.write(" "*spacing)

        if estimated_pos_original[lc] is None:
            print_None_to_file(output_file)
        else:
            rounded_est_y_pos_original = str(round(estimated_pos_original[lc][1], 2))
            fill_spaces(output_file, rounded_est_y_pos_original)
            output_file.write(rounded_est_y_pos_original)
        output_file.write(" "*spacing)

        if all_oris[lc] is None:
            print_None_to_file(output_file)
        else:
            rounded_ori = str(round(all_oris[lc], 2))
            fill_spaces(output_file, rounded_ori)
            output_file.write(rounded_ori)
        output_file.write(" "*spacing)

        if estimated_oris[lc] is None:
            print_None_to_file(output_file)
        else:
            rounded_est_ori = str(round(estimated_oris[lc], 2))
            fill_spaces(output_file, rounded_est_ori)
            output_file.write(rounded_est_ori)
        output_file.write(" "*spacing)

        cnt_of_frame = str(number_contours_per_frame[lc])
        fill_spaces(output_file, cnt_of_frame)
        output_file.write(cnt_of_frame)
        output_file.write(" "*spacing)

        rel_cnt_of_frame = str(number_relevant_contours_per_frame[lc])
        fill_spaces(output_file, rel_cnt_of_frame)
        output_file.write(rel_cnt_of_frame)



        output_file.write("\n")

        lc += 1

    #save last frame
    cv2.imwrite(output_directory + "/" + file_name + "_OV_path.png", last_frame_OV_output)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='tracking fish in video file')
    # parser.add_argument('path', type=str,
    #                     help="absolute file path to video including file name")
    # args = parser.parse_args()

    set_video_file()
    set_video_capture()

    run_Tracker()
    cv2.namedWindow("result")
    cv2.moveWindow("result", 200, 350)


    if ESTIMATE_MISSING_DATA:
        estimate_missing_pos()
        for c in estimated_pos_roi:
            if c is not None:
                cv2.circle(last_frame, (int(round(c[0])), int(round(c[1]))), 2, (0, 0, 255))
                cv2.circle(last_frame_OV_output, (int(round(c[0]))+ROI_X1, int(round(c[1])+ROI_Y1)), 2, (0, 0, 255))

        estimate_missing_ori()

    print_data()


    cv2.imshow("result", last_frame)
    # if SAVE_FRAMES:
    #     cv2.imwrite(dir + "frames/" + str(frame_counter) + "_estimation" + ".jpg", last_frame)

    save_data_to_files()

    if DRAW_ORIGINAL_OUTPUT:
        cv2.namedWindow("result_ov")
        cv2.moveWindow("result_ov", 900, 350)
        cv2.imshow("result_ov", last_frame_OV_output)
    cv2.waitKey(0)
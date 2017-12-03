import os
import cv2
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

path = '3D_images/'
output_path = 'binary_images/'
dir_list = os.listdir(path)


def readimg(filename):
    im = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    tmp_im = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    for i in range(512):
        for j in range(512):
            if im[i][j] <= 3:
                im[i][j] = 1
            else:
                im[i][j] = 254

    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 0
    params.maxThreshold = 300

    # Filter by Color.
    params.filterByColor = True
    params.blobColor = 255

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.01

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.07

    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.01

    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(im)

    # xs = []
    # ys = []
    # for point in keypoints:
    #     xs.append(int(keypoints[0].pt[1]))
    #     ys.append(int(keypoints[0].pt[0]))
    #
    # return xs, ys

    # im_with_keypoints = cv2.drawKeypoints(tmp_im, keypoints, np.array([]), (0, 0, 255),
    #                                       cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # print('color: ' + str(tmp_im[int(keypoints[0].pt[1])][int(keypoints[0].pt[0])]))
    # cv2.imshow("output_1", im_with_keypoints)
    # cv2.imshow("output_2", im)
    # cv2.waitKey(0)
    # cv2.waitKey(0)
    # plt.savefig(output_path + filename)
    cv2.imwrite(filename, im)


def rewrite_all():
    for filename in dir_list:
        print(filename)
        if filename[-4:] != '.jpg':
            continue
        # print(filename)
        readimg(path + filename)


rewrite_all()



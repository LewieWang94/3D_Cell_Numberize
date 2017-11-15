import os
import cv2
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

path = '3D_images/'
dir_list = os.listdir(path)


def readimg(filename):
    im = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
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

    xs = []
    ys = []
    for point in keypoints:
        xs.append(int(keypoints[0].pt[1]))
        ys.append(int(keypoints[0].pt[0]))

    return xs, ys

    # im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255),
    #                                       cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # print('color: ' + str(im[int(keypoints[0].pt[1])][int(keypoints[0].pt[0])]))
    # cv2.imshow("output", im_with_keypoints)
    # k = cv2.waitKey(0)


def show_one_time(time):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for filename in dir_list:
        t = int(filename[2:4])
        s = int(filename[7:10])
        if t == time:
            xs, ys = readimg(path + filename)
            for index in range(len(xs)):
                ax.scatter(xs[index], ys[index], s, c='r', marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    # plt.show()
    plt.savefig(str(time) + '_time')


for i in range(1, 21):
    show_one_time(i)

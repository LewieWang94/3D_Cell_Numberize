import cv2
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

points = []
data = open('true_pos_1.txt', 'r')
for line in data.readlines():
    arr = line.split()
    points.append((int(arr[0]), int(arr[1]), int(arr[2])))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for point in points:
    if 0 <= point[2] <= 100:
        ax.scatter(point[0], point[1], point[2], c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
# plt.savefig(str(time) + '_time')
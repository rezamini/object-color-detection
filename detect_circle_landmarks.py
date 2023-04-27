import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

original_image = cv.imread("example_shapes7.png")
output_image = original_image.copy()
gray = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
hist = cv.equalizeHist(gray)
blur = cv.GaussianBlur(hist, (31,31), cv.BORDER_DEFAULT)
height, width = blur.shape[:2]
minR = round(width/65)
maxR = round(width/11)
minDis = round(width/7)

circles = cv.HoughCircles(blur, cv.HOUGH_GRADIENT, 1, minDis, param1=14, param2=30, minRadius=minR, maxRadius=maxR)

# Draw circles
if circles is not None:
    detected_circles = np.uint16(np.around(circles))
    for (x,y,r) in detected_circles[0, :]:
        # cv2.circle(image, (x,y), r, (36,255,12), 3)
        cv.circle(output_image, (x, y), r, (255, 255, 255), 3)
        cv.circle(output_image, (x, y), 2, (0, 255, 255), 3)

cv.imshow("result", np.hstack([original_image, output_image]))
cv.waitKey(0)
cv.destroyAllWindows()
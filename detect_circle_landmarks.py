import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from detect_landmark_color import DetectLandmarkColor
import math
from apicalls import ApiCalls

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
detectLandmarkColor = DetectLandmarkColor()
api = ApiCalls()

# Draw circles
if circles is not None:
    detected_circles = np.uint16(np.around(circles))
    for (x,y,r) in detected_circles[0, :]:
        landmark_color, bgr_color = detectLandmarkColor.detect_color(original_image, y, x)

        cv.circle(output_image, (x,y), r, (255,255,255), 3) #outer circle
        # cv.circle(output_image, (x, y), 2, (255, 255, 255), 3)# inner circle/dot
        
        cv.putText(output_image, landmark_color, (x+r, y+r+r),
            cv.FONT_HERSHEY_SIMPLEX, 0.5, (int(bgr_color[0]), int(bgr_color[1]), int(bgr_color[2])), 2)



# cv.circle(original_image, (422, 198), 1, (0, 0, 0), 3)
# print(hsv_frame[198, 422])

api.send_data("A")

cv.imshow("result", np.hstack([original_image, output_image]))
cv.waitKey(0)
cv.destroyAllWindows()



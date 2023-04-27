# import numpy
# import cv2

# image = cv2.imread("example_shapes6.png")
# output = image.copy()

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# hist = cv2.equalizeHist(gray)

# blur = cv2.GaussianBlur(hist, (31,31), cv2.BORDER_DEFAULT)
# height, width = blur.shape[:2]

# minR = round(width/65)
# maxR = round(width/11)
# minDis = round(width/7)

# circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, minDis, param1=14, param2=25, minRadius=minR, maxRadius=maxR)

# if circles is not None:
#     circles = numpy.round(circles[0, :]).astype("int")
#     for (x, y, r) in circles:
#         cv2.circle(output, (x, y), r, (0, 255, 0), 2)
#         cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
# cv2.imshow("result", numpy.hstack([image, output]))
# cv2.waitKey()


# import matplotlib.pyplot as plt
# import numpy as np
# import cv2 as cv

# img = cv.imread("example_shapes4.png")
# output = img.copy()
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# # gray = cv.medianBlur(gray, 5)
# # circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, minDist=120,
# #                             param1=100, param2=30, minRadius=0, maxRadius=0)
# hist = cv.equalizeHist(gray)
# blur = cv.GaussianBlur(hist, (31,31), cv.BORDER_DEFAULT)
# height, width = blur.shape[:2]
# minR = round(width/65)
# maxR = round(width/11)
# minDis = round(width/7)

# circles = cv.HoughCircles(blur, cv.HOUGH_GRADIENT, 1, minDis, param1=14, param2=25, minRadius=minR, maxRadius=maxR)


# # Draw circles
# if circles is not None:
#     detected_circles = np.uint16(np.around(circles))
#     for (x,y,r) in detected_circles[0, :]:
#         # cv2.circle(image, (x,y), r, (36,255,12), 3)
#         cv.circle(output, (x, y), r, (0, 255, 0), 3)
#         cv.circle(output, (x, y), 2, (0, 255, 255), 3)

# cv.imshow("output", output)
# cv.waitKey(0)
# cv.destroyAllWindows()


# import cv2
# import numpy as np

# # Load image, grayscale, Otsu's threshold
# image = cv2.imread('example_shapes3.png')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# # Find circles with HoughCircles
# circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, 1, minDist=150, param1=200, param2=18, minRadius=20)

# # Draw circles
# if circles is not None:
#     circles = np.round(circles[0, :]).astype("int")
#     for (x,y,r) in circles:
#         # cv2.circle(image, (x,y), r, (36,255,12), 3)
#         cv2.circle(image, (x, y), r, (0, 255, 0), 3)
#         cv2.circle(image, (x, y), 2, (0, 255, 255), 3)

# cv2.imshow('thresh', thresh)
# cv2.imshow('image', image)
# cv2.waitKey()







# msg = "hello world"
# x = [24, 25, 26, 27, 28]
# y = [23, 24, 25, 29, 30]
# plt.plot(x, y)
# plt.show()
# print(msg)
# print(msg)

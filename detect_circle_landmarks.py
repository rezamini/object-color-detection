import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
# from detect_landmark_color import DetectLandmarkColor
from apicalls import ApiCalls


class DetectCircleLandmarks:
    # detectLandmarkColor = DetectLandmarkColor()
    api = ApiCalls()
    color_result = set()

    def __init__(self):
        pass

    def detect_circles(self, image_path, image_name):
        original_image = cv.imread(image_path + image_name)
        # output_image = original_image.copy()
        gray = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
        hist = cv.equalizeHist(gray)
        blur = cv.GaussianBlur(hist, (31, 31), cv.BORDER_DEFAULT)
        height, width = blur.shape[:2]
        minR = round(width/65)
        maxR = round(width/11)
        minDis = round(width/7)
        circles = cv.HoughCircles(blur, cv.HOUGH_GRADIENT, 1, minDis,
                                  param1=14, param2=30, minRadius=minR, maxRadius=maxR)
        # self.__perform_color_detection(image_name, original_image, output_image, circles)

        return image_name, original_image, circles

    def draw_detected_landmarks(self, original_image, output_image, circles, detected_colors, bgr_colors):
        if circles is not None:
            detected_circles = np.uint16(np.around(circles))
            for index, (x, y, r) in enumerate(detected_circles[0, :]):
                landmark_color = detected_colors[index]

                cv.circle(output_image, (x, y), r,
                          (255, 255, 255), 3)  # outer circle

                cv.putText(output_image, landmark_color.upper(), (x+r, y+r+r),
                           cv.FONT_HERSHEY_SIMPLEX, 0.5, (int(bgr_colors[index][0]), int(bgr_colors[index][1]), int(bgr_colors[index][2])), 2)

            # self.api.send_data(self.colorResult)
            cv.imshow("result", np.hstack([original_image, output_image]))
            cv.waitKey(0)
            cv.destroyAllWindows()

    # def perform_color_detection(self, image_name, original_image, output_image, circles):
    #     if circles is not None:
    #         temp_color_result = set()
    #         detected_circles = np.uint16(np.around(circles))
    #         for (x,y,r) in detected_circles[0, :]:
    #             landmark_color, bgr_color = self.detectLandmarkColor.detect_color(original_image, y, x)
    #             temp_color_result.add(landmark_color.lower())

    #             #modify output image if draw_result is true
    #             if self.draw_result:
    #                 cv.circle(output_image, (x,y), r, (255,255,255), 3) #outer circle
    #                 # cv.circle(output_image, (x, y), 2, (255, 255, 255), 3)# inner circle/dot
    #                 cv.putText(output_image, landmark_color, (x+r, y+r+r),
    #                     cv.FONT_HERSHEY_SIMPLEX, 0.5, (int(bgr_color[0]), int(bgr_color[1]), int(bgr_color[2])), 2)

    #     #add detected colors to the main result
    #     self.color_result.update(temp_color_result)

    #     #print the detected colors for every image
    #     print("------------ Detected Colors for file [" + image_name + "] ------------")
    #     print(temp_color_result)

    #     #display image differences if draw_result is true
    #     if self.draw_result:
    #         self.draw_detected_landmarks(original_image, output_image)

    # def draw_detected_landmarks(self, original_image, output_image):

    #     # self.api.send_data(self.colorResult)
    #     cv.imshow("result", np.hstack([original_image, output_image]))
    #     cv.waitKey(0)
    #     cv.destroyAllWindows()

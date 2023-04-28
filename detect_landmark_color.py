import cv2 as cv
# from sklearn.cluster import KMeans
# import numpy as np

class DetectLandmarkColor:
    color_ranges = {
        (170, 10): "RED",
        (10, 25): "ORANGE",
        (25, 35): "YELLOW",
        (35, 70): "GREEN",
        (70, 110): "CYAN",
        (110, 130): "BLUE",
        (130, 160): "PURPLE",
        (160, 170): "PINK"
    }

    def self(self):
        pass

    def detect_color(self, original_image, y, x):
        hsv_frame = cv.cvtColor(original_image, cv.COLOR_BGR2HSV)
        pixels_center = hsv_frame[y, x]

        color = "undefined"
        hue_value = pixels_center[0]

        color = next((color_name for (lower, upper), color_name in self.color_ranges.items(
        ) if lower <= hue_value < upper), "undefined")

        # if hue_value < 5:
        #     color = "RED"
        # elif hue_value < 22:
        #     color = "ORANGE"
        # elif hue_value < 33:
        #     color = "YELLOW"
        # elif hue_value < 78:
        #     color = "GREEN"
        # elif hue_value < 131:
        #     color = "BLUE"
        # elif hue_value < 170:
        #     color = "VIOLET"

        return color

import cv2 as cv
# from sklearn.cluster import KMeans
import numpy as np


class DetectLandmarkColor:
    color_result = list()

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

    def __init__(self):
        pass

    def detect_colors(self, image_name, original_image, circles):
        if circles is not None:
            temp_color_result = list()
            temp_bgr_colors = list()

            detected_circles = np.uint16(np.around(circles))
            for (x,y,r) in detected_circles[0, :]:
                landmark_color, bgr_color = self.__detect_single_color(original_image, y, x)

                if landmark_color.lower() != "undefined" :
                    temp_color_result.append(landmark_color.lower())
                    temp_bgr_colors.append(bgr_color)


        #add detected colors to the main result  
        self.color_result.extend(temp_color_result)

        #print the detected colors for every image
        print("------------ Detected Unique Colors for file [" + image_name + "] ------------")
        print(set(temp_color_result))

        return temp_color_result, temp_bgr_colors

    def __detect_single_color(self, original_image, y, x):
        hsv_frame = cv.cvtColor(original_image, cv.COLOR_BGR2HSV)
        pixels_center = hsv_frame[y, x]

        color_name = "undefined"
        hue_value = pixels_center[0]

        color_name = next((color_name for (lower, upper), color_name in self.color_ranges.items(
        ) if lower <= hue_value < upper), "undefined")

        #convert the hue value back to bgr in order to be used for text or circle colors
        rgb_color = np.uint8([[[hue_value, 255, 255]]])
        rgb_color = cv.cvtColor(rgb_color, cv.COLOR_HSV2RGB)
        bgr_color = cv.cvtColor(rgb_color, cv.COLOR_RGB2BGR)

        # Detect pixel color from original image. but it might detect wrongly if there is a text on the landmark. it will detect text color
        # pixel_bgr_values = original_image[int(y), int(x + 2)]
        # bgr_1, bgr_2, bgr_3 = int(pixel_bgr_values[0]), int(pixel_bgr_values[1]), int(pixel_bgr_values[2])
        
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

        return color_name, bgr_color[0, 0, :]

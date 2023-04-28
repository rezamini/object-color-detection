import cv2 as cv

class DetectLandmarkColor:
    def self(self):
        pass

    def detect_color(self, original_image, y, x):
        hsv_frame = cv.cvtColor(original_image, cv.COLOR_BGR2HSV)
        pixels_center = hsv_frame[y, x]
        
        color = "undefined"
        hue_value = pixels_center[0]

        if hue_value < 5:
            color = "RED"
        elif hue_value < 22:
            color = "ORANGE"
        elif hue_value < 33:
            color = "YELLOW"
        elif hue_value < 78:
            color = "GREEN"
        elif hue_value < 131:
            color = "BLUE"
        elif hue_value < 170:
            color = "VIOLET"
        
        return color

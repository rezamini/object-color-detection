import os
from detect_circle_landmarks import DetectCircleLandmarks
from detect_landmark_color import DetectLandmarkColor
from apicalls import ApiCalls

IMAGE_FOLDER_PATH = "images/"

detectLandmark = DetectCircleLandmarks()
detectLandmarkColor = DetectLandmarkColor()
api = ApiCalls()

# image_name, original_image, circles = detect.detect_circles(IMAGE_FOLDER_PATH, "example_shapes8.png")
# detected_colors, bgr_colors = detectLandmarkColor.detect_colors(image_name, original_image, circles)
# detect.draw_detected_landmarks(original_image, original_image.copy(), circles, detected_colors, bgr_colors)

# loop and detect entire image folder files
for path, dirs, files in os.walk(IMAGE_FOLDER_PATH):
    for file in files:
        image_name, original_image, circles = detectLandmark.detect_circles(path, file)
        detected_colors, bgr_colors = detectLandmarkColor.detect_colors(image_name, original_image, circles)
        detectLandmark.draw_detected_landmarks(original_image, original_image.copy(), circles, detected_colors, bgr_colors) 

print("------------ FINAL UNIQUE DETECTED COLORS ------------")
print(set(detectLandmarkColor.color_result))

#call the api and post the detected result
# api.send_data(set(detectLandmarkColor.color_result))





import os
from detect_circle_landmarks import DetectCircleLandmarks

IMAGE_FOLDER_PATH = "images/"

detect = DetectCircleLandmarks(True)
# detect.detect_circles(IMAGE_FOLDER_PATH, "example_shapes7.png")

# loop and detect entire image folder files
for path, dirs, files in os.walk(IMAGE_FOLDER_PATH):
    for file in files:
        # image_path = os.path.join(path, file)
        detect.detect_circles(path, file)

print("------------ FINAL DETECTED COLORS ------------")
print(detect.color_result)





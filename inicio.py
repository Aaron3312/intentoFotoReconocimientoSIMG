from ultralytics import YOLO
import os
import cv2
import numpy as np
import time

model = YOLO("yolov8m.pt")

VIDEOS_DIR = os.path.join('.', "videos")
video_path = os.path.join(VIDEOS_DIR, "video1.mp4")
video_path_out = os.path.join("video1_out.mp4")

#capturamos la webcam
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
height, width, _ = frame.shape

out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

results = model.predict("cat_dog.jpg")
result = results[0]
len(result.boxes)

box = result.boxes[0]

print("Object type:", box.cls)
print("Coordinates:", box.xyxy)
print("Probability:", box.conf)

print("Object type:",box.cls[0])
print("Coordinates:",box.xyxy[0])
print("Probability:",box.conf[0])

cords = box.xyxy[0].tolist()
class_id = box.cls[0].item()
conf = box.conf[0].item()
print("Object type:", class_id)
print("Coordinates:", cords)
print("Probability:", conf)

print(result.names)

cords = box.xyxy[0].tolist()
cords = [round(x) for x in cords]
class_id = result.names[box.cls[0].item()]
conf = round(box.conf[0].item(), 2)
print("Object type:", class_id)
print("Coordinates:", cords)
print("Probability:", conf)

for box in result.boxes:
  class_id = result.names[box.cls[0].item()]
  cords = box.xyxy[0].tolist()
  cords = [round(x) for x in cords]
  conf = round(box.conf[0].item(), 2)
  print("Object type:", class_id)
  print("Coordinates:", cords)
  print("Probability:", conf)
  print("---")


# Run batched inference on a list of images
results = model(['im1.jpg', 'im2.jpg'], stream=True)  # return a generator of Results objects

# Process results generator
for result in results:
    boxes = result.boxes  # Boxes object for bbox outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs




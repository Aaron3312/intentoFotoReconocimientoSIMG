from ultralytics import YOLO
import cv2
import numpy as np
import math
import time
import matplotlib.pyplot as plt
from PIL import Image



model = YOLO("yolov8l.pt")  # yolov5s.pt

#the models are from worst to best 
#yolov5s.pt
#yolov5m.pt
#yolov5l.pt
#yolov5x.pt
#yolov8s.pt
#yolov8m.pt
#yolov8l.pt
#yolov8x.pt





#model.predict(source = "s.jpg", save=True, save_txt=True, save_conf=True, save_crop=True)
#model.predict(source = "http://192.168.100.114:4747/video", save=True, save_txt=True, save_conf=True, save_crop=True)

# Simulated depth data (placeholder for actual depth estimation)
# Replace this with real depth data from your hardware
distance_to_bottle = 2.0  # Placeholder value in meters

# Define a threshold distance for approaching the bottle
approach_threshold = 1.0  # Adjust as needed

# Capture video from a source (e.g., camera)
# Replace with your video source (e.g., camera or video file)
#video_source = "http://192.168.100.114:4747/video"
#video_source = 0
#video_source = "s.jpg"
#video_source = "rtsp://192.168.42.1/live"
video_source = "http://10.43.97.210:4747/video"

#cap = cv2.VideoCapture(video_source)
    

# Continuously process frames from the video source
#while True:
# Capture a frame from the video source
print("here")
#, save=False

results = model.predict(source=video_source, save_txt=False, save_conf=False, save_crop=False,show = True)
boxes = results[0].boxes  #

box = boxes[0]
box.xyxy
print(box)

#La idea es que desde aqui equipemos la idea para poder estar tomando screenshots constantes de la camara y poder analizarlas, asi con la retroalimentacion
#constante podremos tomar mejores decisiones de si se acerca o no a la botella




#how do i limit the number of pixels

#results = model.track(source="https://youtu.be/LNwODJXcvt4", save_txt=False, save_conf=False, stream=True,show = True)
#results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True)  # Tracking with default tracker



# Process results generator
#for result in results:
    #boxes = result.boxes  # Boxes object for bbox outputs
    #keypoints = result.keypoints  # Keypoints object for pose outputs
    #probs = result.probs  # Probs object for classification outputs
    #masks = result.masks  # Masks object for segmentation masks outputs
    # Check if the calculated distanc e is less than the approach threshold

#approaching = distance_to_bottle < approach_threshold


# Print the result (you can replace this with your desired action)
#if approaching:
#    print("Approaching the bottle!")
#else:
#    print("Not approaching the bottle.")

# Break the loop if needed (e.g., press a key to exit)
    # Add your exit condition here

# Release resources when done
#model.close()

#, conf=0.25
#model.export(format="onnx", dynamic=False, simplify=False)
#model.export(format="torchscript", dynamic=False, simplify=False)
#model.export(format="coreml", dynamic=False, simplify=False)
#model.export(format="tflite", dynamic=False, simplify=False)
#model.export(format="openvino", dynamic=False, simplify=False)




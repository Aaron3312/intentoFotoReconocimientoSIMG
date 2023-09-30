from ultralytics import YOLO
import cv2


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
video_source = "http://192.168.100.114:4747/video"
#video_source = 0

# Continuously process frames from the video source
while True:
    # Capture a frame from the video source
    print("here")
    results = model.predict(source=video_source, save=False, save_txt=False, save_conf=False, save_crop=False, stream=True,show = True)

    
    # Process results generator
    for result in results:
        boxes = result.boxes  # Boxes object for bbox outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        # Check if the calculated distance is less than the approach threshold
    
    approaching = distance_to_bottle < approach_threshold


    # Print the result (you can replace this with your desired action)
    if approaching:
        print("Approaching the bottle!")
    else:
        print("Not approaching the bottle.")

# Break the loop if needed (e.g., press a key to exit)
    # Add your exit condition here

# Release resources when done
model.close()

#, conf=0.25
#model.export(format="onnx", dynamic=False, simplify=False)
#model.export(format="torchscript", dynamic=False, simplify=False)
#model.export(format="coreml", dynamic=False, simplify=False)
#model.export(format="tflite", dynamic=False, simplify=False)
#model.export(format="openvino", dynamic=False, simplify=False)




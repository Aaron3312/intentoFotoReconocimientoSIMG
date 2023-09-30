from ultralytics import YOLO

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

model.predict(source = "s.jpg", save=True, save_txt=True, save_conf=True, save_crop=True)
#model.predict(source = "http://192.168.100.114:4747/video", save=True, save_txt=True, save_conf=True, save_crop=True)

#, conf=0.25
#model.export(format="onnx", dynamic=False, simplify=False)
#model.export(format="torchscript", dynamic=False, simplify=False)
#model.export(format="coreml", dynamic=False, simplify=False)
#model.export(format="tflite", dynamic=False, simplify=False)
#model.export(format="openvino", dynamic=False, simplify=False)




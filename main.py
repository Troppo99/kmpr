from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")
results = model(source=0, show=True, conf=0.5)

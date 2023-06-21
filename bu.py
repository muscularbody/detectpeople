from ultralytics import YOLO

model = YOLO('yolov8n.pt')

sonuc = model.predict(source="pe.mp4", show=True, save=True)

from ultralytics import YOLO

# Load the model
model = YOLO('yolov8n.pt')

# Training
results = model.train(
   data='/home/students/cs/201920962/datasets/obstacle/data.yaml',
   imgsz=640,
   epochs=1000,
   batch=32,
   project='/home/students/cs/201920962/yolov8/obstacle_model'
)

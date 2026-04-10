import cv2
from ultralytics import YOLO

class DetectorBagagem:
    def __init__(self):
        # Carrega o modelo nano do YOLOv8 (leve e rápido para o RNF-01)
        self.model = YOLO('yolov8n.pt')
        # IDs das classes no dataset COCO: 24 é mochila, 28 é mala
        self.classes_interesse = [24, 28]

    def detectar(self, frame):
        # Realiza a predição
        results = self.model(frame, classes=self.classes_interesse, conf=0.5, verbose=False)
        return results[0]
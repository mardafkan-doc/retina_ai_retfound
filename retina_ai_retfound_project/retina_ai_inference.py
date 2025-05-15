import torch
import numpy as np

def load_model(weights_path):
    model = torch.load(weights_path, map_location="cpu")
    model.eval()
    return model

def analyze_oct(image_path, model):
    # Здесь должна быть реальная обработка изображения и инференс
    return "Подозрение на DME"
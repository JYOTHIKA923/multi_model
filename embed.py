from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import numpy as np

# Load CLIP model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")


# IMAGE EMBEDDING (Correct = 512)
def get_embedding(image_path):
    image = Image.open(image_path).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        image_features = model.get_image_features(**inputs)

    embedding = image_features[0].cpu().numpy()

    return np.array(embedding).flatten()


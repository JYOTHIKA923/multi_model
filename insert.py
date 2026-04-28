import os
from db import add_product
from embed import get_embedding

IMAGE_FOLDER = "static/images"

for i, file in enumerate(os.listdir(IMAGE_FOLDER)):

    if file.lower().endswith((".jpg", ".jpeg", ".png")):

        path = os.path.join(IMAGE_FOLDER, file)

        embedding = get_embedding(path)

        print("Inserted:", file)
        print("Dimension:", len(embedding))



        add_product(i, embedding, path, file)

      

print("All images inserted successfully")
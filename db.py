

import chromadb
import numpy as np



# Fresh new database folder
client = chromadb.PersistentClient(path="./fresh_db_new")

# Fresh new collection
collection = client.get_or_create_collection(
    name="products_final_new"
)


# ---------------------------------
# Add Product
# ---------------------------------
def add_product(id, embedding, image_path, name):

    embedding = np.array(embedding, dtype=np.float32).flatten().tolist()

    collection.add(
        ids=[str(id)],
        embeddings=[embedding],
        metadatas=[{
            "name": name,
            "image_path": image_path
        }]
    )


# ---------------------------------
# Search Similar Products
# ---------------------------------
def search_similar(query_embedding, top_k=5):

    query_embedding = np.array(
        query_embedding,
        dtype=np.float32
    ).flatten().tolist()




    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results
from flask import Flask, render_template, request
import os
from embed import get_embedding
from db import search_similar, add_product, collection
from flask import jsonify


from db import search_similar

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    try:
        if request.method == "POST":
            query_embedding = None

            if "image" in request.files:
                file = request.files["image"]

                if file.filename != "":
                    path = os.path.join(UPLOAD_FOLDER, file.filename)
                    file.save(path)

                    query_embedding = get_embedding(path)
               

                    # Debug first
                    print(type(query_embedding))
                    print(len(query_embedding))
                    print(type(query_embedding[0]))
                 # SEARCH DB
            if query_embedding is not None:
                    

                    data = search_similar(query_embedding)
                    results = []
                    for i in range(len(data["metadatas"][0])):
                          item = data["metadatas"][0][i]

                          distance = data["distances"][0][i]

                          
                         # Convert distance to similarity %
                          similarity = max(0, round((1 - distance) * 100, 2))

                          item["similarity"] = similarity
 
                          results.append(item)
                    # Save Search History
                    with open("history.txt", "a") as f:
                       f.write("Image Search: " + file.filename + "\n")       
                          
                    

    except Exception as e:
        return f"Error: {str(e)}"
    # Read Search History
    history = []

    try:
     
     with open("history.txt", "r") as f:
        history = f.readlines()
    except:
     history = []

    return render_template(
    "index.html",
    results=results,
    history=history[::-1]
)

   


@app.route("/feedback", methods=["POST"])
def feedback():

    data = request.get_json()

    product = data.get("product")
    vote = data.get("vote")

    with open("feedback.txt", "a") as f:
        f.write(f"{product} : {vote}\n")

    return "Feedback Saved Successfully"

@app.route("/admin")
def admin():
    return render_template("admin.html")
@app.route("/add_product", methods=["POST"])
def add_new_product():
    try:
        file = request.files["image"]
        name = request.form["name"]

        if file.filename == "":
            return "No file selected"

        os.makedirs("static/images", exist_ok=True)

        path = os.path.join("static/images", file.filename)
        file.save(path)

        embedding = get_embedding(path)

        add_product(
            file.filename,
            embedding,
            path,
            name
        )

        return "Product Added Successfully"

    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/delete_product/<id>")
def delete_product(id):
    try:
        collection.delete(ids=[id])
        return "Deleted Successfully"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)









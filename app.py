import os
from mnist.configuration import Configuration
from flask import Flask, render_template, request, redirect

from inference import get_prediction
from commons import load_model

app = Flask(__name__)

config = Configuration()
model = load_model(config)


@app.route("/", methods=["GET", "POST"])
def upload_file():
    global model
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files.get("file")
        if not file:
            return
        img_bytes = file.read()
        class_id = get_prediction(model, image_bytes=img_bytes)
        return render_template("result.html", class_id=class_id)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))

from flask import render_template, redirect, request, url_for
from FlaskExercise import app, db
from FlaskExercise.forms import AnimalForm
import FlaskExercise.models as models

# Construct base image URL
IMAGE_SOURCE_URL = f"https://{app.config['BLOB_ACCOUNT']}.blob.core.windows.net/{app.config['BLOB_CONTAINER']}/"

@app.route("/")
@app.route("/home")
def home():
    animals = models.Animal.query.all()
    return render_template(
        "index.html",
        imageSource=IMAGE_SOURCE_URL,
        animals=animals
    )

@app.route("/animal/<int:id>", methods=["GET", "POST"])
def animal(id):
    animal_obj = models.Animal.query.get_or_404(id)
    form = AnimalForm(obj=animal_obj)

    if form.validate_on_submit():
        animal_obj.save_changes(request.files.get("image_path"))
        return redirect(url_for("home"))

    return render_template(
        "animal.html",
        imageSource=IMAGE_SOURCE_URL,
        form=form,
        animal=animal_obj
    )

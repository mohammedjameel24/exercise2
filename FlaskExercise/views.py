from flask import Blueprint, render_template, redirect, request, url_for, current_app
from FlaskExercise import db
import FlaskExercise.models as models
from FlaskExercise.forms import AnimalForm

bp = Blueprint("main", __name__)

def image_source_url():
    return (
        f"https://{current_app.config['BLOB_ACCOUNT']}.blob.core.windows.net/"
        f"{current_app.config['BLOB_CONTAINER']}/"
    )

@bp.route("/")
@bp.route("/home")
def home():
    animals = models.Animal.query.all()
    return render_template(
        "index.html",
        imageSource=image_source_url(),
        animals=animals
    )

@bp.route("/animal/<int:id>", methods=["GET", "POST"])
def animal(id):
    animal_obj = models.Animal.query.get_or_404(int(id))
    form = AnimalForm(obj=animal_obj)

    if form.validate_on_submit():
        animal_obj.save_changes(request.files.get("image_path"))
        return redirect(url_for("main.home"))

    return render_template(
        "animal.html",
        imageSource=image_source_url(),
        form=form,
        animal=animal_obj
    )

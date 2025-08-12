from flask import flash
from werkzeug.utils import secure_filename
from azure.storage.blob import BlobServiceClient
from FlaskExercise import app, db
import uuid
import os

# Azure configuration
BLOB_CONTAINER = app.config["BLOB_CONTAINER"]
STORAGE_URL = f"https://{app.config['BLOB_ACCOUNT']}.blob.core.windows.net/"
blob_service = BlobServiceClient(account_url=STORAGE_URL, credential=app.config["BLOB_STORAGE_KEY"])

class Animal(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75))
    scientific_name = db.Column(db.String(75))
    description = db.Column(db.String(800))
    image_path = db.Column(db.String(100))

    def __repr__(self):
        return f"<Animal {self.name}>"

    def save_changes(self, file):
        try:
            if file and file.filename:
                filename = secure_filename(file.filename)
                ext = filename.rsplit(".", 1)[-1]
                new_filename = f"{uuid.uuid4()}.{ext}"

                # Upload new blob
                blob_client = blob_service.get_blob_client(container=BLOB_CONTAINER, blob=new_filename)
                blob_client.upload_blob(file, overwrite=True)

                # Delete old blob if it exists
                if self.image_path:
                    old_blob = blob_service.get_blob_client(container=BLOB_CONTAINER, blob=self.image_path)
                    old_blob.delete_blob()

                self.image_path = new_filename

            db.session.add(self)
            db.session.commit()

        except Exception as err:
            db.session.rollback()
            flash(str(err))

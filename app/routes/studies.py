# app/routes/studies.py
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.database import mongo
from bson.objectid import ObjectId
from app.utils.study_parser import parse_nebula_dna_score
import logging

# Create a logger for this module
logger = logging.getLogger(__name__)

bp = Blueprint("studies", __name__, url_prefix="/studies")

@bp.route("/")
def list_subjects():
    # Find all subject IDs with studies
    subjects = mongo.db.studies.distinct("patient_id")
    return render_template("subjects.html", subjects=subjects)

# @bp.route("/<subject_id>")
# def list_studies(subject_id):
#     # Find all studies for a specific subject
#     studies = list(mongo.db.studies.find({"patient_id": subject_id}))
#     return render_template("studies.html", subject_id=subject_id, studies=studies)

@bp.route("/<subject_id>", methods=["GET", "POST"])
def list_studies(subject_id):
    # If this is a POST request, then parse the posted study and persist it.
    if request.method == "POST":
        study_url = request.form.get("study_url")
        study_content = request.form.get("study_content")

        if not study_content:
            return render_template("studies.html", subject_id=subject_id, error="Study content cannot be empty")

        if not study_url:
            return render_template("studies.html", subject_id=subject_id, error="Study URL cannot be empty")

        # Retrieve tags from the phenome_tags collection
        tags_cursor = mongo.db.phenome_tags.find({}, {"tag": 1, "_id": 0})
        known_tags = [doc["tag"] for doc in tags_cursor]

        logging.debug(f"Retrieved known_tags: {known_tags}")

        # Parse study data with known_tags
        try:
            study_info = parse_nebula_dna_score(subject_id, study_url, study_content, known_tags=known_tags)
            logging.debug(f"parse_nebula_dna_score returned study_info: {study_info}")
        except Exception as e:
            logging.exception("Error in parse_nebula_dna_score")
            studies = list(mongo.db.studies.find({"patient_id": subject_id}))
            return render_template("studies.html", subject_id=subject_id, studies=studies, error="Failed to parse study information")

        # # Check if record already exists in MongoDB
        if study_info is None:
            logging.error("parse_nebula_dna_score returned None")
            studies = list(mongo.db.studies.find({"patient_id": subject_id}))
            return render_template("studies.html", subject_id=subject_id, studies=studies, error="Failed to parse study information")

        # Check if a study with this patient_id and study_name already exists
        study_name = study_info.get("study").get("name")
        logging.debug(f"Study name: {study_name}")
        existing_record = mongo.db.studies.find_one({"patient_id": subject_id, "study.name": study_name})

        if existing_record:
            # Option 1: Update the existing record
            mongo.db.studies.update_one(
                {"patient_id": subject_id, "study.name": study_name},
                {"$set": study_info}
            )
            logging.info(f"Record successfully updated for {study_name}")
            # return render_template("studies.html", subject_id=subject_id, studies=studies)
            return redirect(url_for("studies.list_studies", subject_id=subject_id))

            # Option 2: Skip insertion if the record exists (Uncomment to use)
            # return render_template("studies.html", subject_id=subject_id, error="Record already exists")

        # Insert new record if not present
        study_info["patient_id"] = subject_id  # Ensure patient_id is included in the document
        mongo.db.studies.insert_one(study_info)
        logging.info("Record successfully added")

        # Redirect to refresh the list of studies
        return redirect(url_for("studies.list_studies", subject_id=subject_id))

    # If it's a GET request then simply fetch studies for the subject and render the studies page
    studies = list(mongo.db.studies.find({"patient_id": subject_id}))
    return render_template("studies.html", subject_id=subject_id, studies=studies)

@bp.route("/<subject_id>/<study_id>")
def get_study(subject_id, study_id):
    # Find a specific study by its ID
    # study = mongo.db.studies.find_one({"_id": mongo.ObjectId(study_id), "patient_id": subject_id})
    study = mongo.db.studies.find_one({"_id": ObjectId(study_id), "patient_id": subject_id})
    # study = mongo.db.studies.find_one({"patient_id": subject_id})
    if not study:
        return "Study not found", 404
    return render_template("study.html", study=study)

# @bp.route("/<patient_id>")
# def get_study(patient_id):
#     study = mongo.db.studies.find_one({"patient_id": patient_id})
#     if not study:
#         return "Study not found", 404
#     return render_template("study.html", study=study)


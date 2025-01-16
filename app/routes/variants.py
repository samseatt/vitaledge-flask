# app/routes/variants.py
from flask import Blueprint, render_template, request, redirect, url_for
from app.database import mongo
from bson.objectid import ObjectId

bp = Blueprint("variants", __name__, url_prefix="/variants")

@bp.route("/<subject_id>")
def variants_landing(subject_id):
    return render_template("variants.html", subject_id=subject_id)

@bp.route("/<subject_id>/search", methods=["POST"])
def search_variants(subject_id):
    search_type = request.form.get("search_type")
    if search_type == "rsid":
        rsID = request.form.get("rsID")
        variant = mongo.db.snps.find_one({"patient_id": subject_id, "rsID": rsID})
        if variant:
            return redirect(url_for("variants.get_variant_by_id", subject_id=subject_id, variant_id=variant["_id"]))
        return render_template("variants.html", subject_id=subject_id, error="Variant not found")
    elif search_type == "chromosome_range":
        chromosome = request.form.get("chromosome")
        start_position = int(request.form.get("start_position"))
        end_position = int(request.form.get("end_position"))
        if start_position >= end_position or (end_position - start_position) > 10000:
            return render_template("variants.html", subject_id=subject_id, error="Invalid position range")
        variants = list(mongo.db.snps.find({
            "patient_id": subject_id,
            "chromosome": chromosome,
            "position": {"$gte": start_position, "$lte": end_position}
        }))
        return render_template("variants.html", subject_id=subject_id, variants=variants)

@bp.route("/<subject_id>/<variant_id>")
def get_variant_by_id(subject_id, variant_id):
    variant = mongo.db.snps.find_one({"_id": ObjectId(variant_id), "patient_id": subject_id})
    if not variant:
        return "Variant not found", 404
    return render_template("variant.html", variant=variant)

@bp.route("/<subject_id>/rsid/<variant_name>")
def get_variant_by_name(subject_id, variant_name):
    variant = mongo.db.snps.find_one({"patient_id": subject_id, "rsID": variant_name})
    if not variant:
        return "Variant not found", 404
    return render_template("variant.html", variant=variant)

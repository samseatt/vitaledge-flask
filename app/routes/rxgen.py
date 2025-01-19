# app/routes/rxgen.py
from flask import Blueprint, render_template, request, jsonify
import requests

bp = Blueprint("rxgen", __name__, url_prefix="/rxgen")

RXGEN_API_BASE = "http://127.0.0.1:8000"  # Base URL for RxGen API

@bp.route("/", methods=["GET", "POST"])
def rxgen_home():
    if request.method == "POST":
        file_path = request.form.get("file_path")
        patient_id = request.form.get("patient_id")
        
        if not file_path or not patient_id:
            return render_template("rxgen.html", error="Both file path and patient ID are required.")

        # Call RxGen API to annotate
        try:
            response = requests.post(
                f"{RXGEN_API_BASE}/annotate",
                json={"file_path": file_path, "patient_id": patient_id},
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            result = response.json()
            return render_template("rxgen.html", result=result)
        except requests.RequestException as e:
            return render_template("rxgen.html", error=f"Failed to call RxGen API: {e}")

    return render_template("rxgen.html")

@bp.route("/variant/interaction", methods=["GET"])
def rxgen_variant_interaction():
    variant_id = request.args.get("variant_id")

    if not variant_id:
        return render_template("rxgen.html", error="Variant ID is required.")

    # Call RxGen API to get variant interaction
    try:
        response = requests.get(f"{RXGEN_API_BASE}/variant/interaction", params={"variant_id": variant_id})
        response.raise_for_status()
        result = response.json()
        return render_template("rxgen.html", interaction=result)
    except requests.RequestException as e:
        return render_template("rxgen.html", error=f"Failed to call RxGen API: {e}")

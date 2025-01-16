# app/main.py
from flask import Flask
from app.routes import studies, variants
from app.database import init_db
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Change to logging.INFO or logging.ERROR for less verbosity
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object("app.config.Config")

# Initialize MongoDB
init_db(app)

# Register Blueprints
app.register_blueprint(studies.bp)
app.register_blueprint(variants.bp)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def home():
    return "Welcome to the VitalEdge Flask UI"

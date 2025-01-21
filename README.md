# VitalEdge Flask

VitalEdge Flask is an internal web-based UI designed to interact with and manage data within the VitalEdge Beaker ecosystem. It enables visualization, control, and interaction with bioinformatics pipelines and genomic data, providing tools for researchers and administrators to streamline operations leading up to Datalake ingestion.

## Features

- **Beaker Data Management**: Directly visualize and manage data stored in Beaker (MongoDB).
- **Pipeline Interaction**: Enable, monitor, and manage bioinformatics pipelines.
- **Study and Variant Visualization**: Browse and edit genomic studies, their associated variants, and subject-specific data.
- **Data Loading Operations**: Facilitate the process of loading Beaker data into Datalake through controlled operations via BRIDGE.
- **User-Friendly Forms and Outputs**: Perform data manipulations and view JSON outputs in user-friendly formats with options to apply transformations.

## Project Structure

```plaintext
vitaledge_flask/
├── app/
│   ├── templates/               # HTML templates for rendering views
│   │   ├── study.html           # Template for displaying a single study
│   │   ├── studies.html         # Template for listing all studies
│   │   ├── subjects.html        # Template for listing subjects and initiating new studies
│   │   ├── variant.html         # Template for displaying a single variant
│   │   └── variants.html        # Template for displaying/searching variants
│   ├── static/                  # Static files (CSS, JS, images)
│   │   └── style.css            # Generic stylesheet for all templates
│   ├── routes/                  # Flask route definitions
│   │   ├── __init__.py          # Route initializer
│   │   ├── studies.py           # Routes for study-related views
│   │   ├── subjects.py          # Routes for subject-related views
│   │   └── variants.py          # Routes for variant-related views
│   ├── services/                # Business logic and pipeline handling
│   │   └── studies_service.py   # Service for handling studies
│   ├── utils/                   # Utility functions
│   │   └── serializers.py       # Serializers for MongoDB data
│   ├── config.py                # Application configuration
│   ├── database.py              # MongoDB connection setup
│   ├── main.py                  # Main entry point for the Flask app
│   └── forms.py                 # Forms for user data entry
├── requirements.in              # Base dependencies
├── requirements.txt             # Compiled dependencies
└── README.md                    # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.8+
- MongoDB

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_org/vitaledge_flask.git
   cd vitaledge_flask
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables in a `.env` file:
   ```env
   FLASK_ENV=development
   MONGODB_URI=mongodb://localhost:27017/beaker_db
   ```

5. Run the Flask app:
   ```bash
   flask run
   ```

6. Access the application at `http://127.0.0.1:5000`.

## Usage

- Use the **Subjects** page to view and manage subjects and their studies.
- Use the **Studies** page to browse, add, and edit genomic studies.
- Use the **Variants** page to search for and explore variants linked to studies.

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch.
4. Open a pull request describing your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please reach out to the development team at [team@vitaledge.org](mailto:team@vitaledge.org).

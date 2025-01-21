##############################################################
## To start project
cd /Users/samseatt/projects/vitaledge/vitaledge-flask
conda activate vitaledge-flask
pip install pip-tools
pip install -r requirements.txt
##
#### Starting server
Export the FLASK_APP environment variable, and run Flask with the desired port:
export FLASK_APP=app.main
flask run --host=0.0.0.0 --port=5001

docker-compose up --build
docker-compose down


#### Endpoints
#
##############################################################

## Creating conda environment:
#conda create -n vitaledge-flask python=3.11
conda activate vitaledge-flask
conda deactivate

##############
ipconfig getifaddr en0
192.168.1.83


python
>>> import psycopg2
>>> conn = psycopg2.connect(
...     dbname="vitaledge_datalake",
...     user="your_username",
...     password="your_password",
...     host="localhost",
...     port="5432"
... )
>>> conn.close()


cp .env.example .env

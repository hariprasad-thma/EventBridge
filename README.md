# EventBridge

# Create virtual environment
python -m venv path\virutalEnv

e.g. python -m venv .venv

# Once virtual enviroment is created, we can install libraries inside the virtual environment.

python -m pip install -r requirements.txt

# Set the environmental variable and authroization keys

export AWS_DEFAULT_REGION=eu-central-1   : region you are using

export IS_LOCAL=True  : if running on your local 

export STAGE=sandbox  : Stage name. All these are considered as 'environment variables'.

Copy paste your credentials to deploy 

# run your application 
python filename.py
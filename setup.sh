#!/bin/sh
python -m venv env
source env/Scripts/activate #If running in unix based OS use: 'source env/bin/activate' instead
pip install -r requirements.txt
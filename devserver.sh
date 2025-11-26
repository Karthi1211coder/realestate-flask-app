#!/bin/sh
source .venv/bin/activate
# Use port 8080 if $PORT is not set, otherwise use the $PORT value
python -u -m flask --app main run -p ${PORT:-8080} --debug

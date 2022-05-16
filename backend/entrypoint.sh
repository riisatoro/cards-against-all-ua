#!/bin/bash

echo "Dependencies install"
poetry install

echo "Server start up"
poetry run uvicorn main:app --host 0.0.0.0 --port $PORT

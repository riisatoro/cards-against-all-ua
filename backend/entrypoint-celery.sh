#!/bin/bash

echo "Worker startup"
poetry run celery -A core worker -E
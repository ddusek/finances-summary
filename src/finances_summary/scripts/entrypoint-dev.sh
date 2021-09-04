#!/usr/bin/env bash

echo -e "Running webserver"

uvicorn finances_summary.user_data.api:app --host 0.0.0.0 --port 8000 --reload
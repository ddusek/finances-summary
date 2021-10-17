#!/usr/bin/env bash

echo -e "Init database"
python /finances_summary/_sync/init_db.py

echo -e "Running webserver"
python /finances_summary/app.py

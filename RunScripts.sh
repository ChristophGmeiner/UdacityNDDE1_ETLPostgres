#!/bin/bash

#py script for dropping/creating db and tables
#WATCH OUT: DROPPING takes placs
python create_tables.py
python etl.py
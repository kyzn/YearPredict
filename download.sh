#!/bin/bash
# Bash script to download Million Song Dataset
#       year prediction subset

# Use the following command to run:
# . download.sh

wget http://archive.ics.uci.edu/ml/machine-learning-databases/00203/YearPredictionMSD.txt.zip
unzip YearPredictionMSD.txt.zip
rm YearPredictionMSD.txt.zip
exit
#!/bin/bash
python cleanInput.py

loc='/home/tbrownex/data/iot/'
fileName='clean.csv'
fullPath=$loc$fileName
gzip -f $fullPath
echo  -e "\nOutput written to $fullPath.gz"

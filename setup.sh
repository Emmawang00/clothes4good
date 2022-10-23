#!/usr/bin/env bash
source /home/codespace/venv/bin/activate
#append it to bash so every shell launches with it 
echo 'source /home/codespace/venv/bin/activate' >> ~/.bashrc
sudo apt-get update
sudo apt-get install tesseract-ocr

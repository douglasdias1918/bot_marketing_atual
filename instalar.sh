#!/data/data/com.termux/files/usr/bin/bash
pkg update -y && pkg upgrade -y
pkg install -y python clang rust make cmake libjpeg-turbo
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
python main.py

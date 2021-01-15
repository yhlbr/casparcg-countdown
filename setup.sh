#!/bin/bash

echo "Install Font"
sudo cp alarm_clock.ttf /usr/share/fonts/

echo "Install Requirements"
/usr/bin/python3 -m pip install -r requirements.txt
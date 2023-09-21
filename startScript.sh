#!/bin/bash
# Started from /etc/xdg/LXDE-pi/autostart
echo "Starting timelapse program in 10 seconds."
sleep 10
lxterminal --working-directory='[where youre code is saved]' --command='python3 timelapseImageFinal.py'

#!/bin/bash
# Started from /etc/xdg/LXDE-pi/autostart
echo "Starting timelapse program in 10 seconds."
sleep 10
lxterminal --working-directory='/home/timelapse1/timelapse' --command='python3 timelapseImageFinal.py'

# Timelapse_rPi
timelapse code for Raspberry pi 

steps necessary for timelapse script to work on reboot/start

Change permissions for startScript.sh:
  In terminal: "chmod 755 [startScript path]"

Edit the Autostart file:
  In terminal: "sudo nano /etc/xdg/lxsession/LXDE-pi/autostart"
  add line "@lxterminal -e /home/pi/StartScript.sh"
    then press: CTRL + X, Y, Enter

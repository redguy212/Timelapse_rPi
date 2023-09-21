# Timelapse_rPi_Setup
Setup instructions code for Raspberry pi 

You need to choose the timelapse parameters.

open timelapseImageFinal.py in an editor and set:

    timeMinutes = [a] #set this to the number of minutes you wish to run your timelapse camera
    
    secondsInterval = [b] #number of seconds delay between each photo taken
  
May also be necessary to change permissions of the Pictures folder, to make deleting.moving easier:

  In terminal: 
  
    chmod 777 /home/[yourPiName]/Pictures

You will need to add extra GPU memory if you intend to use a high resolution camera

It may also be necessary to enable legacy camera mode.

In terminal: 
  
    sudo raspi-config

This will bring you to the config window.

in '3 Interface Options' you will find the legacy camera setting,

In '4 Performance Options' you will find the GPU memory setting,

For GPU memory, doubling it from 128 to 256 is usually enough.
    
**----------------------------------------------------------------------------------------**

**Steps necessary for timelapse script to work on reboot/start**

**----------------------------------------------------------------------------------------**

Open startScript.sh

edit line 5 and change working directory from blank default to where your timelapse code is.

  EXAMPLE:
  
  from
  
    lxterminal --working-directory='[where youre code is saved]' --command='python3 timelapseImageFinal.py'
  
  to
  
    lxterminal --working-directory='/home/timelapse1/timelapse' --command='python3 timelapseImageFinal.py'


Change permissions for startScript.sh:

  In terminal: 
  
    chmod 755 [startScript path]
  

Edit the Autostart file:

  In terminal: 
  
    sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
  
  add line:
  
    @lxterminal -e /home/pi/StartScript.sh
  
  then press: CTRL + X, Y, Enter

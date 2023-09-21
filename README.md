# Timelapse_rPi_Setup
Setup instructions code for Raspberry pi 

You need to choose the timelapse parameters.

open timelapseImageFinal.py in an editor and set:

    timeMinutes = [a] #set this to the number of minutes you wish to run your timelapse camera
    
    secondsInterval = [b] #number of seconds delay between each photo taken
  

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

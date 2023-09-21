from picamera import PiCamera
import os
from os import system
import datetime
from time import sleep


#######################################################################
#  TIMELAPSE PARAMETERS
        
timeMinutes = 360 #set this to the number of minutes you wish to run your timelapse camera
secondsInterval = 2 #number of seconds delay between each photo taken
#fps = 30 #frames per second timelapse video
numPhotos = int((timeMinutes*60)/secondsInterval) #number of photos to take

#######################################################################

runProgram = input("Run timelapse program? (Y/N): ")

if runProgram.lower() == "n":
        print("No selected, Program terminating...")
        sleep(2)
        quit

elif runProgram.lower() =="y":
        #print ("test running sucessful") 
        
        print("10 second delay for reading - terminate anytime with [ CTRL + C ]")
        print("")
        print("--------------------------------")
        print("Welcome to the Timelapse code")
        print("--------------------------------")
        print("")
        print("Remember to set timelapse parameters in the file")
        print("")
        print("AFTER the camera preview begins, press ENTER to end preview and continue the script")
        sleep(10)

        camera = PiCamera()
        camera.start_preview()

        #empty true statements
        y = 1;
        z = 0 
        negative = "-"
        while True:
                x = input("Press ENTER to continue")
	
                if x == "":
                        x = 0.5
                        break
                else: 
                        x = 0.5
                        break

        sleep(x)

        camera.stop_preview()
        camera.close()
        
        
        #time to cancel the command before it generates files
        print("")
        print("Timelapse script is starting... [ Ctrl + C = Terminate at any time]")
        sleep(10)

        print("")
        print("number of photos to take = ", numPhotos)
        print("")
        
        dateRaw= datetime.datetime.now()
        startDateTimeFormat = dateRaw.strftime("%Y-%m-%d_%H:%M:%S")
        
        os.mkdir('/home/timelapse1/Pictures/' + startDateTimeFormat)
        print("The Pi has now started taking photos for your timelapse, start time: " + startDateTimeFormat)
        
        camera = PiCamera()
        camera.resolution = (3000, 2000)
        
        for i in range(numPhotos):
            camera.capture('/home/timelapse1/Pictures/' + startDateTimeFormat +'/{0:06d}.jpg'.format(i))
            sleep(secondsInterval)
        
        dateRaw= datetime.datetime.now()
        endDateTimeFormat = dateRaw.strftime("%Y-%m-%d_%H:%M")
        print("Photos finished on " + endDateTimeFormat + ". Files located at /home/timelapse1/Pictures/" + startDateTimeFormat)
        
        camera.close()
        
        #print("Please standby as your timelapse video is created.")
        
        #system('ffmpeg -r {} -f image2 -pattern_type glob -i "/home/timelapse1/Pictures/*.jpg" -vcodec mpeg4 -b:v 800k /home/timelapse1/Videos/{}.avi'.format(fps, datetimeformat))
        #system('rm /home/timelapse1/Pictures/*.jpg')
        #print('Timelapse video is complete. Video saved as /home/timelapse1/Videos/{}.avi'.format(datetimeformat))
        
        #print('Timelapse photo taking is complete. Saved to /home/timelapse1/photos/{}.jpg'.format(datetimeformat))

else:
        print("Unknown input, please try again")
        quit

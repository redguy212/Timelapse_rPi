from picamera import PiCamera
import os
from os import system
import datetime
from time import sleep

timeMinutes = 2 #set this to the number of minutes you wish to run your timelapse camera
secondsInterval = 1 #number of seconds delay between each photo taken
#fps = 30 #frames per second timelapse video
numPhotos = int((timeMinutes*60)/secondsInterval) #number of photos to take
print("number of photos to take = ", numPhotos)

dateRaw= datetime.datetime.now()
startDateTimeFormat = dateRaw.strftime("%Y-%m-%d_%H:%M:%S")

os.mkdir('/home/timelapse1/Pictures/' + startDateTimeFormat)
print("The Pi has now started taking photos for your timelapse, start time: " + startDateTimeFormat)

camera = PiCamera()
camera.resolution = (4000, 3000)

for i in range(numPhotos):
    camera.capture('/home/timelapse1/Pictures/' + startDateTimeFormat +'/{0:06d}.jpg'.format(i))
    sleep(secondsInterval)

dateRaw= datetime.datetime.now()
endDateTimeFormat = dateRaw.strftime("%Y-%m-%d_%H:%M")
print("Photos finished on " + endDateTimeFormat + ". Files located at /home/timelapse1/Pictures/" + startDateTimeFormat)


#print("Please standby as your timelapse video is created.")

#system('ffmpeg -r {} -f image2 -pattern_type glob -i "/home/timelapse1/Pictures/*.jpg" -vcodec mpeg4 -b:v 800k /home/timelapse1/Videos/{}.avi'.format(fps, datetimeformat))
#system('rm /home/timelapse1/Pictures/*.jpg')
#print('Timelapse video is complete. Video saved as /home/timelapse1/Videos/{}.avi'.format(datetimeformat))

#print('Timelapse photo taking is complete. Saved to /home/timelapse1/photos/{}.jpg'.format(datetimeformat))








#In order for this to work properly your screen resolution must be set at 1280x720.
#The scale and layout set to 100%
#Have only two tabs open. The first tab "https://www.youtube.com/playlist?list=WL" and the second "https://mp4s.org/en1/youtube-to-mp4/" 
#If you attempt to use another mp4 site the program will not work.
#Close all other applications and save any unsaved data. 
#I would recommend setting the 'time.sleep(1)' to 'time.sleep(10)' if this is your first time running this program. 
#That way you will have ten seconds before the next action takes place. Just in case the program malfunctions
#I run this program with IDLE (Python 3.9 64-bit) the place where IDLE pops up is random so I usually move it 

from pynput.mouse import Button, Controller
from datetime import datetime
import time
dateTimeObj = datetime.now()
mouse = Controller()
#Max length video 2hours 13mins 10/8/20
def youtube():
    mouse.position = (1120, 255)  #Move to Video
    mouse.click(Button.right, 1) #Right click
    time.sleep(1)
    mouse.position =(1080, 411)  # Move to 'copy link'
    mouse.click(Button.left, 1) #click
    time.sleep(1)
    mouse.position = (329, 17) #Move to converter tab
    mouse.click(Button.left, 1) #click
    time.sleep(1)
    mouse.position = (466, 424) #Move to enter URL
    mouse.click(Button.left, 1) #click
    time.sleep(1)
    mouse.click(Button.right, 1) #Right click
    mouse.position = (490, 440) #Move to paste
    time.sleep(1)
    mouse.click(Button.left, 1) #click
    mouse.position = (855, 415) #Move to converter
    time.sleep(1)
    mouse.click(Button.left, 1) #click
    mouse.position = (559, 426) #move to download button and wait
    time.sleep(20)
    mouse.click(Button.left, 1) #click
    time.sleep(1)
    mouse.position =(707, 15) #Move to close Spam tab
    mouse.click(Button.left, 1) #click
    time.sleep(7)
    mouse.position = (673, 417) #Move to convert next
    mouse.click(Button.left, 1) #click
    time.sleep(1)
    mouse.position = (121, 15) #Move to Youtube tab
    mouse.click(Button.left, 1) #click
    time.sleep(1)
    mouse.position = (1219, 217) #Move to options button
    mouse.click(Button.left, 1) #click
    time.sleep(1)
    mouse.position = (1070, 420) #Move to Remove from playlist button
    mouse.click(Button.left, 1) #click
    time.sleep(1)
for i in range (200, 0, -1):  #Change the variable '200' to the amount of videos in the playlist.
    youtube()
    time.sleep(45) #Change the 45 to 180 if the video is longer than 5 minutes. 360 if it is an hour or longer
print(dateTimeObj)

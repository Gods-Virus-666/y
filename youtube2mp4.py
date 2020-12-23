#from pynput.mouse import Button, Controller
#from pynput.keyboard import Key, Controller
#mouse = Controller()
#keyboard = Controller()
#mouse.position = (123,704) #move to browser
#mouse.click(Button.right, 1) #right click
#mouse.position = (75, 500) #move to open new window
#mouse.click(Button.left, 1) #clicks to open
#keyboard.type("https://www.youtube.com/")
#mouse.position=(40,100)
#mouse.click(Button.left,1)
#mouse.position=(100,425)
#mouse.click(Button.left,1)

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
    mouse.position = (1103, 386) #Move to Remmove from playlist button
    mouse.click(Button.left, 1) #click
    time.sleep(1)
for i in range (200, 0, -1): #Change the variable '200' to the amount of videos in the playlist.
    youtube()
    time.sleep(180)
print(dateTimeObj)

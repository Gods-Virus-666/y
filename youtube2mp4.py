from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
mouse = Controller()
keyboard = Controller()
mouse.position = (123,704) #move to browser
mouse.click(Button.right, 1) #right click
mouse.position = (75, 500) #move to open new window
mouse.click(Button.left, 1) #clicks to open
keyboard.type("https://www.youtube.com/")
mouse.position=(40,100)
mouse.click(Button.left,1)
mouse.position=(100,425)
mouse.click(Button.left,1)

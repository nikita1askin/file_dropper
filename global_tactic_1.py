import pyautogui as pag
import time, os, sys, cv2, datetime
''' Before running this script open the browser and tile it left,
 on the right side open Finder with opened tactic derictory.
    
Hot to start script -> $ python3 global_tactic_1.py 
'''

print("Start script {}".format(datetime.datetime.now()))

def present(file_name, region):
    """Looking for specific img"""
    while(True):
        if pag.locateCenterOnScreen("img/{}.png".format(file_name), grayscale=True, region=region, confidence=0.85): return True
        time.sleep(0.1)

def run():
    while(True):
        if present('upload', (100, 100, 350, 350)) and present('file', (1400, 100, 1600, 200)): move_file()
        time.sleep(1.5) #Pause between each file

def finder():
  '''Click on Finder window'''
  pag.click(1569, 158)

def move_file():
    '''Moving and uploading files'''
    # Click on Upload button (358, 277)
    pag.click(333, 277, clicks=2, interval=0.25)
    # Location of a file which we uploading 1569, 158
    time.sleep(1) #Waiting until form loads, better to change to chacking if form opened
    finder()
    # Location of drag and drop file window 673, 400
    pag.dragTo(673, 400, 0.2, button='left')
    # Location of Uploda button 1019, 699
    pag.click(1035, 615, clicks=2, interval=0.25)
    # Click on Finder window
    finder()
    # Location of folder athena_results 1552, 158
    pag.dragTo(1569, 119, 0.2, button='left')

run()

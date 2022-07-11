import pyautogui as pag
import time, os, sys, cv2, datetime
''' Before running this script open the browser and tile it left,
 on the right side open Finder.
  Upload first file, to set region in uploading window.
  To upload 100 files: 
    [ python3 100 ]
    
'''
# python3 global_tactic_1.py 100
# 100 files
number_of_files = int(sys.argv[1])

# Delay 5s for time to open (Ctrl + Tab) browser and filnder windows
time.sleep(5)

def uploaded():
    """Looking for upload button"""
    while(True):
        if pag.locateCenterOnScreen('img/upload.png', grayscale=True, region=(0, 0, 500, 500)): return True
        time.sleep(0.2)

def run(number):
    for i in range(number):
        if uploaded(): move_file()
        time.sleep(5)

def finder():
  '''Click on Finder window'''
  pag.click(1569, 158)

def move_file():
    '''Moving and uploading files'''
    # Click on Upload button (358, 277)
    pag.click(333, 277, clicks=2, interval=0.25)
    # Location of a file which we uploading 1569, 158
    time.sleep(1)
    finder()
    # Location of upoad window 673, 400
    pag.dragTo(673, 400, 0.2, button='left')
    # Location of Uploda button 1019, 699
    pag.click(1035, 615, clicks=2, interval=0.25)
    # Click on Finder window
    finder()
    # Location of folder athena_results 1552, 158
    pag.dragTo(1569, 119, 0.2, button='left')

run(number_of_files)

# file dropper

## GUI automation for GTT tickets

## Required libraries

* PyAUTOGUI (for GUI automation)
* DateTime
* OS
* cv2 (for image recognition)

If you want to use this script, you should set up 7 things. 5 points on your screen and a screenshot of an upload button and files in folders for spesific tactic.

## Points on screen whitch should be set up:
1. Position of the first file in finder (as List view)
2. Position of upload button
3. Drag and drop area where file should be put in
4. Save button in drag and drop window
5. Position of a folder in which file should be putten after upload.

## Screenshot:
Make a screenshot of the upload button and file img. Put files in /img folder near script.

## How to use this script:
Open windows side by side (On the left Browser, on right finder (as Lis view))
Run $ python3 global_tactic_1.py 

## Known issues

## Please wait window steis on screen more than 20 sec.
1. Click on Finder window and press Command + Z
2. Close Please wait window

## Form rendered after file already moved
1. Click on Finder window and press Command + Z
2. Close Form window

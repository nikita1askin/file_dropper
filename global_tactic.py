import pyautogui as pag
import time
import datetime

# Constants for pixel coordinates
UPLOAD_BUTTON = (333, 277)
FINDER_WINDOW = (1569, 158)
DRAG_DROP_WINDOW = (673, 400)
UPLOAD_BUTTON_FINAL = (1035, 615)
FOLDER_ATHENA_RESULTS = (1569, 119)

print("Start script {}".format(datetime.datetime.now()))


def present(file_name, region):
    """Looking for specific img"""
    while True:
        image_location = pag.locateCenterOnScreen("img/{}.png".format(file_name), grayscale=True, region=region, confidence=0.85)
        if image_location:
            return True
        time.sleep(0.1)


def click_location(location, clicks=1, interval=0.25):
    pag.click(location[0], location[1], clicks=clicks, interval=interval)


def move_file():
    '''Moving and uploading files'''
    click_location(UPLOAD_BUTTON, clicks=2)
    time.sleep(1)  # Waiting until form loads, better to change to checking if form opened
    click_location(FINDER_WINDOW)
    pag.dragTo(DRAG_DROP_WINDOW[0], DRAG_DROP_WINDOW[1], 0.2, button='left')
    click_location(UPLOAD_BUTTON_FINAL, clicks=2)
    click_location(FINDER_WINDOW)
    pag.dragTo(FOLDER_ATHENA_RESULTS[0], FOLDER_ATHENA_RESULTS[1], 0.2, button='left')
    print("File uploaded at: {}".format(datetime.datetime.now()))

def run():
    while True:
        if present('upload', (100, 100, 350, 350)) and present('file', (1400, 100, 1600, 200)):
            move_file()
        time.sleep(1.5)  # Pause between each file


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print('\nCtrl+C pressed. Exiting...')

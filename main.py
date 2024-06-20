import mss
import pyautogui
import pytesseract

import cv2 as cv
import numpy as np
import time

import ollama

def update_screen(recording_window):

    print("PIL Screen Capture Speed Test")
    print(f"Screen Resolution: f{recording_window}")
    #{'top': 187, 'left': 562, 'width': 660, 'height': 457}

    t0 = time.time()
    n_frames = 1

    with mss.mss() as sct:
        while True:
            screenshot = sct.grab(recording_window)
            screenshot_np = np.array(screenshot)

            small = cv.resize(screenshot_np, (0, 0), fx=0.5, fy=0.5)
            cv.imshow("Computer Vision", small)

            key = cv.waitKey(1)

            if key == ord('o'):
                text = pytesseract.image_to_string(screenshot_np)
                response = ollama.generate(model='llama3',
                                           prompt=f'The following text is written with french erros, please fix it: {text}')
                print(f"Text: {text}\n")
                print(response['response'])
            if key == ord('q'):
                break

            elapsed_time = time.time() - t0
            avg_fps = (n_frames / elapsed_time)
            #print(f"Average FPS: {str(avg_fps)}")
            n_frames += 1


def create_recording_window():
    recording_window = {"top": 0, "left": 0, "width": 0, "height": 0}
    is_creating = True

    while is_creating:
        print("Recording Window - MENU:")
        print("t: \ttop and left positions")
        print("w: \twidth and height positions")
        print("q: \texit menu")

        key = input()

        if key == "t":
            recording_window["top"] = pyautogui.position().y
            recording_window["left"] = pyautogui.position().x
            print(f"recording_window:{recording_window}")
        if key == "w":
            if recording_window["top"] == 0 and recording_window["left"] == 0:
                recording_window["width"] = pyautogui.position().x
                recording_window["height"] = pyautogui.position().y

            recording_window["width"] = pyautogui.position().x - recording_window["left"]
            recording_window["height"] = pyautogui.position().y - recording_window["top"]
            print(f"recording_window:{recording_window}")
        if key == "q":
            break

    return recording_window

if __name__ == "__main__":
    recording_window = create_recording_window()
    update_screen(recording_window)
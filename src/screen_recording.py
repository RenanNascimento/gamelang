import os
import time
import mss
import numpy as np
import cv2 as cv
import pytesseract
import ollama

from elevenlabs.client import ElevenLabs
from elevenlabs import play
from dotenv import load_dotenv

client = ElevenLabs(
  api_key=os.getenv("ELEVEN_LABS_API_KEY")
)

load_dotenv()
def update_screen(recording_window):

    print("PIL Screen Capture Speed Test")
    print(f"Screen Resolution: {recording_window}")

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
                                           prompt=f'This text \'{text}\' is written with french erros, please fix it and provide only the correct text and it\'s translation to brasilian portuguese without any additional information')
                print(f"Text OCR >>>>>: {text}\n")
                print(f"Response llama >>>>: {response['response']}")

                audio = client.generate(
                    text=response['response'],
                    model="eleven_multilingual_v2"
                )
                play(audio)
            if key == ord('q'):
                break

            elapsed_time = time.time() - t0
            #print(f"Average FPS: {str(avg_fps)}")
            n_frames += 1

import pyautogui

class RecordingWindow:

    def __init__(self, top, left, width, height):
        self.top = top
        self.left = left
        self.width = width
        self.height = height

    @classmethod
    def create_recording_window(cls):
        top = 0
        left = 0
        width = 0
        height = 0
        is_creating = True

        while is_creating:
            print("Recording Window - MENU:")
            print("t: \tTop and Left positions")
            print("w: \tWidth and Height positions")
            print("q: \tExit menu")

            key = input()

            if key == "t":
                top = pyautogui.position().y
                left = pyautogui.position().x
            elif key == "w":
                width = pyautogui.position().x - left
                height = pyautogui.position().y - top
            elif key == "q":
                break

        return cls(top, left, width, height)

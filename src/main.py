from recording_window import RecordingWindow
from screen_recording import update_screen

if __name__ == "__main__":
    recording_window = RecordingWindow.create_recording_window()
    update_screen(recording_window.__dict__)
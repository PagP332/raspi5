from picamera2 import Picamera2
import io
import time

def capture():
    picam2 = Picamera2()
    picam2.start()
    time.sleep(1)
    data = io.BytesIO()
    picam2.capture_file(data, format='jpeg')
    return data

if __name__ == '__main__':
    capture()
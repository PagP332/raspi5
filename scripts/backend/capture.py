import time

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

def capture():
    # Initialize Picamera2
    picam2 = Picamera2()

    # Configure for still image capture
    config = picam2.create_still_configuration()

    # Apply the configuration
    picam2.configure(config)

    # Start the camera
    picam2.start()

    # Wait briefly to ensure the camera is ready
    time.sleep(2)

    # Capture and save the image
    picam2.capture_file("template.jpeg")

    # Stop the camera
    picam2.stop()

if __name__ == '__main__':
    capture()
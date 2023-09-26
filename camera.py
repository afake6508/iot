import time
import picamera
camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
time.sleep(2)
image_path = '/home/pi/Desktop/visitor/images{}.jpg'.format(time.strftime('%Y%m%d%H%M%S'))
camera.capture(image_path)
camera.stop_preview()

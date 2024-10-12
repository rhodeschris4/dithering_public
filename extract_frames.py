import cv2
from pixelate_video import pixelate_image

def extract(video_name):
    video_name_DEBUG = "./videos/red_eye_video_c.mp4" # or any other extension like .avi etc
    vidcap = cv2.VideoCapture(video_name)
    success,image = vidcap.read()
    count = 0
    while success:
      cv2.imwrite("./frames/lib_frame%d.jpg" % count, image)     # save frame as JPEG file
      success,image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1

    pixelate_image()

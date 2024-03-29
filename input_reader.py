import numpy as np
from PIL import ImageGrab
import cv2
import time


#https://stackoverflow.com/questions/35097837/capture-video-data-from-screen-in-python
def screen_record(): 
    last_time = time.time()
    while(True):
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,1980,1080)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    screen_record() 
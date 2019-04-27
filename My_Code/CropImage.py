import cv2
import matplotlib.pyplot as plt
import numpy as np
import os,sys

from matplotlib import cm

class easy_label():
    def __init__(self,img_path,num_color = 10):
        self.img = cv2.imread(img_path)
        self.img_o = cv2.imread(img_path)
        self.img_t = cv2.imread(img_path)
        create_c = np.array(cm.tab10(num_color))[:3]*255
        self.color_list = [np.array(cm.tab10(color_num))[:3]*255 for color_num in range(num_color)]
        self.x1,self.x2,self.y1,self.y2 = 0,0,0,0
        self.drawing = False

    def mouse_callback(self,event, x, y, flags, param):
        ''' Drawing rectangle on the image
        '''
        if event == cv2.EVENT_LBUTTONDOWN:
            self.x1,self.y1 = x,y
            print("first point : ",self.x1,self.y1)
            cv2.circle(self.img,(self.x1,self.y1),1, (255,0,0), -1)
            self.drawing = True
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing == True:
                print("moving")
                self.x2,self.y2 = x,y 
                self.img = self.img_t.copy()
                cv2.circle(self.img,(self.x1,self.y1),1, (255,0,0), -1)
                cv2.rectangle(self.img,(self.x1,self.y1),(self.x2,self.y2),(255,0,0), 3)
        elif event == cv2.EVENT_LBUTTONUP:
            print("end point : ",x,y)
            self.x2,self.y2 = x,y 
            cv2.rectangle(self.img,(self.x1,self.y1),(self.x2,self.y2),(255,0,0), 3)
            self.drawing = False
            self.img_t = self.img

    def display_img(self):
        ''' Display image 
        '''
        cv2.namedWindow('Image')
        #param = [color_list[0],img.copy()]
        cv2.setMouseCallback('Image',self.mouse_callback)
        while True:
            # Display the image 
            cv2.imshow('Image',self.img)
            # Cloase all windows if press ESC
            k = cv2.waitKey(1) 
            if k == 27 or k == ord('q'):
                cv2.destroyAllWindows()
                break
            elif k == ord('c'):
                print("get new img")
                self.img = self.img_o.copy()
            elif k == ord('t'):
                cv2.circle(self.img,(150,150), 5, (0,0,0), -1)

        #    elif k > 0 and chr(k).isdigit():
        #        print(k)
        #        current_marker  = int(chr(k))
        #        param = [color_list[current_marker],img_c.copy()]
        #        cv2.setMouseCallback('Image', mouse_callback,param)

if __name__ == '__main__':
    img_path = '/Users/WillyChen/Learning/Learning_OPENCV/Test_Photo/cat.jpg'
    start = easy_label(img_path)
    start.display_img()
    

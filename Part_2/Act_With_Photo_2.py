import cv2
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

# cv2的event 都會回傳以下的資訊回來
# event -> 動作
# x,y -> 當下使用者點的位置
# flag -> 是否觸發事件
# param -> 可以將其他數值傳進去fun裡面
# 畫圈圈的function
def move_circle(event,x,y,flag,param):
    global first_pts,click_check
  
    if event == cv2.EVENT_LBUTTONDOWN:
        first_pts = (x,y)
        click_check = True
    elif event == cv2.EVENT_MOUSEMOVE:
        second_pts = (x,y)
        if click_check:
            cv2.circle(img_c,first_pts,calc_distance(first_pts,second_pts),(255,0,0),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        second_pts = (x,y)
        click_check = False
        cv2.circle(img_c,first_pts,calc_distance(first_pts,second_pts),(255,0,0),-1)

def calc_distance(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return round(sqrt((x1-x2)**2 + (y1-y2)**2))

# 定義一些Global Variable
first_pts = (0,0)
click_check = False
    
# 先透過cv2.imread的方式將照片讀進來
img = cv2.imread("../Test_Photo/cat.jpg")
img_c = img.copy()

# 如果要串接cv2的event的話, 我們需要先定義視窗的名稱
cv2.namedWindow("TEST")
# 再透過setMouseCallback來將視窗與我們定義的function 串再一起
cv2.setMouseCallback("TEST",move_circle)

while True:
    
    # 透過cv2.imshow 的方式顯示照片, 因為這邊是使用cv2.imshow的方式
    # 所以不需要特別改變RGB的順序, 像我們當時在使用matplotlib需要改順序
    cv2.imshow('TEST',img_c)
    
    # 透過q來結束程式, c來還原照片
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('c'):
        img_c = img.copy()

cv2.destroyAllWindows()


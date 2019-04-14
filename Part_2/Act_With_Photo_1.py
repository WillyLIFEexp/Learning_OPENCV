import cv2
import matplotlib.pyplot as plt
import numpy as np

# cv2的event 都會回傳以下的資訊回來
# event -> 動作
# x,y -> 當下使用者點的位置
# flag -> 是否觸發事件
# param -> 可以將其他數值傳進去fun裡面
# 畫圈圈的function
def draw_circle(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img_c,(x,y),10,(255,0,0),-1)
    
# 先透過cv2.imread的方式將照片讀進來
img = cv2.imread("../Test_Photo/cat.jpg")
img_c = img.copy()

# 如果要串接cv2的event的話, 我們需要先定義視窗的名稱
cv2.namedWindow("TEST")
# 再透過setMouseCallback來將視窗與我們定義的function 串再一起
cv2.setMouseCallback("TEST",draw_circle)

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


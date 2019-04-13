import cv2,os
import matplotlib.pyplot as plt
import numpy as np

# 先透過imread的方式將照片讀進來
img = cv2.imread("../Test_Photo/cat.jpg")
print(type(img)) # numpy array

# 透過While 一直將照片顯示出來直到結束
while True:
    # 將照片顯示出來
    cv2.imshow('cat',img)
    
    # 當使用者點擊Q時可將會結束回圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 將所有視窗關閉
cv2.destroyAllWindows()

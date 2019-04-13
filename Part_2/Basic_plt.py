import cv2
import matplotlib.pyplot as plt
import numpy as np

# 透過cv2.imread來讀取照片
img_orig = cv2.imread("../Test_Photo/cat.jpg")

# 這邊需要注意的是因為cv2 在顏色上面的順序是不同的
# plt 的顏色是RGB, 但cv2 的顏色是 BGR
# 所以我們需要透過轉色的方式才可以將圖片正常顯示
img_color = cv2.cvtColor(img_orig,cv2.COLOR_BGR2RGB)

plt.imshow(img_orig)
plt.imshow(img_color)
plt.show()

# 建立一個全黑的背景
#bg = np.ones((512,512,3))*255

#print(bg)

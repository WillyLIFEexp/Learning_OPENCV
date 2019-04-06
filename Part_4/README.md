# Part4 Video Basic with OPENCV
## Connect with WebCam

透過cv2的VideoCapture, 我們可以連結到電腦的WebCam

`cv2.VideoCapture(0)`

Function 裡面的`0`代表著default的WebCam

之前在學習如何透過OpecnCV讀取照片時RGB的順序會變調整為BGR
因此我們在圖取照片後還需要透過`cv2.cvtColor()` 的幫助才能
將照片以正常的方式顯示出來

![Hello](https://snag.gy/F3yA1p.jpg) ![alt text](https://snag.gy/nPO2Iz.jpg)

但在抓取影片時, OpenCV已經顏色的順序調整好所以在抓取影像時不需要
再特別去轉顏色的順序

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

我們透過While迴圈不斷地抓取抓取照片, 因影片其實就是不間斷的照片
抓到照片後我們就可以依照需求對照片進行處理, 接下來再透過`cv2.imshow()`
的方式將照片顯示出來

如果有要將影像存起來, 我們可以透過定義`cv2.VideoWriter()`的方式將影片存取
只是要注意在定義VideoWriter時裡面的fourcc的參數,可透過下面兩個表格自己需要用哪種fourcc


## 讀取Video

這邊也是透過cv2的VideoCapture, 我們可以讀取影片

`cv2.VideoCapture("vidoe/path/name.mp4")`

因為透過cv2顯示影片的速度非常的快, 並不是給我們人讀的速度
所以記得需要透過time delay的方式將影片放慢速度

當我們開始在讀取影片時, cv2.VideoCapture()會回傳兩個直回來
一個是ret, 是來判定是否有影片回傳回來, 另一個則是frame, 是照片的資訊
所以我們可以透過ret 來確認影片是否已結束

### Reference
[Wiki](https://en.wikipedia.org/wiki/FourCC)

[List](https://gist.github.com/takuma7/44f9ecb028ff00e2132e)

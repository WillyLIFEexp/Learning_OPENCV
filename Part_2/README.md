# Image Basics with OpenCV

## 透過OpenCV將照片打開
透過cv2.imread()的方式, 我們可以先將照片以Numpy array的
格式存進我們所定義的參數裡面
`img = cv2.imread("../Test_Photo/cat.jpg")`

那我們用opecv的imshow的方式顯示照片. 但要透過While的
方式才能保持圖片打開, 完整的程式如下
```python
while True:
    # 將照片顯示出來
    cv2.imshow('cat',img)

    # 當使用者點擊Q時可將會結束回圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```



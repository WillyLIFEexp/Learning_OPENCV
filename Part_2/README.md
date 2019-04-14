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

## 透過OpenCV畫出基本圖型
OpenCV有提供幾種以下方式讓使用者可以在照片或者影片中進行畫圖
1. cv2.rectangle
2. cv2.circle
3. cv2.line
4. cv2.putText
5. cv2.polylines

透過jupyter notebook可以快速的讓我們了解每個使用的方式


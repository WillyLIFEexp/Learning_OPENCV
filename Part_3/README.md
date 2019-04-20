# Image Processing

這裡講的主要是關於影像的一些基本處理

## Color Mapping
現在知道如何透過matplotlib 來讀取照片, 現在來看看關於顏色順序的問題除了我們熟悉的BGR,RGB. 這邊也會在介紹關於 HSL 與 HSV

## Blending and Pasting 
在這邊我們學習如何將兩張照片,同樣大小或不同大小的圖片,透過重疊的方式將兩張照片和成為一張. 除此之外,我們也會在這邊學習到關於Mask的使用方法與觀念

## Image Thresholding
我們先將照片轉換成黑跟白再透過 Thresholding 的方式將我們想要抓取的部分區分出來
這邊需注意就是關於設定threshold 1 與 2 的關係, 透過cv2.threshold的方式
照片中的值指要只要低於Threshold, lower bound,就直接轉換成0, 如果超過lower bound 的話將
直接轉換成 threshold 2, max value.

## Image Blurring and Smoothing
透過影像模糊的方式, 我們可以將照片中一些比較不重要的資訊去除掉. 這樣可以讓我們更容易透過其他方式將我們認為重要的資訊抓取出來.
此練習我們將會使用以下的方式進行模糊的動作
• filter2D
    • 對於此function, 我們需要瞭解什麼叫做ddepth. 透過Google大神的解釋是ddepth是用來定義當照片回傳時要用哪種格式存取圖片.格式有unsigned char (CV_8U), signed char (CV_8S), unsigned short (CV_16U),還有其他的. 如果選擇-1的話就是要依照輸入的格式存取輸出照片
• blur
• GaussianBlur
    • A linear operation
    • 透過sigma來決定多少edges可以被保存
• medianBlur
    • A non-linear operation
    • 將圖片中的pixel值透過附近的median值來取代
    • Edges可以被保存
• bilateralFilter
    • A non-linear operation
    • Edge-preserving, and noise-reducing smoothing filter for images
Reference:
[Difference](https://stackoverflow.com/questions/43392956/explanation-for-ddepth-parameter-in-cv2-filter2d-opencv)
## Morphological Operations


## Gradients 

## Histogram


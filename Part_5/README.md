# Object Detection

## Template Matching
這是最基本的物件追蹤, 如果要使用這種方式比對的圖片要完全一模一樣才有辦法比對到
對應的方式是透過將已知的小照片沿著大照片一格一格掃過去, 直到找到一樣的圖案

## Corner Detection
對於這部分我們要先定義在照片中的corner是什麼? 在照片中corner的定義就是兩個邊邊的接觸點
以及照片亮度的強烈反差.
此教學主要會focus 在以下兩種不同的corner detection 的方式
1. Harris Corner Detection
2. Shi-Tomasi Corner Deteciton

## Edge Detection
現在了解可以透過上面兩種方式幫我們抓取到照片中Corner的部分,現在我們要透過CV2 所提供的方式,
Canny Edge Detection,來找學照片中物品的外誆. 

Wiki :https://en.wikipedia.org/wiki/Canny_edge_detector


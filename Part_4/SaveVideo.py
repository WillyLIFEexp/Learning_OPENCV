import cv2

# 定義一個變數叫做Cap並使用cv2.VideoCapture()來抓取對應的視訊機
cap = cv2.VideoCapture(0)

# 如需要抓取影像的高度與寬度可以使用以下兩個function抓取
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 定義存取影片的位置,名稱,Codec,高度與寬度
# 在定義fourcc時先確定自己的OS是對應到哪個
writer = cv2.VideoWriter('../Part_4/my_capture.mp4', cv2.VideoWriter_fourcc(*'avc1'),25, (width, height))

# 透過While迴圈不斷地抓取抓取照片, 因影片其實就是不間斷的照片
while True:
    # 抓取照片
    ret,frame = cap.read()
    
    # 從之前學習到的, 因OpenCV對應的RGB位子順序不同所以抓取到照片時需要再調整順序
    # 但在影像抓取時, 顏色的部分已經轉製好了所以不需要特別在做調整
    g_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 將抓取的圖片存進檔案裡面
    writer.write(frame)
    
    # 透過之前的方式將照片顯示出來
    cv2.imshow("img",frame)
    cv2.imshow("g_img",g_img)
    
    # 透過按q來結束迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# 將所有東西結束
cap.release()
writer.release()
cv2.destroyAllWindows()

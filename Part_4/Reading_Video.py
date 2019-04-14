import cv2
import time 

# 透過cv2.VideoCapture()來讀取影片
cap = cv2.VideoCapture("video_capture.mp4")

# 因在讀取影片時, 電腦讀取影片的速度不是給我們人讀的速度
# 所以需要調整fps才讓我們人方便讀取
fps = 25

# 為了確保影片是否可以被正常讀取, 先確認是否可以正常開啟你的影片
if cap.isOpened() == False:
    print("Something is not right")

# 透過while迴圈來確認影片是否開啟與結束
while cap.isOpened():
  
    # 抓取照片
    # ret -> 回傳True/False
    # frame -> 回傳照片的資訊
    ret,frame = cap.read()

    # 如果影片還有的話, ret 會回傳True
    if ret == True:
       # 如上面所述的, 因為需要讓我們人方便的看影片所以需要放delay
        time.sleep(1/fps)
        cv2.imshow("img",frame)
       
       # 透過按q來結束迴圈
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        
# 將VideoCapture 結束
cap.release()
cv2.destroyAllWindows()

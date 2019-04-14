import cv2

# 定義劃框框的function
def draw_rect(event,x,y,flag,param):
    global pt1,pt2,firstPoint,secondPoint
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if firstPoint and secondPoint:
            pt1 = (0,0)
            pt2 = (0,0)
            firstPoint = False
            secondPoint= False
       
        if firstPoint == False:
            pt1 = (x,y)
            firstPoint = True
        elif secondPoint == False:
            pt2 = (x,y)
            secondPoint = True

# 定義一個變數叫做Cap並使用cv2.VideoCapture()來抓取對應的視訊機
cap = cv2.VideoCapture(0)

# 定義一些global variable
pt1 = (0,0)
pt2 = (0,0)
firstPoint = False
secondPoint= False

# 定義視窗名稱
cv2.namedWindow("Test")
# 透過setMouseCallBack, cv2就能知道我們在點哪個視窗應該要觸發什麼樣的事件
cv2.setMouseCallback("Test", draw_rect)

# 透過While迴圈不斷地抓取抓取照片, 因影片其實就是不間斷的照片
while True:
    # 抓取照片
    ret,frame = cap.read()

    if firstPoint:
        cv2.circle(frame, pt1,5,(255,0,0),3)
    
    if firstPoint and secondPoint:
        cv2.circle(frame, pt2,5,(255,0,0),3)
        cv2.rectangle(frame,pt1,pt2,(0,0,255),3)     

    cv2.imshow("Test",frame) 
    
    # 透過按q來結束迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# 將VideoCapture 結束
cap.release()
cv2.destroyAllWindows()

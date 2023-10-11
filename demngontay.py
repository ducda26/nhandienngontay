import cv2
import time
import os
import hand as htm

cap = cv2.VideoCapture(0)  # nếu có nhiều cam thì thêm id webcam  1,2,3..

FolderPath = "Fingers"
lst = os.listdir(FolderPath)

lst_2 = []
for i in lst:
    image = cv2.imread(f'{FolderPath}/{i}')
    print(f'{FolderPath}/{i}')
    lst_2.append(image)
# print(lst_2[0].shape)
pTime=0

while True:
    ret, frame = cap.read()
    h, w, c = lst_2[0].shape
    frame[0:h, 0:w] = lst_2[0]

    #Viết ra FPS
    cTime=time.time()  # trả về số giây, tính từ 0:0:00 ngày 1/1/1970 theo giờ  utc , gọi là(thời điểm bắt đầu thời gian)
    fps=1/(cTime-pTime) # tính fps Frames per second - đây là  chỉ số khung hình trên mỗi giây
    pTime=cTime
    # print(type(fps))
    
    # show fps lên màn hình, fps hiện đang là kiểu float , ktra print(type(fps))
    cv2.putText(frame, f"FPS: {int(fps)}",(150,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    
    cv2.imshow("Anh Duc", frame)
    if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
        break

cap.release()  # giai phong camera
cv2.destroyAllWindows()

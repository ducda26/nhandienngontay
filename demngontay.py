import cv2
import time
import os
import hand as htm

cap = cv2.VideoCapture(0) # nếu có nhiều cam thì thêm id webcam  1,2,3..

FolderPath = "Fingers"
lst = os.listdir(FolderPath)

lst_2 = []
for i in lst:
    image = cv2.imread(f'{FolderPath}/{i}')
    print(f'{FolderPath}/{i}')
    lst_2.append(image)
print(lst_2[0].shape)

while True:
    ret, frame = cap.read()
    h, w, c = lst_2[0].shape
    frame[0:h, 0:w] = lst_2[0]
    
    cv2.imshow("Anh Duc", frame)
    if cv2.waitKey(1) == ord("q"): # độ trễ 1/1000s , nếu bấm q sẽ thoát
        break

cap.release() #giai phong camera
cv2.destroyAllWindows()
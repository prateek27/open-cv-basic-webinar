import cv2


# Camera Object
camera = cv2.VideoCapture(0)


while True:
    success,pic = camera.read()
    
    if success==False:
        continue
        
    cv2.imshow("Video Frame",pic)
    # Pause the loop for 1 ms
    cv2.waitKey(1)
    




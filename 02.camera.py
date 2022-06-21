import cv2
import time

def main():
    camera = cv2.VideoCapture(0)
    camera.set(3, 640)
    camera.set(4, 480)
  
    while( camera.isOpened() ):
        
        keyValue = cv2.waitKey(10)
        print(str(keyValue))
        
        if keyValue == ord('q') :
            break
        
        _, image = camera.read()
        cv2.imshow('Original', image)
            
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()

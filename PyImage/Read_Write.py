'''
read and write an image

images/Judson.jpg

'''
import cv2
in_image=cv2.imread('images/Judson.jpg',-1)
out_image=cv2.imwrite('images/Judson_Copy.jpg',in_image)
try:
    cv2.imshow('ME',in_image)
    k=cv2.waitKey(0)& 0xff
    if k ==27:
        
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('images/Judson_copy.jpg',in_image)
        cv2.destroyAllWindows()
    elif k==ord('c'):
        in_imageGray=cv2.cvtColor(in_image,cv2.COLOR_RGB2GRAY)
        canny=cv2.Canny(in_imageGray,120,255)
        cv2.imwrite('images/Judson2_copy.jpg',canny)
        cv2.imshow('images/Judson2_copy.jpg',canny)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
except Exception as err:
    print("ERROR: ",err)
    

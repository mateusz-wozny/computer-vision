import cv2
import numpy as np

orig_img= cv2.imread('assets/python.png')
img=orig_img.copy()
# cv2.imshow('Python', mat=img)
# cv2.waitKey()

h, w=img.shape[:2]

#Draw line
# cv2.line(img=img, pt1=(0,0), pt2=(w,h), color=(0,255,0), thickness=4)
# cv2.imshow('Python', mat=img)
# cv2.waitKey()

#Draw rectangle
# cv2.rectangle(img=img, pt1=(200,50), pt2=(400,230), color=(0,255,0), thickness=4)
# cv2.imshow('Python', mat=img)
# cv2.waitKey()

#Draw polygons

# pts=np.array([[300,140], [200,200], [200,50],[300,50]], dtype=np.int32).reshape((-1,1,2))
# cv2.polylines(img, pts=[pts], isClosed=False, color=(0,0,255), thickness=3)
# cv2.imshow('Python', mat=img)
# cv2.waitKey()
#Draw text
cv2.putText(img,
            text="Python",
            org=(20,40),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1.5,
            color=(0,0,200),
            thickness=2)
cv2.imshow('Python', mat=img)
cv2.waitKey()
import requests as rq
import cv2 as cv
import numpy as np
import time
url = "http://inquiry.ecust.edu.cn/jsxsd/verifycode.servlet"
c = ''
k = 111
c = str(int(time.time()))
print(c)
while c != 'q':
    k = k + 1
    p = rq.get(url)
    p = p.content
    #读取图像，支持 bmp、jpg、png、tiff 等常用格式
    image = np.asarray(bytearray(p), dtype="uint8")
    img = cv.imdecode(image,flags=cv.IMREAD_COLOR)
    cv.namedWindow("Image")
    cv.imshow("Image",img)
    cv.waitKey(0)
    #释放窗口
    cv.destroyAllWindows()
    a = input("验证码为:")
    if len(a) == 0:
        continue
    f = open("%s_%d.jpg"%(a,k),"wb+")
    f.write(p)
    f.close()

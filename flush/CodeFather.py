import requests
import io
class CodeFather:
    @staticmethod
    def RFromFile(filename:str):
        files = {'image_file': (filename, open(filename, 'rb'), 'application')}
        r = requests.post(url='http://118.25.91.92:6000/ecust', data={'key': 'ecust'}, files=files)
        return r.json()

    @staticmethod
    def RFromBytes(bname:bytes):
        f = io.BytesIO()
        f.write(bname)
        binData = f.getvalue()
        f.close()
        files = {'image_file': ('BytesNoName.jpg',binData,'application')}
        r = requests.post(url='http://118.25.91.92:6000/ecust', data={'key': 'ecust'}, files=files)
        return r.json()

if __name__ == "__main__":
    import cv2 as cv
    import numpy as np
    url = "http://inquiry.ecust.edu.cn/jsxsd/verifycode.servlet"
    p = requests.get(url)
    p = p.content
    image = np.asarray(bytearray(p), dtype="uint8")
    img = cv.imdecode(image, flags=cv.IMREAD_COLOR)
    cv.namedWindow("Image")
    cv.imshow("Image", img)
    cv.waitKey(0)
    sk = CodeFather.RFromBytes(p)
    print(sk)

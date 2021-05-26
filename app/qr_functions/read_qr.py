import cv2


def read_qrcode(filename):
    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    if bbox is not None:
        return data

# print(read_qrcode("fb_com.png"))

import cv2
def Read_Uploaded_Image():
    img=cv2.imread("medium.png")
    det=cv2.QRCodeDetector()
    val, pts, st_code=det.detectAndDecode(img)
    print(val)
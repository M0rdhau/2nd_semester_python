try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import sys

imgurl = "hqdefault.jpg"
readimgurl = "sign.jpg"

img = cv2.imread(imgurl)
readimg = cv2.imread(readimgurl)
dimensions = img.shape[0:2]
readdimensions = readimg.shape[0:2]
resizedimensions = (int(readdimensions[0]*1/4), int(readdimensions[1]*1/4))

cv2.imshow("Text reading from image", cv2.resize(readimg, resizedimensions))
cv2.waitKey(0)
print("Image text: \n")
print(pytesseract.image_to_string(Image.open(readimgurl)))
cv2.destroyAllWindows()



# Rotating the image by 60 degrees
rotMatrix = cv2.getRotationMatrix2D((dimensions[0]/2, dimensions[1]/2), 60, 1)
rotImage = cv2.warpAffine(img, rotMatrix, (dimensions[0], dimensions[1]))
croppedImage = img[int(dimensions[0]*1/3):int(dimensions[0]*2/3),
                   int(dimensions[1]*1/3 + 10):int(dimensions[1]*2/3 + 10)]
cv2.imshow('Rotated Image', rotImage)
cv2.waitKey(0)
cv2.imshow('Cropped Image', croppedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

noiseUrl = "floppa.jpg"
noiseimg = cv2.imread(noiseUrl)
result = cv2.fastNlMeansDenoisingColored(noiseimg, None, 20, 10, 7, 21)
cv2.imshow('Original', noiseimg)
cv2.waitKey(0)
cv2.imshow('Noise Cleaned', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

sys.exit()
from PIL import Image
import numpy



# open images and make the same size
im = Image.open("eat_micro.jpg").resize((256, 256))
data = im.getdata()
im.show()

colors = im.getpixel((120,120)) #rgb values in a concrete pixel
r = colors[0]
g = colors[1]
b = colors[2]

# convert to YCbCr
Y= 0 + (0.299*r)+(0.587*g)+(0.114*b)
Cb = 128 - (0.168736*r)-(0.331264*g)+(0.5*b)
Cr = 128 + (0.500*r) - (0.418688 * g) - (0.081312 * b)

# convert to RGB again
R = Y + 1.402*(Cr-128)
G = Y-0.34414 * (Cb-128) - 0.71414*(Cr-128)
B = Y + 1.772*(Cb-128)


print ("The value of R (RGB) before any conversion is",r)

print ("The value after the conversion to YCbCr is ",Y)
print ("The value R after YCbCr->RGB is ",R)

print("Close enough!")

#cv2.COLOR_BGR2YUV
#cv2.COLOR_BGR2YCrCb


# Para pasar a YUV:

#import cv2

## get all color codes

#codes = [x for x in dir(cv2) if x.startswith("COLOR_")]

## print first three color codes
#print(codes[:3])

# ['COLOR_BAYER_BG2BGR', 'COLOR_BAYER_BG2BGRA', 'COLOR_BAYER_BG2BGR_EA']

# print all color codes
#print(codes)

#img = cv2.imread("eat_micro.jpg")
#yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
#cv2.imwrite("yuv.png", yuv)








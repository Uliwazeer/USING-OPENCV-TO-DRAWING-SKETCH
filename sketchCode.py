

#https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html


import cv2
image = cv2.imread('girl.jpg') # loads an image from the specified file
# convert an image from one color space to another
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img) # helps in masking of the image
# sharp edges in images are smoothed while minimizing too much blurring
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
cv2.imwrite("sketch.png", sketch) # converted image is saved as mentioned name

cv2.imshow('sketch',sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()








import cv2

image=cv2.imread('girl.jpg')
grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert=cv2.bitwise_not(grey_image)
blur=cv2.GaussianBlur(invert,(55,55),0)
invertednlur=cv2.bitwise_not(blur)
sketch=cv2.divide(grey_image,invertednlur,scale=256.0)

cv2.imshow('sketch',sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()






vowels=['a','e','i','o','u']
word=input('provide a word to look for vowels')
found={}
found['a']=0
found['e']=0
found['i']=0
found['o']=0
found['u']=0

for letter in word:
    if letter in vowels:
        found[letter]+=1
for k,v in found.items():
    print(k,'found \t ',v, 'times')



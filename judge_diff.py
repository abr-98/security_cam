from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def mse(imageA,imageB):
  err=np.sum(imageA.astype("float")-imageB.astype("float")**2)
  err/=float(imageA.shape[0]*imageA.shape[1])
  return err
def compare_images(imageA,imageB):
  img_a=cv2.imread(imageA)
  img_b=cv2.imread(imageB)
  imga_g=cv2.cvtColor(img_a,cv2.COLOR_BGR2GRAY)
  imgb_g=cv2.cvtColor(img_b,cv2.COLOR_BGR2GRAY)
  cv2.imshow("img_a",imga_g)
  cv2.imshow("img_b",imgb_g)
  m=mse(imga_g,imgb_g)
  s=ssim(imga_g,imgb_g)
 # print(s," ",m)
  if m!=0 and s<=0.9 :
    return -1
  else:
    return 1
#if __name__ == '__main__':
#    k=compare_images("frame8.jpg","frame9.jpg")
#    print(k)

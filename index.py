import numpy as np, matplotlib.pyplot as plt
from PIL import Image
from scipy import spatial
import imghdr

import os
path = os.path.abspath('./')   #表示当前所处的文件夹的绝对路径

def traverse(f):
    array = []
    fs = os.listdir(f)
    for f1 in fs:
        tmp_path = os.path.join(f,f1)
        if not os.path.isdir(tmp_path):
            if (imghdr.what(tmp_path) == 'png'):
              array.append(tmp_path)
        else:
            traverse(tmp_path)
    return array
            




              

# 计算指纹相似度
def calcImgSimHash(img1, img2):
  # 图像像素均值
  mean1 = np.mean(img1)
  mean2 = np.mean(img2)
  # 每个像素点与图像像素均值的距离
  distance1 = np.greater_equal(img1, mean1)
  distance2 = np.greater_equal(img2, mean2)
  # 通过汉明距离, 计算相似度
  return 1 - spatial.distance.hamming(distance1.flatten(), distance2.flatten())

if __name__ == '__main__':
  # 加载图片

  img_1 = Image.open(path + '/ic-jijing-forecast@2x.png').convert('YCbCr').resize((180, 180))
  img_2 = Image.open(path + '/ic-jijing-forecast@3x.png').convert('YCbCr').resize((180, 180))
  # 图片转numpy矩阵
  img_1_mat = np.asarray(img_1)
  img_2_mat = np.asarray(img_2)



def imageAll():
    array = traverse(path)
    conformIMG = []
    for i, img in enumerate(array):
        for j in range(i + 1, len(array)):
                print(i, j)
                img_1 = Image.open(img).convert('YCbCr').resize((180, 180))
                img_2 = Image.open(array[j]).convert('YCbCr').resize((180, 180))
                # 图片转numpy矩阵
                img_1_mat = np.asarray(img_1)
                img_2_mat = np.asarray(img_2)
                num = calcImgSimHash(img_1_mat, img_2_mat)
                if(num > 0.95):
                  conformIMG.append(img)
                  conformIMG.append(array[j])

    return conformIMG

# print(imageAll())
#   # 计算图片相似度
print(calcImgSimHash(img_1_mat, img_2_mat))
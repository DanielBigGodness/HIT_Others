#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import cv2
import math
import numpy as np


def int2bin8(x):                               # 整型转8位二进制
    result="";
    for i in range(8):
        y=x&(1)
        result+=str(y)
        x=x>>1
    return result[::-1]

def int2bin16(x):                              # 整型转8位二进制
    result="";
    for i in range(16):
        y=x&(1)
        result+=str(y)
        x=x>>1
    return result

def Encryption(img,j0,g0,x0,EncryptionImg):
    x = img.shape[0]
    y = img.shape[1]
    c = img.shape[2]
    g0 = int2bin16(g0)
    for s in range(x):
        for n in range(y):
            for z in range(c):
                m = int2bin8(img[s][n][z])                   # 像素值转八位二进制
                ans=""
                #print("ok")
                for i in range(8):
                    ri=int(g0[-1])                           # 取手摇密码机最后一位ri
                    qi=int(m[i])^ri                          # 与像素值异或得qi
                    xi = 1 - math.sqrt(abs(2 * x0 - 1))      # f1(x)混沌迭代
                    if qi==0:                                # 如果qi=0,则运用x0i+x1i=1;
                        xi=1-xi;
                    x0=xi                                    # xi迭代
                    t=int(g0[0])^int(g0[12])^int(g0[15])     # 本源多项式x^15+x^3+1
                    g0=str(t)+g0[0:-1]                       # gi迭代
                    ci=math.floor(xi*(2**j0))%2              # 非线性转换算子
                    ans+=str(ci)
                re=int(ans,2)
                EncryptionImg[s][n][z]=re                    # 写入新图像

def Decryption(EncryptionImg, j0, g0, x0, DecryptionImg):
    x = EncryptionImg.shape[0]
    y = EncryptionImg.shape[1]
    c = EncryptionImg.shape[2]
    g0 = int2bin16(g0)
    for s in range(x):
        for n in range(y):
            for z in range(c):
                cc = int2bin8(img[s][n][z])
                ans = ""
                print("no")
                for i in range(8):
                    xi = 1 - math.sqrt(abs(2 * x0 - 1))
                    x0 = xi
                    ssi = math.floor(xi * (2 ** j0)) % 2
                    qi=1-(ssi^int(cc[i]))
                    ri = int(g0[-1])
                    mi=ri^qi
                    t = int(g0[0]) ^ int(g0[12]) ^ int(g0[15])
                    g0 = str(t) + g0[0:-1]
                    ans += str(mi)
                re = int(ans, 2)
                DecryptionImg[s][n][z] = re


if __name__ == "__main__":
    img = cv2.imread("1.png", 1)                    # 读取原始图像
    cv2.imshow("img", img)                                                             # 显示原图

    EncryptionImg = np.zeros(img.shape, np.uint8)
    Encryption(img,10,30,0.123345,EncryptionImg)                                       # 加密
    cv2.imwrite("2.png",EncryptionImg)  # 保存
    cv2.imshow("EncryptionImg", EncryptionImg)                                        # 显示

    img = cv2.imread("2.png", 1)        # 读取加密图像
    DecryptionImg = np.zeros(img.shape, np.uint8)
    Decryption(img, 10, 30, 0.123345, DecryptionImg)                                   # 解密
    cv2.imwrite("3.png", DecryptionImg) # 保存
    cv2.imshow("DecryptionImg ", DecryptionImg)                                        # 显示

    cv2.waitKey(0)



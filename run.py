import base64

import cv2
import numpy as np
import requests


my_img_path = './img/picture.jpg'
my_img_outpath = './img/'

def get_mouth(dst_pic):
    with open(dst_pic, 'rb') as f:
        base64_data = base64.b64encode(f.read())
    url='https://api-cn.faceplusplus.com/facepp/v1/face/thousandlandmark'
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    data={
          # Use your own api_key,api_secret, apply through face++ website
          'api_key':'JEQ8NyE9zruxqCed9I8jOhBpsO5d-_T-',
          'api_secret':'kmRg7hOHvgtobAt3UDw4Y5L-SM-Bm-Fk',
          'return_landmark': 'mouth',
          'image_base64': base64_data,
                         }
    r=requests.post(url,headers=headers,data=data)
    mouth=r.json()['face']['landmark']['mouth']
    x,y=[],[]
    for i in mouth.values():
        y.append(i['y'])
        x.append(i['x'])
    y_max=max(y)
    y_min=min(y)
    x_max=max(x)
    x_min=min(x)
    middle_x=int((x_max+x_min)/2)
    middle_y=int((y_max+y_min)/2)
    size=(int(3*(x_max-x_min)),int(5*(y_max-y_min)))
    return (middle_x,middle_y),size

def add_mask(img_path, img_outPath):
    src_pic = "./img/N95.jpg" # 口罩路径
    center, size = get_mouth(img_path)
    src = cv2.imread(src_pic)
    src = cv2.resize(src, size)
    dst = cv2.imread(img_path)

    mask = 255*np.ones(src.shape, src.dtype)
    output = cv2.seamlessClone(src, dst, mask, center, cv2.NORMAL_CLONE)
    cv2.imshow('output', output)
    cv2.waitKey()

add_mask(my_img_path, my_img_outpath)
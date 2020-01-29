import base64

import requests


def get_mouth(dst_pic):
    with open(dst_pic, 'rb') as f:
        base64_data = base64.b64decode(f.read())
        url = 'https://api-cn.faceplusplus.com/facepp/v1/face/thousandlandmark'
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
        }
        data={
            'api_key':'JEQ8NyE9zruxqCed9I8jOhBpsO5d-_T-',
            'api_sercet':'	kmRg7hOHvgtobAt3UDw4Y5L-SM-Bm-Fk',
            'return_landmark': 'mouth',
            'image_base64': base64_data
        }
        r = requests.post(url, headers=headers, data=data)
        mouth = r.json()['face']['landmark']['mouth']
        x,y = [],[]
        for i in mouth.values():
            y.append(i['y'])
            x.append(i['x'])
        y_max = max(y)
        y_min = min(y)
        x_max = max(x)
        x_min = min(x)
        middle_x = int((x_max + x_min)/2)
        middle_y = int((y_max + y_min)/2)
        size = (int(3 * (x_max - x_min)), int(5 * (y_max - y_min)))
        return (middle_x, middle_y), size
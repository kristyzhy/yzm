# -*- coding: utf-8 -*-
# @Software: PyCharm
import requests
import time
import json
from PIL import Image
from io import BytesIO
from collections import Counter
def get_max_char(str):
    '''
    获取频率最高字符
    :param str:
    :return:
    '''
    count = Counter(str)
    count_list = list(count.values())
    max_value = max(count_list)
    max_list = []
    for k, v in count.items():
        if v == max_value:
            max_list.append(k)
    return max_list[0]
def recogition(yzm_data):
    '''
    验证码识别
    :param yzm_data:
    :return:
    '''
    resp = requests.post('http://127.0.0.1:8080', data=yzm_data)
    return resp.text

def img_to_text(yzmdatas):
    '''
    图片转字符
    :param length:
    :return:
    '''
    yzm1 = ""
    yzm2 = ""
    yzm3 = ""
    yzm4 = ""
    for data in yzmdatas:
        text = recogition(data)
        json_obj = json.loads(text)
        yzm_text = json_obj.get("code","")
        #本文中的验证码长度为4    实际测试中只要长度大于等于4的都可以统计进去，不影响识别准确率
        if len(yzm_text) == 4:
            l_yzm = list(yzm_text)
            yzm1 = yzm1 + l_yzm[0]
            yzm2 = yzm2 + l_yzm[1]
            yzm3 = yzm3 + l_yzm[2]
            yzm4 = yzm4 + l_yzm[3]
    yzm1 = get_max_char(yzm1)
    yzm2 = get_max_char(yzm2)
    yzm3 = get_max_char(yzm3)
    yzm4 = get_max_char(yzm4)
    return yzm1+yzm2+yzm3+yzm4
def download():
    '''
    下载验证码
    :return:
    '''
    #验证码地址
    url = 'http://credit.customs.gov.cn/ccppserver/verifyCode/creator'
    resp = requests.get(url)
    data = resp.content
    return data
def gif_to_png(length,image):
    '''
    gif抽帧
    :param length:
    :param image:
    :return:
    '''
    try:
        yzm_list = []
        for i in range(1, length):
            image.seek(i)
            stream = BytesIO()
            image.save(stream, 'PNG')
            s = stream.getvalue()
            yzm_list.append(s)
        return yzm_list
    except Exception as e:
        print(e)
    return None
def handle_yzm(length):
    '''
    处理验证码
    :return:
    '''
    gif = download()
    start = time.time()
    if gif:
        data = BytesIO(gif)
        image = Image.open(data)
        png_list = gif_to_png(length, image)
        if png_list:
            yzm_text = img_to_text(png_list)
    with open("./Gif_IMG/{}_{}.gif".format(yzm_text, str(time.time())),"wb") as fw:
        fw.write(gif)
    end = time.time()
    print("抽帧length:{}-花费时间：{}".format(length, end - start))
def run():
    #抽帧长度：具体抽帧多少可以依据实际的gif识别准确率来调整。
    #抽帧越少识别率可能会低，但是识别所需的时间会减少。23帧准确率98%，时间1s； 6帧准确率85%，时间0.5s左右
    #在识别速度和精度之间找一个平衡点即可
    length = 10
    #识别图片个数
    num = 20
    for i in range(num):
        handle_yzm(length)
if __name__ == '__main__':
    run()

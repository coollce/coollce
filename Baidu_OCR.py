# encoding:utf-8
# author:callyer
# datetime:2020/11/25
import requests
import base64

# client_id 为官网获取的AK， client_secret 为官网获取的SK
client_id='xxxxxxxxxxxxxx'
client_secret='xxxxxxxxxxxxx'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(client_id,client_secret)
response = requests.get(host).json()
print(response)
print(response['access_token'])
access_token=response['access_token']

'''
通用文字识别（高精度版）
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
with open('123.jpg', 'rb') as f:
    img = base64.b64encode(f.read())
params = {"image":img}
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
    print(response.json()['words_result'][0]['words'])

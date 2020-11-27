# -*-coding:utf-8 -*-
#!/usr/bin/env python
# for callyer
import hashlib
import requests
import re
import sys
import 

import json


def get_md5(data):
    obj = hashlib.md5()
    obj.update(data.encode('utf-8'))
    result = obj.hexdigest()
    return result


def login(username, passwd, questionid, answer):
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    data = {'username': username, 'password': pwd, 'questionid': questionid, 'answer': answer}
    response = requests.post(url=login_url, headers=headers, data=data)
    error = re.findall('密码错误次数过多，请 15 分钟后重新登录', response.text)

    cookie = requests.utils.dict_from_cookiejar(response.cookies)

    if not re.findall('.*' + username + '.*', response.text):
        print('第' + str(i + 1) + '个账号登陆失败，请检查用户名与密码')
        print(error[0])
        print()
        return 1
    else:
        print('登陆成功')
        return cookie


def Sign(sign_ID):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
               "Accept": "application/json, text/javascript, */*; q=0.01",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "X-Requested-With": "XMLHttpRequest",
               }
    data = {"formhash": sign_ID, "signsubmit": "apply"}
    response = requests.post(url=Sign_url, headers=headers, cookies=cookies, data=data)
    # with open('tools_index.html', mode='w+') as f:
    #     userinfo = f.write(response.text)

    if re.findall('{"status":"(fail|success)"', response.text):

        if re.findall('{"status":"(fail|success)"', response.text)[0] == 'fail':
            print('签到失败')
        else:
            print('签到成功')
    else:
        print('签到出错')


def get_signid(cookies):
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}
    response = requests.get(url=get_ID_url, headers=headers, cookies=cookies)
    uid = re.findall('discuz_uid\s+=\s+(\d+)', response.text)
    url = 'https://www.t00ls.net/members-profile-' + uid[0] + '.html'
    response_2 = requests.get(url=url, headers=headers, cookies=cookies)
    if re.findall('value="已签到 \(\d天\)"', response_2.text):
        return 0
    else:
        sign_ID = re.findall('javascript:WebSign\(\'(.*)?\'\)', response_2.text)
        if not sign_ID[0]:
            print('未获取到签到ID')
            return
        else:
            return sign_ID[0]


if __name__ == '__main__':

    login_url = "https://www.t00ls.net/logging.php?action=login&loginsubmit=yes&inajax=1"
    get_ID_url = 'https://www.t00ls.net/memcp.php'
    Sign_url = "https://www.t00ls.net/ajax-sign.json"

    isfile = os.path.isfile('toolsuser.txt')
    if not isfile:
        fp = open("toolsuser.txt", mode='w')
        fp.close()
        print('文件不存在')
        print('toolsuser.txt创建完成，请在文本中输入账号信息')

    with open('toolsuser.txt', mode='r+', encoding='utf-8') as f:
        userinfo=json.load(f)
    print(userinfo)

    if len(userinfo) < 4:
        print("请在toolsuser.txt中按照  json格式填写用户名，密码，安全问题编号和安全问题答案：example：{'username': 'xxxx', 'password': 'xxxx', 'questionid': '1', 'question_answer': 'xxx'}")
        sys.exit()
# 也可以直接在这输入用户信息，把91-104行注释掉即可

    username = userinfo['username']
    passwd = userinfo['password']
    questionid = userinfo['questionid']
    answer = userinfo['question_answer']
    print(username,passwd,questionid,answer)

    pwd = get_md5(passwd)
    cookies = login(username, pwd, questionid, answer)
    sign_ID = get_signid(cookies)
    if sign_ID == 0:
        print('此账号已经签到')
    else:
        Sign(sign_ID)

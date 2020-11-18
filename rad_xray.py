import subprocess,time
#rad路径,使用相对路径
rad_path="rad_windows_amd64.exe"
#xray路径，使用相对路径
xray_path="xray_windows_amd64.exe"
#扫描的目标url
url="http://10.51.30.34:8999"
#xray启动代理地址
xrayProxy="127.0.0.1:7799"

def Scan(target,startxray):
	cmd = [rad_path,"-t",target,"-http-proxy",xrayProxy]
	rsp=subprocess.Popen(cmd,start_new_session=True)
	rsp.communicate()
	
# with open("target.txt","r") as targats:
xrayShell = [xray_path, "webscan", "--listen", xrayProxy, "--html-output", "result4.html"]
startxray = subprocess.Popen(xrayShell)
time.sleep(10)
# targat = targats.readline().strip("\n")

Scan(url,startxray)

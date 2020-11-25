
<body marginheight="0"><h2>日常脚本</h2>
<p>更新采集中。。。


</p>
</body></html>

##信息收集
https://github.com/lz520520/railgun　　渗透工具

https://github.com/gobysec/Goby　　扫描工具（梳理资产暴露攻击面）

https://github.com/k8gege/K8CScan　　k8gege扫描器

https://github.com/chaitin/xray　　长亭Xray

https://github.com/maurosoria/dirsearch　　Dirsearch（扫目录）

https://github.com/H4ckForJob/dirmap　　Dirmap（扫目录）

https://github.com/Tuhinshubhra/CMSeeK　　CMS识别

https://github.com/shack2/SNETCracker　　超级弱口令检查工具

 

https://github.com/shmilylty/OneForAll　　子域收集工具

https://github.com/lijiejie/subDomainsBrute　　subdomainsbtute（子域）

 

https://github.com/BugScanTeam/GitHack　　Git泄露

https://github.com/BugScanTeam/GitHack　　Git 信息泄露

https://github.com/kost/dvcs-ripper　　常规信息泄露

 

https://github.com/TheKingOfDuck/fuzzDicts　　fuzzdb

https://github.com/1N3/IntruderPayloads　　fuzzdb

 

#漏洞检测攻击
https://github.com/Macr0phag3/email_hack　　钓鱼邮件

https://emkei.cz/　　伪造邮件

https://github.com/brendan-rius/c-jwt-cracker　　jwt伪造

https://github.com/feihong-cs/ShiroExploit　　Shiro 反序列化

https://github.com/dionach/CMSmap　　CMS漏洞检测工具

https://github.com/chenjj/CORScanner　　扫描CORS配置漏洞

https://github.com/deathmarine/Luyten/releases/　　Luyten反编译工具（jar包）

 

##后主机存活扫描
nbtscan.exe：nbtscan 192.168.1.1/20

arp-scan.exe：arp-scan.exe -t 192.168.1.1/24　　https://github.com/QbsuranAlang/arp-scan-windows-

ping：for /L %I in (1,1, 254) do @ping -w 1 -n 1 192.168.1.%I | findstr “TTL=”

Invoke-ARPScan.ps1： powershell.exe -exec bypass -Command “& {Import-Module c:\Invoke-ARPScan.ps1;Invoke-ARPScan -CIDR 192.168.1.1/24}” >> c:\log.txt

Powershell 渗透测试工具-Nishang　　https://github.com/samratashok/nishang

cping：cping scan smbvul 10.33.93.1 10.33.93.1

qs.exe：qs alive 192.168.1.1/24

dnsbrute

F-NAScan.py

Hscan

 

##端口扫描
s.exe： s.exe tcp 192.168.1.1 192.168.1.254 445,1433,3389,7001 256 /Banner /save

scanline： scanline -h -t 20,80-89,110,389,445,3389,1099,7001,3306,1433,8080,1521 -u 53,161 -O c:\log.txt -p 192.168.1.1-254 /b

Invoke-Portscan.ps1：Invoke-PortScan -StartAddress 192.168.1.1 -EndAddress 192.168.1.254 -ScanPort [探测存活 -ResolveHost]

K8PortScan.exe

F-NAScan.py

nmap

 

##后渗透
https://github.com/BloodHoundAD/BloodHound　　域用户

https://ngrok.com/　　内网穿透1

https://github.com/fatedier/frp　　内网穿透2

https://github.com/sensepost/reDuh　　内网穿透3

https://github.com/SECFORCE/Tunna　　内网穿透4

https://github.com/BeichenDream/Godzilla/ 　　哥斯拉 Webshell

https://github.com/rebeyond/Behinder/　　冰蝎 Webshell

https://github.com/FireFart/dirtycow　　脏牛提权（cve-2016-5159）

 View Code
https://github.com/dirtycow/dirtycow.github.io　　脏牛提权1（cve-2016-5159）

https://github.com/gbonacini/CVE-2016-5195　　脏牛提权2（cve-2016-5159）

 View Code
https://github.com/abatchy17/WindowsExploits　　提权漏洞（2017.5）

https://github.com/QAX-A-Team/BrowserGhost      浏览器信息收集

https://github.com/SecureAuthCorp/impacket　　Impacket是用于网络协议的Python类的集合

https://github.com/yangyangwithgnu/bypass_disablefunc_via_LD_PRELOAD　　disable_function.工具

 

 

###蓝队
##威胁情报
https://www.virustotal.com/　　VirusTotal

https://x.threatbook.cn/　　微步在线

https://ti.qianxin.com/　　奇安信威胁情报

https://ti.360.cn/#/homepage　　360威胁情报中心

https://www.venuseye.com.cn/　　启明星辰威胁情报

https://redqueen.tj-un.com　　REDQUEEN

https://poma.nsfocus.com/　　绿盟的威胁分析中心

https://habo.qq.com/　　腾讯哈勃系统

https://mac-cloud.riskivy.com　　FreeBuf × 漏洞盒子「大圣云沙箱」

 

##漏洞情报
https://www.secshi.com/circle/qingbao　　安全师情报共享

https://www.seebug.org/　　seebug

https://nosec.org/home/index/hole.html　　nosec

 

##webshell查杀
http://www.d99net.net/　　D盾 

https://www.shellpub.com/　　河马

-https://scanner.baidu.com　　[百度]

 

 

#应急响应工具
-https://github.com/grayddq/GScan　　Linux主机排查

-https://github.com/T0xst/linux　　Linux 安全检查


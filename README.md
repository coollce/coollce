<html>
<body marginheight="0"><h2>日常脚本</h2>
<ul>
<li>更新采集中。。。</li>
</ul>
<h2>信息收集</h2>
<ul>
<li><p><a href="https://github.com/lz520520/railgun">渗透工具</a>: <a href="https://github.com/lz520520/railgun">https://github.com/lz520520/railgun</a></p>
</li>
<li><p><a href="https://github.com/gobysec/Goby">扫描工具Goby</a>:<a href="https://github.com/gobysec/Goby">https://github.com/gobysec/Goby</a></p>
</li>
<li><p>k8gege扫描器 <a href="https://github.com/k8gege/K8CScan">https://github.com/k8gege/K8CScan</a>　　</p>
</li>
<li><p>长亭Xray <a href="https://github.com/chaitin/xray">https://github.com/chaitin/xray</a>　　</p>
</li>
<li><p>Dirsearch（扫目录） <a href="https://github.com/maurosoria/dirsearch">https://github.com/maurosoria/dirsearch</a>　　</p>
</li>
<li><p>Dirmap（扫目录） <a href="https://github.com/H4ckForJob/dirmap">https://github.com/H4ckForJob/dirmap</a>　　</p>
</li>
<li><p>CMS识别 <a href="https://github.com/Tuhinshubhra/CMSeeK">https://github.com/Tuhinshubhra/CMSeeK</a>　　</p>
</li>
</ul>
<p><a href="https://github.com/shack2/SNETCracker">超级弱口令检查工具</a>:<a href="https://github.com/shack2/SNETCracker">https://github.com/shack2/SNETCracker</a>　　


</p>
<ul>
<li><p><a href="https://github.com/shmilylty/OneForAll">https://github.com/shmilylty/OneForAll</a>　　子域收集工具</p>
</li>
<li><p><a href="https://github.com/lijiejie/subDomainsBrute">https://github.com/lijiejie/subDomainsBrute</a>　　subdomainsbtute（子域）</p>
</li>
</ul>
<ul>
<li><p><a href="https://github.com/BugScanTeam/GitHack">https://github.com/BugScanTeam/GitHack</a>　　Git泄露</p>
</li>
<li><p><a href="https://github.com/BugScanTeam/GitHack">https://github.com/BugScanTeam/GitHack</a>　　Git 信息泄露</p>
</li>
<li><p><a href="https://github.com/kost/dvcs-ripper">https://github.com/kost/dvcs-ripper</a>　　常规信息泄露</p>
</li>
</ul>
<ul>
<li><a href="https://github.com/TheKingOfDuck/fuzzDicts">https://github.com/TheKingOfDuck/fuzzDicts</a>　　fuzzdb</li>
</ul>
<h2>后主机存活扫描</h2>
<pre><code>    nbtscan.exe：nbtscan 192.168.1.1/20

    arp-scan.exe：arp-scan.exe -t 192.168.1.1/24　　https://github.com/QbsuranAlang/arp-scan-windows-

    ping：for /L %I in (1,1, 254) do @ping -w 1 -n 1 192.168.1.%I | findstr “TTL=”

    Invoke-ARPScan.ps1： powershell.exe -exec bypass -Command “&amp; {Import-Module c:\Invoke-ARPScan.ps1;Invoke-ARPScan -CIDR 192.168.1.1/24}” &gt;&gt; c:\log.txt

    Powershell 渗透测试工具-Nishang　　https://github.com/samratashok/nishang

    cping：cping scan smbvul 10.33.93.1 10.33.93.1

    qs.exe：qs alive 192.168.1.1/24

    dnsbrute

    F-NAScan.py

    Hscan</code></pre>
<h2>端口扫描</h2>
<pre><code>  s.exe： s.exe tcp 192.168.1.1 192.168.1.254 445,1433,3389,7001 256 /Banner /save

  scanline： scanline -h -t 20,80-89,110,389,445,3389,1099,7001,3306,1433,8080,1521 -u 53,161 -O c:\log.txt -p 192.168.1.1-254 /b

  Invoke-Portscan.ps1：Invoke-PortScan -StartAddress 192.168.1.1 -EndAddress 192.168.1.254 -ScanPort [探测存活 -ResolveHost]

  K8PortScan.exe

  F-NAScan.py

  nmap</code></pre>
<h2>后渗透</h2>
<ul>
<li><p><a href="https://github.com/BloodHoundAD/BloodHound">https://github.com/BloodHoundAD/BloodHound</a>　　域用户</p>
</li>
<li><p><a href="https://ngrok.com/">https://ngrok.com/</a>　　内网穿透1</p>
</li>
<li><p><a href="https://github.com/fatedier/frp">https://github.com/fatedier/frp</a>　　内网穿透2</p>
</li>
<li><p><a href="https://github.com/sensepost/reDuh">https://github.com/sensepost/reDuh</a>　　内网穿透3</p>
</li>
<li><p><a href="https://github.com/SECFORCE/Tunna">https://github.com/SECFORCE/Tunna</a>　　内网穿透4</p>
</li>
<li><p><a href="https://github.com/BeichenDream/Godzilla/">https://github.com/BeichenDream/Godzilla/</a> 　　哥斯拉 Webshell</p>
</li>
<li><p><a href="https://github.com/rebeyond/Behinder/">https://github.com/rebeyond/Behinder/</a>　　冰蝎 Webshell</p>
</li>
<li><p><a href="https://github.com/FireFart/dirtycow">https://github.com/FireFart/dirtycow</a>　　脏牛提权（cve-2016-5159）</p>
<p>View Code</p>
</li>
<li><p><a href="https://github.com/dirtycow/dirtycow.github.io">https://github.com/dirtycow/dirtycow.github.io</a>　　脏牛提权1（cve-2016-5159）</p>
</li>
<li><p><a href="https://github.com/gbonacini/CVE-2016-5195">https://github.com/gbonacini/CVE-2016-5195</a>　　脏牛提权2（cve-2016-5159）</p>
<p>View Code</p>
</li>
<li><p><a href="https://github.com/abatchy17/WindowsExploits">https://github.com/abatchy17/WindowsExploits</a>　　提权漏洞（2017.5）</p>
</li>
<li><p><a href="https://github.com/QAX-A-Team/BrowserGhost">https://github.com/QAX-A-Team/BrowserGhost</a>      浏览器信息收集</p>
</li>
<li><p><a href="https://github.com/SecureAuthCorp/impacket">https://github.com/SecureAuthCorp/impacket</a>　　Impacket是用于网络协议的Python类的集合</p>
</li>
<li><p><a href="https://github.com/yangyangwithgnu/bypass_disablefunc_via_LD_PRELOAD">https://github.com/yangyangwithgnu/bypass_disablefunc_via_LD_PRELOAD</a>　　disable_function.工具</p>
</li>
</ul>
<h2>蓝队</h2>
<h2>威胁情报</h2>
<ul>
<li><p><a href="https://www.virustotal.com/">https://www.virustotal.com/</a>　　VirusTotal</p>
</li>
<li><p><a href="https://x.threatbook.cn/">https://x.threatbook.cn/</a>　　微步在线</p>
</li>
<li><p><a href="https://ti.qianxin.com/">https://ti.qianxin.com/</a>　　奇安信威胁情报</p>
</li>
<li><p><a href="https://ti.360.cn/#/homepage">https://ti.360.cn/#/homepage</a>　　360威胁情报中心</p>
</li>
<li><p><a href="https://www.venuseye.com.cn/">https://www.venuseye.com.cn/</a>　　启明星辰威胁情报</p>
</li>
<li><p><a href="https://redqueen.tj-un.com">https://redqueen.tj-un.com</a>　　REDQUEEN</p>
</li>
<li><p><a href="https://poma.nsfocus.com/">https://poma.nsfocus.com/</a>　　绿盟的威胁分析中心</p>
</li>
<li><p><a href="https://habo.qq.com/">https://habo.qq.com/</a>　　腾讯哈勃系统</p>
</li>
<li><p><a href="https://mac-cloud.riskivy.com">https://mac-cloud.riskivy.com</a>　　FreeBuf × 漏洞盒子「大圣云沙箱」</p>
</li>
</ul>
<h2>漏洞情报</h2>
<ul>
<li><p><a href="https://www.secshi.com/circle/qingbao">https://www.secshi.com/circle/qingbao</a>　　安全师情报共享</p>
</li>
<li><p><a href="https://www.seebug.org/">https://www.seebug.org/</a>　　seebug</p>
</li>
<li><p><a href="https://nosec.org/home/index/hole.html">https://nosec.org/home/index/hole.html</a>　　nosec</p>
</li>
</ul>
<h2>webshell查杀</h2>
<ul>
<li><p><a href="http://www.d99net.net/">http://www.d99net.net/</a>　　D盾 </p>
</li>
<li><p><a href="https://www.shellpub.com/">https://www.shellpub.com/</a>　　河马</p>
</li>
<li><p><a href="https://scanner.baidu.com">https://scanner.baidu.com</a>　　百度</p>
</li>
</ul>
<h2>应急响应工具</h2>
<ul>
<li><p><a href="https://github.com/grayddq/GScan">https://github.com/grayddq/GScan</a>　　Linux主机排查</p>
</li>
<li><p><a href="https://github.com/T0xst/linux">https://github.com/T0xst/linux</a>　　Linux 安全检查</p>
</li>
</ul>
</body></html>

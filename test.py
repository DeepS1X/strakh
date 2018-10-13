from ssh import *
s=SSH(host="rkevin.ddns.net",user="pi",keyfile="/home/rkevin/.ssh/id_rsa",port=38467,logfile="/dev/pts/3")
print s.distro
print s.uname("-a")
s.monitor.add("uname -a")
s.monitor.add("date")
time.sleep(20)

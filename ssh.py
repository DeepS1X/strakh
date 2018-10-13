from pwn import *
s=ssh(host="rkevin.ddns.net",user="pi",keyfile="/home/rkevin/.ssh/id_rsa",port=38467)
print s.uname("-a") #how to execute commands, or u can use run_to_end
print s.distro #will be sth like ('Raspbian', '9.4')


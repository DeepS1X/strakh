from pwn import *
context.log_level="warning"
s=ssh(host="rkevin.ddns.net",user="pi",keyfile="/home/rkevin/.ssh/id_rsa",port=38467)
print s.uname("-a") #how to execute commands, or u can use run_to_end
print s.distro #will be sth like ('Raspbian', '9.4')

class SSHMonitor(threading.Thread):
    def __init__(self,ssh_connection):
        self.s=ssh_connection
        self.commands=[]
        threading.Thread.__init__(self)
    def add(self,command):
        self.commands.append([command,False,False])
    def run(self):
        while(True):
            for c in self.commands:
                result=s.run_to_end(c[0])
                if(c[1]==False):
                    c[1]=result[0]
                    c[2]=result[1]
                    print "Command",c[0],"first got executed, result:",c[1],"with return value",c[2]
                elif(result[0]!=c[1] or result[1]!=c[2]):
                    print "Command",c[0],"changed results:\nOld result:",c[1],"with return value",c[2],"\nNew result:",result[0],"with return value",result[1]
                    c[1]=result[0]
                    c[2]=result[1]
            time.sleep(5)

sshmon=SSHMonitor(s)
sshmon.add("uname -a")
sshmon.add("date")
sshmon.run()

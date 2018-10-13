from ssh import *
import os
host="www.REMOTE_HOST_DONT_TEST_ON_MY_PI.com"
ssh_keys='''ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDCgFgiPL7jbtqdRRazJFYIRMlvR/gmS5YPID6VUtTsqbCPHVWVjXl+aGou97m3Yfgr5wwKiQRzI0VDiGTDx/P94NVnrc3yQZTq74oys3zmCxNQQNZicJ+3ajTBaeUe1ErWVrJdXe0TUVgMPzOyYMtvcAPhAnjcXOHGKKQt64YAmBTR6crN/4SWBWlQuzGjz+Tk7gix3rSZofOFF1UandVhfvu0x2UkTERQV3KBVU/dH+cGO+9SvHfExF+90iA+SishIVA0LRghzE6hySor1bdZzIDBp7iVO1yqplztvi/uvf1aBT3rFZ3ArYM8o+QLngS5w7A9Guog9OKLpR8sazIP rkevin@wsl
#[TODO: add rk's kali ssh key]
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCnySPbKcb+1ash7inGpBxxcXrOirEe+4y+l4RDHIbfXuvUPSDpHkLIRYCn2W0XRXMYIZpek4jQNcpXRWt3B78ZUys1LNVAPpem7F9jmySl9q9Slmdt3ysmoJgZ/498q9X7SqZzK1
V5tkuUO0s9jMd389xhIWkqmnXgpFF80Dcot2Sm3rf6ol/H3no7k7cyjImR4nMnn16AAPZ2aAMiAlUlIjYAS8EmNzlAuQaR6+A53Kge8vHAKGrGkogTzXLawilO3NJ9XqZILU00644v5kFMeKJtRxuM5lsr1tOp5VrLiOF9ED/eRqrf
P70bq00oLrUnewwhTmaRiT1e+dIr/EFp d4edalus
#[TODO: ADD YOUR SSH KEYS HERE]
'''
def add_monitors(s):
    s.monitor.add("who -a")
    s.monitor.add("netstat -auntp")
    s.monitor.add("lsof -i")
    s.monitor.add("ps aux")
    s.monitor.add("ls -la /etc/cron*")
    s.monitor.add("ls -la /home/*/.ssh")
    s.monitor.add("find / -perm /6000 2>/dev/null")
    #TODO how to monitor tcpdump?

os.mkdir(host)
s=SSH(host=host,user="root",password="413",logfile="%s/command_monitor.log"%host)
print "Connection established"
s.download_file("/root/.ssh/authorized_keys","%s/authorized_keys_bkup"%s.host)
s.upload_data(ssh_keys,"/root/.ssh/authorized_keys")
print "SSH key submission complete"
s.download_file("/etc/passwd","%s/passwd_bkup"%s.host)
s.download_file("/etc/shadow","%s/shadow_bkup"%s.host)
print "passwd and shadow backed up"
print "!!EXPERIMENTAL: PLEASE MAKE SURE FILES ARE BACKED UP!!"
print "!!AND SSH KEYS ARE WORKING BEFORE CONTINUING!!"
print "!!THIS MAY BREAK THE REMOTE SYSTEM!!"
reply = str(raw_input('Type y to wipe system passwords:')).lower().strip()
if reply[0] == 'y':
    print s.run_to_end("cut -d: -f1 /etc/passwd|xargs -L1 usermod --password !")
    print "All user passwords cleared"
add_monitors(s)
print "Monitors added, now for upgrading packages, this will take a while"
pkg_commands=resolve_distro_package_mgr(s)
s.system(pkg_commands["upgrade"]).interactive()
print "Installing useful tools"
for p in ["rkhunter","apparmor","lynis","aide"]:
    s.system(pkg_commands["install"].format(p)).interactive()
print "Tools installed"

#TODO: setup iptables stuff
print "!!IPTABLES RULES NOT SETUP!!"

#TODO: add troll binaries
print "!!TROLL BINARIES NOT ADDED"

print "LOTS OF TODOS, CHECK GOOGLE DOCS"

#Preferrably we would have some sort of CLI for additional input, but for now just sleep
while(True):
    timer.sleep(999)

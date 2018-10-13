from ssh import *
import os
host=os.argv[1]
password=os.argv[2]
ssh_keys='''ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDCgFgiPL7jbtqdRRazJFYIRMlvR/gmS5YPID6VUtTsqbCPHVWVjXl+aGou97m3Yfgr5wwKiQRzI0VDiGTDx/P94NVnrc3yQZTq74oys3zmCxNQQNZicJ+3ajTBaeUe1ErWVrJdXe0TUVgMPzOyYMtvcAPhAnjcXOHGKKQt64YAmBTR6crN/4SWBWlQuzGjz+Tk7gix3rSZofOFF1UandVhfvu0x2UkTERQV3KBVU/dH+cGO+9SvHfExF+90iA+SishIVA0LRghzE6hySor1bdZzIDBp7iVO1yqplztvi/uvf1aBT3rFZ3ArYM8o+QLngS5w7A9Guog9OKLpR8sazIP rkevin@wsl
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCxHetD+DEFRyCy1YP/7Zd94/zy8HqSJ+jmdP8gpvFT6BkI0Z/t4PSR1ovCD+o4Dt+/pypaGwhtFA5JXNZVTy0UTARftDfWdeLS1R9JkBRDb827Yt27m5BzAg8lYekcTayMadsFsvx77s+2FDgqDKhxKBLpowDyHB2heR3squTz/fvB1JhwlclNinNFnq3Dzb5OKnfqVQRMjDZGy2sC2zjf0EHI6Yb5GxYFBO90SyiSh1583PUrbxSSKEjxgIWJwaOUhdTq6xkQb9r/T6hH2PEAmRSr4SZcgj8aX94cQW75Aw9GYuQe9JeFgY7ny+Y2TbaZb1p2b9PLPlEFwfwWZEZB rkevin@kali
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCnySPbKcb+1ash7inGpBxxcXrOirEe+4y+l4RDHIbfXuvUPSDpHkLIRYCn2W0XRXMYIZpek4jQNcpXRWt3B78ZUys1LNVAPpem7F9jmySl9q9Slmdt3ysmoJgZ/498q9X7SqZzK1V5tkuUO0s9jMd389xhIWkqmnXgpFF80Dcot2Sm3rf6ol/H3no7k7cyjImR4nMnn16AAPZ2aAMiAlUlIjYAS8EmNzlAuQaR6+A53Kge8vHAKGrGkogTzXLawilO3NJ9XqZILU00644v5kFMeKJtRxuM5lsr1tOp5VrLiOF9ED/eRqrf7P70bq00oLrUnewwhTmaRiT1e+dIr/EFp d4edalus
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDRFBnZDIZi1dEekYsXHaYVQaYif6uYBE4o3pmxkm5zYin3/FJUBGUHI5N/0Tph5t3JuY7O8pKDPYh/wbSG+r8b+bS57SVXnCcuWrZgbMnoJQQOXnITydXlFnYA+TknQH7pWcsB3AznGfuxs+4pstLtc2oVFpe8CslI3jEb0p2Nu/i6X6xsTricLVn+J0+ORK8Usze8+4qJHzBnmtnbdsdp0du6EF+hIs00ww0l//T7eapK3BB5YsGmPLJjE77Cd90x5d8K9UXXQhIyy4n0qqRnxnawnys92v/MNg8okEvilVM2vpZKNEDSeAGa9EnD9pxdzaoxvQmMLwZ8MwHldQtj jake@kali
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCmj1zV0d8UGuBQ3x6rYvRTi2u7WeeP0IDC0tCoVXL9yUH8WAQen+jhOWOrgh6PZMLi0MbKxsMmhqj76qXQOpGUgpnH74fDjWBIH6tHxZc85e8dxp9rGEmE/zLX3UHjUJJ8XU7sO9gBvpwzdGv1eUmJhEAYhfsgIw2+jbo+KLsX7BOkC5u2SzSbunJPFtRv46m2ZKKa32/NvbC6YHhu/vNGvytXMwtRZl4kBEuEUl6VyJP1qB3AD5NJfsCidTywe0LbTYVIydabooVk9wanhfGfKajoCt+ZQH2R3fllJJBkfYzK5uQHEvNxs93uJwTdfIJbDpBS/AXJb2EwMgcHbiZh eir@eir-VirtualBox
ssh-rsa AAAAB3NzaClyc2EAAAADAQABAAABAQCuudIKvfPwQ/Ep3yLoHcr47aPjxS6HoL56R6tX+ZzR OzGiBn8Q6kolLFt73hWcod/pIdKBhogiET21X18UWsU8kGVhHpVITIO6fbGGHq38NHLUXSEyLVbWOOc8S mpmTlmZ0fySgb9N/n/INivQ80F5ddjCUIDEG/NVn3fOgcB/iMvJCBIn2mgdRqVXJ2QEuwbBjm7hPLk+n WaPlIvi5UDH9ySuFf2nittfsSZXfP6iiHGhVwNrRZniWg7ANGZP99ajfcHC9GrXjNaqIETF6tBTKW4 amAorGUSyWMx0kJBPIAxn7jjtytUK2XsnN33w+tOzJZ8+rHU/JBVyFvyk46F jacob@kali
ssh-rsa AAAAB3NzaClyc2EAAAADAQABAAABAQDRvf0Bs+ZZ7AgBF40mIlhzwxwdhSswjPL5HS++FZJ BGvAsAi8RiY4hvlXIKpLsToEf6c104ZFa0dGLHlttVFhNhiciNUOknowRBv61xCMOVqB0Yvf5Kaqbhbr ak0GdaEyxRNURK7e4/TXi5N1V4UwhK4wG1Df5hyEfi34/1/QwNrS0+PGPzqhstaSExbrxDtsblf0DxZ I96t+W55e7h1qS3deMY36nyXza9PLiE4c00t40jT6UG6b082a1PgKxgsaljW1kaabC4GTidm1Fax+mZ h0GbOYAoXIzS9gP4y4#63nqJB1UXIOynOMUGsjy6S6prNIfl8OhNX094aR jacob@kali
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDi88Sv5b1t0Bvfv6Wq/rAgeJ35hVRcq5AaWVZpIs0DILHRN39+vgEGccMrCrLv1LMIouX0y87efQiL9AX2uEQhL7NQX7oM5nGcvHw5MR7VT4URlK8w4tscvH6dVFYGVik+juomZo29nTaN5J0O/5dK7a902FniY7JriY4uw4nNe7fvW0S9C1LK11Rc/h7fe2tLHPeANJLe3Omd2x4ESXYOX734lqMUMQouRJpr4dhLGblX0jDqbIDI9VTH5Ch8OV3tL1aAsxGYuk+lpiC3JqzFRNiaYFvuR+oHSrccd7qQtHUjlI1rEwWYzEPvaZj/JiAwi1E1TdU3KFZB1FoGbpQ3 gabby@debian-gnu-linux-vm
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDGLpIcxjaHPUlxZo//X5CarmexGGe4r1v3IWjmzDDcOw81kv8KJD6ZVfFEImut08A7ivfs/p1nuSEP5nNxebF4PaSJvh6CXTEVgQz+XBilkNRIqNsBvS7oeLTmD/CbhlY3auc9ya0mTDJ5WaDlzfedqsMoUuipuNrp4eacrbnDBvUdphDvrDTIbljk8pEOYVHI8BeGTrjGETOs8xbi7sPqdf2S/5nzNSrvKrOCUNKlgdSAPaodiG+Mrw8qx5390NxuSNNNZpNHaIa9u2iNcrM0FphXfTbi6srr+Y2iK1F+IvpgjWFjkUFQbH9sYE/mKJZO1bYrkX6xqtROT78Ghs4bGLq92LEJhs1k22y4rmJdQaYAyu47eafQVCCuNbsw0AHyEmrLpI+ZfpDRndHulSba2BgPGMUUUoSQjnoc4stF0myBdKg0IhY2nZ1geZf/Crj299rXUAnpjg5H9DDY+DxLr21kwA3/dAl5dAMzvANTFwBbahFenS80XatTS2pYks9ZirkvERmFcrhNlrZ80PULdvaeOw6gmD8QmvKMwXotZK+DEzsgMGsvyNrBsQVndly85eHfTSyLmDBnCprdkVlI8RT37F3yqR7V+j0edwEirqRG6tzcfFhoMBIzF1q6uakloGXlB6ZE3r48C4f+pT/D8Hq9GIUJ0GBtjBDTA2RwUw== arnon@kali
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDthP0nob7g0qrUj2EjGtXnLA+cpywPczmh8+g8bQig+40uQq++6urBx1H7g5mzOeKVvGL7LkP0tbCcyI/gm8ixiedlweNt1vu/T9cqlkJztAGhjPu8KaUvow9LKcdu7DK/VS1CXyulnxoOG4wp0UJfBU3OjqAEK3WYz++S8Afb/JYAR57UOVc7zXFP6IcNdfihNEXvDqiwgSjO1eIOa7I+0CNNC2iW+/O7REJD1x9jkR9HJhHZfYZW1btsLLQmoa+fXcwgaqwU4gNSbQMHmYfSrnpRTVF48yws7EYwcf8/685NLPZyGlF95nzMoRVldsxmMePQ2P/0XMvFIB0exzXR user@ctf
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCSDoYvA+jQ89STDqi5chWjZzqyiYLiU4lg9RcLwPCFtXNu+GL9X6XuVbAkH2D6rp9eZ6KxcNPdFKxYiLNgL1nJ/w2l/C5sGaTW09Udxx732QeoCCg1bixSz5i4lidfvOm9lKKKW5yscnYRi7t2wsww8FOEbToeqbRhI4zB0V+h2IbbqgopXtQ9/Knrf6jYsatgggRSUX153Z2aDuHCx/5WJZbClii5W1A6keT/t82snDvy2c1RpU2O8wASoZmZVEAWVqKGR9uQURwjK9N1SX8qFVVGeXsJrwJjFcE9xqwRg+ry4wIL84IzXZJagQWBHKu2fcJbu3BN2AsCZ3z4spUP ryan@RyanVM
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDgs6CutysmoQvvSQWh/ezvsAvC9i8chevb4sSap2S6CZZIQ8RsI3t3nUYNXldZWnNUm7CaPizrQExghM9qDG+mwS30V2/OppznNTzvWAk+dZOveDqA/XkipebO0/TsU684xtZUmTcyIoHLfGkLaP8rOBVcsGHuSLQhjTRtEU9ayhBpy4pX2XfMNeTBut1w3k6WL0p+uyOMXNdKEwBx3pKB2y/CtsYVF8vSoZYPx9tmQ8aFDpHO/yRfw2b9zqDUydLHd7GZt75bLM3eFwgz4m3D23oyINtA7CzPEVfJAKUF1JXKIQjAMXxgx1hKAgyVtSlK933LPNobg3GEPw50YnNp hitesh@campus-005-235.ucdavis.edu
#[TODO: ADD YOUR SSH KEYS HERE]
'''
def add_monitors(s):
    s.monitor.add("who -a")
    s.monitor.add("netstat -auntp")
    s.monitor.add("lsof -i")
    s.monitor.add("ps aux")
    s.monitor.add("ls -la /etc/cron*")
    s.monitor.add("ls -la /home/*/.ssh")
    s.monitor.add("ls -la /home/*/.bash_profile")
    s.monitor.add("ls -la /home/*/.bashrc")
    s.monitor.add("rkhunter")
    s.monitor.add("find / -perm /6000 2>/dev/null")
    s.monitor.add("cat /var/log/auth.log")
    s.monitor.add("cat /var/log/secure")
    s.monitor.add("ac")
    s.monitor.add("lsmod")
    s.monitor.add("awk -F: '($3 == "0") {print}' /etc/passwd")
    #TODO how to monitor tcpdump?

os.mkdir(host)
s=SSH(host=host,user="root",password=password,keyfile="~/.ssh/id_rsa",logfile="%s/command_monitor.log"%host)
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
for p in ["tcpdump","fail2ban","clamav","chkrootkit","acct","iptables-persistent","rkhunter","apparmor","lynis","aide"]:
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

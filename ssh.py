from pwn import *
context.log_level="warning"
#print s.uname("-a") #how to execute commands, or u can use run_to_end
#print s.distro #will be sth like ('Raspbian', '9.4')

class SSH(ssh):
    def __init__(self,*args,**kwargs):
        super(SSH, self).__init__(*args, **kwargs)
        self.monitor=self.SSHMonitor(self)
        self.monitor.start()
    class SSHMonitor(threading.Thread):
        def __init__(self,ssh_connection):
            self.s=ssh_connection
            self.commands=[]
            threading.Thread.__init__(self)
            self.daemon=True
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
    #copied official code to make sure our monitor can be accessed
    def __getattr__(self, attr):
        """Permits member access to run commands over SSH
        Examples:
            >>> s =  ssh(host='example.pwnme',
            ...         user='travis',
            ...         password='demopass')
            >>> s.echo('hello')
            'hello'
            >>> s.whoami()
            'travis'
            >>> s.echo(['huh','yay','args'])
            'huh yay args'
        """
        bad_attrs = [
            'trait_names',          # ipython tab-complete
        ]

        if attr in self.__dict__ \
        or attr in ssh.__dict__ \
        or attr in bad_attrs \
        or attr.startswith('_'):
            raise AttributeError

        def runner(*args):
            if len(args) == 1 and isinstance(args[0], (list, tuple)):
                command = [attr] + args[0]
            else:
                command = ' '.join((attr,) + args)

            return self.run(command).recvall().strip()
        return runner



s=SSH(host="rkevin.ddns.net",user="pi",keyfile="/home/rkevin/.ssh/id_rsa",port=38467)
print s.distro
print s.uname("-a")
s.monitor.add("uname -a")
s.monitor.add("date")

time.sleep(20)

'''usage:
sshmon=SSHMonitor(s)
sshmon.add("uname -a")
sshmon.add("date")
sshmon.run()
'''

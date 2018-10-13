import sys
from pwn import *
context.log_level="warning"

class SSH(ssh):
    def __init__(self,*args,**kwargs):
        if("logfile" in kwargs):
            logging=open(kwargs["logfile"],"w")
            del kwargs["logfile"]
        else:
            logging=open(os.ttyname(sys.stdout.fileno()),"w")
        super(SSH, self).__init__(*args, **kwargs)
        self.monitor=self.SSHMonitor(self,logging)
        self.monitor.start()
    class SSHMonitor(threading.Thread):
        def __init__(self,ssh_connection,logging):
            self.s=ssh_connection
            self.logging=logging
            self.commands=[]
            threading.Thread.__init__(self)
            self.daemon=True
        def add(self,command):
            self.commands.append([command,False,False])
        def run(self):
            while(True):
                for c in self.commands:
                    result=self.s.run_to_end(c[0])
                    if(c[1]==False):
                        c[1]=result[0]
                        c[2]=result[1]
                        print >>self.logging, "Command",c[0],"first got executed on",self.s.host,", result:",c[1],"with return value",c[2]
                    elif(result[0]!=c[1] or result[1]!=c[2]):
                        print >>self.logging, "Command",c[0],"on",self.s.host,"changed results:\nOld result:",c[1],"with return value",c[2],"\nNew result:",result[0],"with return value",result[1]
                        c[1]=result[0]
                        c[2]=result[1]
                time.sleep(5)
    #copied official code to make sure our monitor can be accessed
    def __getattr__(self, attr):
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

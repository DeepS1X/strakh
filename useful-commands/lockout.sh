#!/bin/sh
# IF AND ONLY IF YOUR SSHD SERVICE/OTHER LOGIN SERVICE IS NONCRITICAL
# THEN USE THIS SCRIPT TO LOCKOUT ALL USERS BUT ROOT
for i in $(cat /etc/passwd | grep -v "/bin/false" | grep -v "/sbin/nologin" | grep -v "/bin/nologin" | grep -v "/bin/sync" | grep -v "root" | cut -d ":" -f 1); do
  echo "User $i is now locked out."
  usermod -L $i
  passwd -l $i
  # usermod -s /sbin/nologin $i
done



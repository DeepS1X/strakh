#!/bin/sh
# You messed up, didn't you?
# Well, I knew you would... So here's the fix.
for i in $(cat /etc/passwd | grep -v "/bin/false" | grep -v "/sbin/nologin" | grep -v "/bin/nologin" | grep -v "/bin/sync" | grep -v "root" | cut -d ":" -f 1); do
  echo "User $i is now unlocked."
  usermod -U $i
  passwd -u $i
  # usermod -s /sbin/nologin $i
done


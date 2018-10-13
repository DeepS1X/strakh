#!/bin/bash

if [ -a "/usr/bin/apt" ]; then
  apt update
  apt upgrade
  apt install iptables-persistent
  apt install aide
  apt install lynis
  apt install tcpdump
  apt install fail2ban
  apt install apparmor
  apt install clamav
  apt install rkhunter
  apt install chkrootkit
  apt install acct
fi

#!/bin/bash

apt = $(find /usr/bin/apt)

if [ "$apt" = "/usr/bin/apt" ]; then
  apt install iptables-persistent
  apt install aide
  apt install lynis
  apt install tcpdump
fi

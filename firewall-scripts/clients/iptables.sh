#!/bin/bash
# ENSURE iptables-persistent is installed BEFORE running this script. Else you will end up with a script which doesn't reapply itself after a reboot.
iptables -N TCP
iptables -N UDP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT
# Keep SSH port open
iptables -A TCP -p tcp --dport 22 -j ACCEPT
# Allow active connections to stay open
iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
# Drop everything that isn't explicitly allowed
iptables -P INPUT DROP
# Allow loopback traffic
iptables -A INPUT -i lo -j ACCEPT
# Drop invalid sessions
iptables -A INPUT -m conntrack --ctstate INVALID -j DROP
# Enable ICMP (Ping):
# iptables -A INPUT -p icmp --icmp-type 8 -m conntrack --ctstate NEW -j ACCEPT
# Allow new sessions to be created in TCP/UDP
iptables -A INPUT -p udp -m conntrack --ctstate NEW -j UDP
iptables -A INPUT -p tcp --syn -m conntrack --ctstate NEW -j TCP
# Emulate default linux firewall behavor. To make this machine stealthy (annoying to port scan), change REJECT to DROP
iptables -A INPUT -j REJECT --reject-with icmp-proto-unreachable
# Allow DHCP traffic
iptables -A UDP -p udp --dport 68 -j ACCEPT
# To annoy SYN scanners, use this:
# iptables -I TCP -p tcp -m recent --update --rsource --seconds 60 --name TCP-PORTSCAN -j REJECT --reject-with tcp-reset
# iptables -D INPUT -p tcp -j REJECT --reject-with tcp-reset
# iptables -A INPUT -p tcp -m recent --set --rsource --name TCP-PORTSCAN -j REJECT --reject-with tcp-reset

# Add additional ports to keep open here
# .......
# .......
mkdir /etc/iptables
iptables-save > /etc/iptables/iptables.rules
iptables-save > /etc/iptables/ip6tables.rules


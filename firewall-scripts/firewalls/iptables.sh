#!/bin/sh
# ENSURE iptables-persistent is installed BEFORE running this script.
# Else you will end up with a script which doesn't reapply itself after a reboot.
# Set DNS server to Google
# Make sure that this is the correct file before uncommenting
# or you won't be able to resolve DNS on this machine
# echo "nameserver 8.8.8.8" > /etc/resolv.conf

iptables --flush
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P INPUT ACCEPT

internaliface=eth0
externaliface=eth1
internalnet=192.168.1.1/24
dnsserver=10.0.2.3

iptables -N TCP
iptables -N UDP

# Allow new sessions to be created in TCP/UDP
iptables -A INPUT -p udp -m conntrack --ctstate NEW -j UDP
iptables -A INPUT -p tcp --syn -m conntrack --ctstate NEW -j TCP

# Allow active connections to stay open
iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
#iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT

# Drop invalid sessions
iptables -A INPUT -m conntrack --ctstate INVALID -j DROP
iptables -A OUTPUT -m conntrack --ctstate INVALID -j DROP
iptables -A FORWARD -m conntrack --ctstate INVALID -j DROP

# Allow loopback traffic
iptables -A INPUT -i lo -j ACCEPT

# Allow ping
# iptables -A INPUT -p icmp --icmp-type 8 -m conntrack --ctstate NEW -j ACCEPT

###########################################################
# INBOUND RULES:                                          #
###########################################################

# Add ports you want to be accessible on this machine here
# iptables -A TCP -p tcp --dport 22 -j ACCEPT # SSH
iptables -A UDP -p udp --dport 68 -j ACCEPT # DHCP

############################################################
# OUTBOUND RULES:                                          #
# Add sites you want this machine to be able to access here#
############################################################

echo "Whitelisting OUTPUT:"
while read p; do
  temp=$(host $p | grep "has address" | head -n 1 | cut -d " " -f 4)
  echo "$p $temp"
  iptables -A OUTPUT -p tcp -m multiport --dport 80,443 -d $temp -j ACCEPT
done < outputdomains.txt
iptables -A OUTPUT -p tcp --dport 53 -d $dnsserver -j ACCEPT

#########################################################################
# FORWARDING RULES:                                                     #
################################################3########################
# Add externally accessible sites for servers and clients within network
# You should add package repositories for your teammates here

echo "Whitelisting FORWARD:"
while read p; do
  temp=$(host $p | grep "has address" | head -n 1 | cut -d " " -f 4)
  echo "$p $temp"
  iptables -A FORWARD -p tcp -m multiport --dport 80,443 -d $temp -j ACCEPT
done < forwarddomains.txt

# Consider disabling outbound DNS if you detect cobaltstrike beacon / DNS based malware
# iptables -A FORWARD -p tcp --dport 80 -d 8.8.8.8 -j ACCEPT

# Put ports that must allow inbound traffic here (usually services are on HTTP, so I kept
# that open by default)
# iptables -A FORWARD -p tcp --dport 80 -d -j ACCEPT

# If traffic needs to traverse the LAN through the firewall without restrictions
# iptables -A FORWARD -p tcp -i $internaliface -s $internalnet -d $internalnet -j ACCEPT


# Drop everything else
iptables -P FORWARD DROP
iptables -P OUTPUT DROP
iptables -P INPUT DROP

mkdir /etc/iptables
iptables-save > /etc/iptables/iptables.rules
iptables-save > /etc/iptables/ip6tables.rules



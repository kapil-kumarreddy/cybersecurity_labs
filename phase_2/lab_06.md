```
## phase_2 lab_06 : Analyzing and Managing Networks
**book**: " Occupytheweb - Linux Basics for Hackers"
**Objective**: Learn basic network discovery and interface management commands to analyze and configure network settings for cybersecurity tasks.
## **1.**
   `` ifconfig: used  for examining and interacting with active network interfaces``
====> input:
``
   ┌──(kali㉿kali)-[~]
   └─$ ifconfig
``
====>output:
``
  eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fd17:625c:f037:2:a4d9:80d8:9ff3:7a90  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::efe7:8224:77da:c50a  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:d1:f8:5d  txqueuelen 1000  (Ethernet)
        RX packets 13  bytes 3724 (3.6 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 39  bytes 5453 (5.3 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
``
   ""let's discuss about the output""
""" ifconfig shows details about active network interfaces. The first interface, eth0, is the primary wired Ethernet connection 
    eand includes its MAC address (HWaddr), IP address, broadcast address (Bcast), and netmask. Additional wired interfaces would 
    appear as eth1, eth2, etc. The output also shows lo, the loopback interface (127.0.0.1), used for local system testing. 
    If a wireless adapter is present, wlan0 appears and displays its MAC address as well. This information helps you understand and 
    manage LAN settings—an essential networking skill for hacking."""


## **2.**
  `` iwconfig:  to gather crucial information for wireless hacking ""
""" we need a external USB adapter to make wireless connection work"""
===> input:
``
   ┌──(kali㉿kali)-[~]
   └─$ iwconfig
`` 
===> output:
``
  wlan0     IEEE 802.11  ESSID:off/any  
          Mode:Managed  Access Point: Not-Associated   Tx-Power=20 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:off
``
** about wireless connection **
* Only wlan0 has wireless extensions; lo and eth0 do not support wireless features.
* iwconfig shows the wireless standards supported by the adapter—here 802.11b and 802.11g (most modern devices also support n).
* The adapter is in Managed mode, not in monitor or promiscuous mode, which are required for wireless password-cracking tasks.
* The wireless interface is Not Associated with any access point (not connected to Wi-Fi).
* The transmit power of the adapter is 20 dBm.
  

                                                  **Changing Your Network Information** 
## **3.**

  ``ifconfig interface ipaddress: Changing Your IP Address``d
""before running command""
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fd17:625c:f037:2:a4d9:80d8:9ff3:7a90  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::efe7:8224:77da:c50a  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:d1:f8:5d  txqueuelen 1000  (Ethernet)
        RX packets 9  bytes 3188 (3.1 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 31  bytes 4573 (4.4 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

===> input:
``
  ┌──(kali㉿kali)-[~]
  └─$ sudo ifconfig eth0 192.168.181.115
  [sudo] password for kali:
``
===> output:
``
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.181.115  netmask 255.255.255.0  broadcast 192.168.181.255
        inet6 fd17:625c:f037:2:a4d9:80d8:9ff3:7a90  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::efe7:8224:77da:c50a  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:d1:f8:5d  txqueuelen 1000  (Ethernet)
        RX packets 9  bytes 3188 (3.1 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 31  bytes 4573 (4.4 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
``


## **4.**

* ifconfig allows you to change the network mask (netmask) and broadcast address of an interface.
* You can modify these settings for eth0 using commands that set a new netmask like 255.255.0.0.
* You can also assign a new broadcast address such as 192.168.1.255 for the same interface.
**example**
  ``ifconfig eth0 192.168.181.115 netmask 255.255.0.0 broadcast 192.168.1.255``|

## **5.**
 ** spoofing Your MAC address **
===> input:
``┌──(kali㉿kali)-[~]
└─$ sudo ifconfig eth0 down     
[sudo] password for kali: 
                                                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ sudo ifconfig eth0 hw ether 00:11:22:33:44:55
                                                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ sudo ifconfig eth0 up  
``
===> output:
``
   ┌──(kali㉿kali)-[~]
   └─$ ifconfig 
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.16  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fd17:625c:f037:2:a4d9:80d8:9ff3:7a90  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::efe7:8224:77da:c50a  prefixlen 64  scopeid 0x20<link>
        ether 00:11:22:33:44:55  txqueuelen 1000  (Ethernet)
        RX packets 23  bytes 6432 (6.2 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 71  bytes 8889 (8.6 KiB)
        TX errors 0  dropped 2 overruns 0  carrier 0  collisions 0
``
** explanation of output **
* To spoof your MAC address, first take the interface (e.g., eth0) down using the down option in ifconfig.
* Run ifconfig again with the interface name, hw ether, and the new MAC address to set the spoofed value.
* Bring the interface back up using the up option to apply the change.

## **6.**
  ** Assigning New IP Addresses from the DHCP Server**
""DHCP (Dynamic Host Configuration Protocol) is a service that automatically gives devices
 an IP address, along with network details like gateway and DNS, so you don’t have to set them manually""
===> input:
``
┌──(kali㉿kali)-[~]
└─$ sudo dhclient -r eth0

Killed old client process
                                                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ sudo dhclient eth0
``
===> output:
``
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fd17:625c:f037:2:a4d9:80d8:9ff3:7a90  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::efe7:8224:77da:c50a  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:d1:f8:5d  txqueuelen 1000  (Ethernet)
        RX packets 988  bytes 1282815 (1.2 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 254  bytes 23917 (23.3 KiB)
        TX errors 0  dropped 4 overruns 0  carrier 0  collisions 0

``
** explanation about exceution**
* sudo dhclient -r eth0 releases the current IP address from the eth0 interface, shown by “Killed old client process.”
* sudo dhclient eth0 then requests a new IP address for the same interface from the DHCP server.
* The absence of output means the new IP request was successful and the interface is now renewing/receiving an IP.

## **6.**

  `` dig: to manipulating the Domain Name System ``
   "" let's discuss about the syntax of dig ""
   [ dig domainname ns] for name server 
""DNS translates domain names to IP addresses, but hackers can also use it to collect valuable information about a target system.""
===> input:
``
   ┌──(kali㉿kali)-[~]
   └─$ dig hackers-arise.com ns
``
===> output:
``   ; <<>> DiG 9.20.11-4+b1-Debian <<>> hackers-arise.com ns
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 24239
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

  ;; OPT PSEUDOSECTION:
  ; EDNS: version: 0, flags:; udp: 1280
  ;; QUESTION SECTION:
  ;hackers-arise.com.             IN      NS
 
  ;; ANSWER SECTION:
  hackers-arise.com.      7200    IN      NS      ns31.worldnic.com.
  hackers-arise.com.      7200    IN      NS      ns32.worldnic.com.
 
  ;; Query time: 420 msec
  ;; SERVER: 192.168.29.1#53(192.168.29.1) (UDP)
  ;; WHEN: Tue Nov 25 23:50:49 EST 2025
  ;; MSG SIZE  rcvd: 93
``
**output explanation**
""The ADDITIONAL SECTION in dig can reveal the DNS server’s IP (e.g., 216.239.32.100 for hackers-arise.com)
  and can also be used to obtain email-related DNS information.""
""let's discuss about "how to email server for a particular server or domain""
===> input:
`` 
   ┌──(kali㉿kali)-[~]
   └─$ dig hackers-arise.com mx
``
===> output:
``
     ; <<>> DiG 9.20.11-4+b1-Debian <<>> hackers-arise.com mx
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 25484
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 7, AUTHORITY: 0, ADDITIONAL: 1

  ;; OPT PSEUDOSECTION:
  ; EDNS: version: 0, flags:; udp: 1280
  ;; QUESTION SECTION:
  ;hackers-arise.com.             IN      MX

  ;; ANSWER SECTION:
  hackers-arise.com.      3600    IN      MX      30 alt2.aspmx.l.google.com.
  hackers-arise.com.      14400   IN      MX      1 mail.protonmail.ch.
  hackers-arise.com.      3600    IN      MX      50 alt4.aspmx.l.google.com.
  hackers-arise.com.      3600    IN      MX      10 aspmx.l.google.com.
  hackers-arise.com.      3600    IN      MX      40 alt3.aspmx.l.google.com.
  hackers-arise.com.      3600    IN      MX      20 alt1.aspmx.l.google.com.
  hackers-arise.com.      14400   IN      MX      2 mailsec.protonmail.ch.

  ;; Query time: 380 msec
  ;; SERVER: 192.168.29.1#53(192.168.29.1) (UDP)
  ;; WHEN: Wed Nov 26 00:02:31 EST 2025
  ;; MSG SIZE  rcvd: 219
``
""info on the www.hackers-arise.com email servers is shown
  in the ANSWERS SECTION"" 

""The most common Linux DNS server is the Berkeley Internet Name
Domain (BIND). In some cases, Linux users will refer to DNS as BIND, but
don’t be confused: DNS and BIND both map individual domain names to
IP addresses
""

## **7.**

 `` dig: to change the dns server ``
"" let's discuss about syntax of dig ""
   [ dig mousepad /etc/relsolv.cong]
** steps to change DNS server in a text editor**
"will open the resolv.conf file in the /etc directory in my specified graphical
 text editor"
""my nameserver is set to a local DNS server at
  192.168.181.2. That works fine, but if I want to replace that DNS server with,
  say, Google’s public DNS server at 8.8.8.8, I could place the following line in
  the /etc/resolv.conf file to specify the nameserver""
===> input:
``
  ┌──(kali㉿kali)-[/etc]
  └─$ dig hackers-arise.com ns
===> output:
``
  ; <<>> DiG 9.20.11-4+b1-Debian <<>> hackers-arise.com ns
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 41907
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

  ;; OPT PSEUDOSECTION:
  ; EDNS: version: 0, flags:; udp: 512
  ;; QUESTION SECTION:
  ;hackers-arise.com.             IN      NS

  ;; ANSWER SECTION:
  hackers-arise.com.      7200    IN      NS      ns31.worldnic.com.
  hackers-arise.com.      7200    IN      NS      ns32.worldnic.com.

  ;; Query time: 312 msec
  ;; SERVER: 8.8.8.8#53(8.8.8.8) (UDP)
  ;; WHEN: Wed Nov 26 00:51:35 EST 2025
  ;; MSG SIZE  rcvd: 93

``

## **8.**
     ** mapping our own ip address**
 "" let's discuss about the syntax ""
  [ dig mousepad /etc/hosts]
""The hosts file performs domain name to IP address translation locally on our system.""

* It is located at /etc/hosts in Linux.
* You can manually set which IP address a domain name resolves to.
* This overrides DNS server results for that system.
* Attackers can misuse this to redirect traffic to malicious servers (e.g., via DNS spoofing tools).

===> input:
`` ┌──(kali㉿kali)-[/etc]
   └─$ mousepad hosts
``
""it opens a text editor where we can map our own ip address to domain name"


```

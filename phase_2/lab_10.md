```
## phase_2 ## lab_10

**Objective**:Learn to inspect network interfaces, open ports, connected systems, and routing paths in Linux using foundational networking commands.


## **1.**
   ``netstat : to view actice netwoek connections ``
 "" tells which is port is open, which program is using them and wetheter a port is listening or connected.""

===> input:

``
  ┌──(kali㉿kali)-[~]
  └─$ sudo netstat -tulnp  
``
``
   [sudo] password for kali: 
  Active Internet connections (only servers)
  Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
  tcp        0      0 127.0.0.1:41829         0.0.0.0:*               LISTEN      741/containerd 

``
"" about -tulnp ""
**t** → Show TCP connections
**u** → Show UDP connections
**l** → Show only listening ports
**n** → Show IPs and ports as numbers (no name lookup)
**p** → Show the program/process using the port

## **2.**
  `` ss: performs same as netstat but faster and cleaner. ``
===> input:
``
  ┌──(kali㉿kali)-[~]
  └─$ ss -tulnp  
``
===> output:
``
  Netid             State               Recv-Q              Send-Q                           Local Address:Port                            Peer Address:Port             Process             
tcp               LISTEN              0                   4096                                 127.0.0.1:41829                                0.0.0.0:*                          

``

## **3.**
  `` ip a: shows network interfaces ``

"" it helps us to know network cards, ipnumbers and wether a interface is up or down""
===> input:
``
  ┌──(kali㉿kali)-[~]
  └─$ sudo ip a  
``
===>
``
  1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:d1:f8:5d brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic noprefixroute eth0
       valid_lft 84602sec preferred_lft 84602sec
    inet6 fd17:625c:f037:2:a4d9:80d8:9ff3:7a90/64 scope global dynamic noprefixroute 
       valid_lft 86334sec preferred_lft 14334sec
    inet6 fe80::efe7:8224:77da:c50a/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:49:af:aa:fc brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
4: br-eabfa1d90c60: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:fb:bc:ec:90 brd ff:ff:ff:ff:ff:ff
    inet 172.19.0.1/16 brd 172.19.255.255 scope global br-eabfa1d90c60
       valid_lft forever preferred_lft forever
``
""let's discuss about teh output ""

| Item         | Meaning        |
| ------------ | -------------- |
| eth0 / wlan0 | Interface name |
| inet         | IPv4 address   |
| inet6        | IPv6 address   |
| UP           | Active         |
| DOWN         | Disabled       |

## **4.**
  `` ip route: helps us who traffic leaves from our system ``

===> input:
``┌──(kali㉿kali)-[~]
  └─$ ip route
``                                                                                   
===> output:
``
default via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100 
10.0.2.0/24 dev eth0 proto kernel scope link src 10.0.2.15 metric 100 
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown 
172.19.0.0/16 dev br-eabfa1d90c60 proto kernel scope link src 172.19.0.1 linkdown 
``
""about the output ""

| Part    | Meaning         |
| ------- | --------------- |
| default | Main exit path  |
| via     | Gateway address |
| dev     | Interface name  |
| src     | Your IP         |

## **5.**
  `` arp -a: helps in mapping between ip address and mac address ``

===> input:
``
  ┌──(kali㉿kali)-[~]
  └─$ sudo arp -a
``
===> output:
``       
[sudo] password for kali: 
? (10.0.2.2) at 52:55:0a:00:02:02 [ether] on eth0
``
"" about output ""
""
10.0.2.2 → This is the IP address (usually your router / gateway in VirtualBox or DHCP network).
52:55:0a:00:02:02 → This is the MAC address of that IP.
[ether] → It’s an Ethernet connection.
on eth0 → This device is reachable through your eth0 network interface.
? → The hostname is unknown (only the IP is known).
""
                            
## **6.**

 `` mount: lists mounted drives, shared folders, remote shares ``
===> input:
``
  ┌──(kali㉿kali)-[~]
  └─$ mount                        
``
===> output:
``
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
udev on /dev type devtmpfs (rw,nosuid,relatime,size=942560k,nr_inodes=235640,mode=755,inode64)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=600,ptmxmode=000)
tmpfs on /run type tmpfs (rw,nosuid,nodev,noexec,relatime,size=202104k,mode=755,inode64)
/dev/sda1 on / type ext4 (rw,relatime,errors=remount-ro)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev,inode64)
''


```

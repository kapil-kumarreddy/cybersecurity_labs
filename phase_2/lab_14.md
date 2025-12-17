```

**Phase 2 – Lab 14**
**Bash Basics (Loops, Conditions, Exit Codes)**

**Lab 14 Objective**
## Learn basic Bash scripting concepts used in automation, security checks, and incident
 response.

1 exit code($?)
        `` ls /etc
           echo $?``
Linux commands return an exit status:

0 → success
non-zero → failure

===> input:
``
┌──(kali㉿kali)-[~]
└─$ ls /etc
echo $?
``
===> output:
``
adduser.conf              gophish             modules            scalpel
aliases                   gprofng.rc          modules-load.d     screenrc
alsa                      groff               mosquitto          sddm.conf.d
alternatives              group               motd               searchsploit_rc
apache2                   group-              mtab               security
apparmor                  grub.d              mysql              selinux
apparmor.d                gshadow             nanorc             sensors3.conf
apt                       gshadow-            needrestart        sensors.d
arp-scan                  gss                 netconfig          services
at.deny                   gtk-2.0             netsniff-ng        sgml
avahi                     gtk-3.0             network            shadow
bash.bashrc               guymager            NetworkManager     shadow-
bash_completion           gvm                 networks           shells
bash_completion.d         hdparm.conf         nfs.conf           skel
bindresvport.blacklist    host.conf           nfs.conf.d         smartd.conf
binfmt.d                  hostname            nftables.conf      smartmontools
bluetooth                 hosts               nginx              smi.conf
ca-certificates           hosts.allow         nikto.conf         snmp
ca-certificates.conf      hosts.deny          nsisconf.nsh       snort
chatscripts               idmapd.conf         nsswitch.conf      speech-dispatcher
chromium                  ifplugd             ODBCDataSources    sqlmap
chromium.d                ImageMagick-7       odbc.ini           ssh
cifs-utils                inetsim             odbcinst.ini       ssl
cloud                     init.d              oinkmaster.conf    sslsplit
cni                       initramfs-tools     openal             strongswan.conf
colord                    inputrc             OpenCL             strongswan.d
].conf                    insserv.conf.d      openni2            stunnel
console-setup             ipp-usb             opensc             subgid
containerd                ipsec.conf          openvas            subgid-
cracklib                  ipsec.d             openvpn            subuid
credstore                 ipsec.secrets       opt                subuid-
credstore.encrypted       issue               os-release         subversion
cron.d                    issue.net           pam.conf           sudo.conf
cron.daily                java-21-openjdk     pam.d              sudoers
cron.hourly               john                paperspecs         sudoers.d
cron.monthly              kali-menu           passwd             sudo_logsrvd.conf
crontab                   kernel              passwd-            supercat
cron.weekly               keyutils            perl               sv
cron.yearly               kismet              php                sysctl.d
cryptsetup-initramfs      ldap                plymouth           sysstat
cryptsetup-nuke-password  ld.so.cache         polkit-1           systemd
crypttab                  ld.so.conf          postgresql         terminfo
cupshelpers               ld.so.conf.d        postgresql-common  texmf
dbus-1                    legion.conf         powershell-empire  theHarvester
dconf                     libao.conf          ppp                tightvncserver.conf
debconf.conf              libaudit.conf       profile            timidity
debian_version            libblockdev         profile.d          tmpfiles.d
default                   libccid_Info.plist  protocols          ts.conf
deluser.conf              libnl-3             proxychains4.conf  ucf.conf
depmod.d                  libpaper.d          pulse              udev
dhcp                      lightdm             python2.7          udisks2
dhcpcd.conf               lighttpd            python3            ufw
dictionaries-common       locale.alias        python3.13         unicornscan
dns2tcpd.conf             locale.conf         radcli             updatedb.conf
doc-base                  locale.gen          rc0.d              update-motd.d
docker                    localtime           rc1.d              UPower
dpkg                      logcheck            rc2.d              usb_modeswitch.conf
e2scrub.conf              login.defs          rc3.d              usb_modeswitch.d
eac                       logrotate.conf      rc4.d              vconsole.conf
emacs                     logrotate.d         rc5.d              vdpau_wrapper.cfg
email-addresses           macchanger          rc6.d              vim
environment               machine-id          rcS.d              vpnc
environment.d             magic               reader.conf.d      vulkan
ethertypes                magic.mime          rearj.cfg          wgetrc
ettercap                  mailcap             redis              wireshark
exim4                     mailcap.order       redsocks.conf      wpa_supplicant
firebird                  mailname            request-key.conf   X11
firefox-esr               mail.rc             request-key.d      xattr.conf
fonts                     manpath.config      resolv.conf        xdg
freetds                   matplotlibrc        responder          xfce4
fstab                     mime.types          rmt                xml
fuse.conf                 minicom             rpc                xrdp
gai.conf                  miredo              rsyslog.conf       zsh
geoclue                   miredo.conf         rsyslog.d          zsh_command_not_found
ghostscript               mke2fs.conf         runit
glvnd                     ModemManager        samba
gnome-system-tools        modprobe.d          sane.d
0
``


"" let's try a failing command''

     ``ls /notexist
        echo $?``
===> input:
``
┌──(kali㉿kali)-[~]
└─$ ls /sdiuob
ls: cannot access '/sdiuob': No such file or directory
``                                                                                     
===> output:
``
┌──(kali㉿kali)-[~]
└─$ echo $?
2``

  
**Cybersecurity relevance:**

Exit codes are used in scripts to detect failures, unauthorized access, or broken
 services automatically.

2.  Basic if condition
   `` if [ -f /etc/passwd ]; then
      echo "File exits"
      else 
      echo "File not Found"
      fi``
===> input:
``┌──(kali㉿kali)-[~]
└─$ if [ -f /etc/passwd ]; then 
``
===> output:
``  
then> echo "File exists"         
then> else   
else> echo "file do not exist"
else> fi            
File exists
``                   
3.

  ``ping -c 1 google.com > /dev/null"
   if [ $? -eq 0 ]; then
   echo "Network is reachable"
   else
     echo "Network issue detected"
    fi
   ``

===> input:
``
┌──(kali㉿kali)-[~]
└─$ ping -c 1 google.com > /dev/null
                                                                                           
┌──(kali㉿kali)-[~]
└─$ if [ $? -eq 0 ]; then
``
===> output:
``
then> echo "Network detected"
then> else   
else> echo  " network not detected"
else> fi                          
Network detected
``
**Cybersecurity relevance:**

Used in network monitoring scripts and availability checks during incident response.


**Cybersecurity relevance:**

Used to check critical files (logs, configs, binaries) during audits or compromise
 detection.


4. for Loop (user  Enumeration)

 ``for user in $(cut -d: -f1 /etc/passwd)
   do 
     echo "User : $user'
   done
``
===> input:
``┌──(kali㉿kali)-[~]
└─$ for user in $(cut -d: -f1 /etc/passwd)
for> do                           
for> echo "User : $user"
for> done                         
``
===> output:
``
User : root
User : daemon
User : bin
User : sys
User : sync
User : games
User : man
User : lp
User : mail
User : news
User : uucp
User : proxy
User : www-data
User : backup
User : list
User : irc
User : _apt
User : nobody
User : systemd-network
User : dhcpcd
User : systemd-timesync
User : messagebus
User : tss
User : strongswan
User : tcpdump
User : sshd
User : _rpc
User : dnsmasq
User : avahi
User : nm-openvpn
User : speech-dispatcher
User : usbmux
User : nm-openconnect
User : pulse
User : lightdm
User : statd
User : saned
User : polkitd
User : rtkit
User : colord
User : mysql
User : stunnel4
User : geoclue
User : Debian-snmp
User : sslh
User : cups-pk-helper
User : redsocks
User : _gophish
User : iodine
User : miredo
User : redis
User : postgres
User : mosquitto
User : inetsim
User : _gvm
User : kali
User : test
User : pipewire
User : tony
User : raju
User : kous
User : poorna
User : kapil
User : snort
User : Debian-exim
``                                                                                            

**Cybersecurity relevance**

Helps identify user accounts, suspicious users, or privilege escalation paths

5.for Loop (File Enumeration)
``
 for file in /etc/*.conf
 do
 echo "Found config: $file"
 done
``
===> input:
``
┌──(kali㉿kali)-[/etc]
└─$ for file in /etc/*.conf               
for> do                           
for> echo "Found config: $file"
for> done     
``
===> output:
``                    
Found config: /etc/adduser.conf
Found config: /etc/ca-certificates.conf
Found config: /etc/].conf
Found config: /etc/debconf.conf
Found config: /etc/deluser.conf
Found config: /etc/dhcpcd.conf
Found config: /etc/dns2tcpd.conf
Found config: /etc/e2scrub.conf
Found config: /etc/fuse.conf
Found config: /etc/gai.conf
Found config: /etc/hdparm.conf
Found config: /etc/host.conf
Found config: /etc/idmapd.conf
Found config: /etc/ipsec.conf
Found config: /etc/ld.so.conf
Found config: /etc/legion.conf
Found config: /etc/libao.conf
Found config: /etc/libaudit.conf
Found config: /etc/locale.conf
Found config: /etc/logrotate.conf
Found config: /etc/miredo.conf
Found config: /etc/mke2fs.conf
Found config: /etc/nfs.conf
Found config: /etc/nftables.conf
Found config: /etc/nikto.conf
Found config: /etc/nsswitch.conf
Found config: /etc/oinkmaster.conf
Found config: /etc/pam.conf
Found config: /etc/proxychains4.conf
Found config: /etc/redsocks.conf
Found config: /etc/request-key.conf
Found config: /etc/resolv.conf
Found config: /etc/rsyslog.conf
Found config: /etc/sensors3.conf
Found config: /etc/smartd.conf
Found config: /etc/smi.conf
Found config: /etc/strongswan.conf
Found config: /etc/sudo.conf
Found config: /etc/sudo_logsrvd.conf
Found config: /etc/tightvncserver.conf
Found config: /etc/ts.conf
Found config: /etc/ucf.conf
Found config: /etc/updatedb.conf
Found config: /etc/usb_modeswitch.conf
Found config: /etc/vconsole.conf
Found config: /etc/xattr.conf
``                                    
**Cybersecurity relevance:**
Used to scan configuration files for misconfigurations or insecure settings.

6. while loop
``
  count=1
  while [$count -le 5]
  do 
    echo "Attempt $count"
    count=$((count+1))
  done
``
===> input:
``
┌──(kali㉿kali)-[/etc]
└─$ count=1
while [ $count -le 5 ]
do
  echo "Attempt $count"
  count=$((count+1))
done
''
===> output:
``
Attempt 1
Attempt 2
Attempt 3
Attempt 4
Attempt 5
``
**Cybersecurity relevance:**

Used for retry logic, monitoring loops, and controlled automation.

7. simple bash script
``
nano check_logs.sh

if [ -f /var/log/auth.log ]; then
  echo "Auth log exists"
else
  echo "Auth log missing"
fi
chmod +x check_logs.sh
./check_logs.sh
``
===> input:
``
┌──(kali㉿kali)-[~/Downloads]
└─$ nano check_logs.sh
``
===> bash script:
``if [ -f /var/log/auth.log ]; then
  echo "Auth log exists"
else
  echo "Auth log missing"
fi
``
===> output:
``
┌──(kali㉿kali)-[~/Downloads]
└─$ bash check_logs.sh
Auth log exist
``                  

**Cybersecurity relevance:**

This is the starting point of SOC automation, compliance checks, and detection scripts.

==========================================end of lab_14===============================

```

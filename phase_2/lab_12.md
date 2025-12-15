## Text Processing with awk and sed

## Book reference:
**OccupyTheWeb** – Linux Basics for Hackers
(Used heavily for log analysis and text manipulation)

**Objective:*
Learn how to extract, filter, and modify text data using awk and sed, 
which are essential for analyzing logs, outputs of commands, and large text files in cybersecurity.

1. awk - Pattern Scanning and Proccessing language

##1.1
  `awk` '{print}' /var/log/auth.log

===>output:
``┌──(kali㉿kali)-[~]
└─$ awk '{print}' /var/log/auth.log   
2025-12-14T00:55:01.380879-05:00 kali CRON[10602]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-12-14T00:55:01.393645-05:00 kali CRON[10602]: pam_unix(cron:session): session closed for user root
2025-12-14T01:05:01.453393-05:00 kali CRON[10885]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-12-14T01:05:01.464878-05:00 kali CRON[10885]: pam_unix(cron:session): session closed for user root
2025-12-14T01:09:01.482048-05:00 kali CRON[10982]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-12-14T01:09:01.485528-05:00 kali CRON[10982]: pam_unix(cron:session): session closed for user root
2025-12-14T01:15:01.733799-05:00 kali CRON[11165]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-12-14T01:15:01.753202-05:00 kali CRON[11165]: pam_unix(cron:session): session closed for user root
2025-12-14T01:17:01.763535-05:00 kali CRON[11177]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-12-14T01:17:01.770359-05:00 kali CRON[11177]: pam_unix(cron:session): session closed for user root
2025-12-14T01:21:00.492256-05:00 kali xfce4-screensaver-dialog: gkr-pam: unlocked login keyring
2025-12-14T01:21:00.494075-05:00 kali xfce4-screensaver-dialog: pam_unix(xfce4-screensaver:account): setuid failed: Operation not permitted
2025-12-14T01:25:01.782553-05:00 kali CRON[11281]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-12-14T01:25:01.787741-05:00 kali CRON[11281]: pam_unix(cron:session): session closed for user root
2025-12-14T01:35:01.809499-05:00 kali CRON[11375]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-12-14T01:35:01.818805-05:00 kali CRON[11375]: pam_unix(cron:session): session closed for user root
2025-12-14T01:39:01.834775-05:00 kali CRON[11409]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-12-14T01:39:01.841058-05:00 kali CRON[11409]: pam_unix(cron:session): session closed for user root
2025-12-14T01:41:34.472222-05:00 kali xfce4-screensaver-dialog: gkr-pam: unlocked login keyring
2025-12-14T01:41:34.475251-05:00 kali xfce4-screensaver-dialog: pam_unix(xfce4-screensaver:account): setuid failed: Operation not permitted
2025-12-14T01:45:01.860283-05:00 kali CRON[11551]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-12-14T01:45:01.864434-05:00 kali CRON[11551]: pam_unix(cron:session): session closed for user root
2025-12-14T01:55:02.033256-05:00 kali CRON[11808]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-12-14T01:55:02.049328-05:00 kali CRON[11808]: pam_unix(cron:session): session closed for user root
2025-12-14T01:58:14.400642-05:00 kali xfce4-screensaver-dialog: gkr-pam: unlocked login keyring
2025-12-14T01:58:14.404232-05:00 kali xfce4-screensaver-dialog: pam_unix(xfce4-screensaver:account): setuid failed: Operation not permitted
2025-12-14T02:05:02.629806-05:00 kali CRON[12049]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-12-14T02:05:02.778618-05:00 kali CRON[12049]: pam_unix(cron:session): session closed for user root
2025-12-14T02:09:44.349727-05:00 kali systemd-logind[548]: New seat seat0.
``

**Explanation:**

{print} tells awk to print every line
Similar to cat, but awk is used for processing

**Cybersecurity relevance:**
Logs are often processed using awk instead of viewing manually

1.2
  ``awk '{print $1}' /var/log/auth.log``

``
┌──(kali㉿kali)-[~]
└─$ awk '{print $1}' /var/log/auth.log
2025-12-14T00:55:01.380879-05:00
2025-12-14T00:55:01.393645-05:00
2025-12-14T01:05:01.453393-05:00
2025-12-14T01:05:01.464878-05:00
2025-12-14T01:09:01.482048-05:00
2025-12-14T01:09:01.485528-05:00
2025-12-14T01:15:01.733799-05:00
2025-12-14T01:15:01.753202-05:00
2025-12-14T01:17:01.763535-05:00
2025-12-14T01:17:01.770359-05:00
2025-12-14T01:21:00.492256-05:00
2025-12-14T01:21:00.494075-05:00
2025-12-14T01:25:01.782553-05:00
2025-12-14T01:25:01.787741-05:00
2025-12-14T01:35:01.809499-05:00
2025-12-14T01:35:01.818805-05:00
2025-12-14T01:39:01.834775-05:00
2025-12-14T01:39:01.841058-05:00
2025-12-14T01:41:34.472222-05:00
2025-12-14T01:41:34.475251-05:00
2025-12-14T01:45:01.860283-05:00
2025-12-14T01:45:01.864434-05:00
2025-12-14T01:55:02.033256-05:00
2025-12-14T01:55:02.049328-05:00
2025-12-14T01:58:14.400642-05:00
2025-12-14T01:58:14.404232-05:00
2025-12-14T02:05:02.629806-05:00
2025-12-14T02:05:02.778618-05:00
2025-12-14T02:09:44.349727-05:00
2025-12-14T02:09:44.349731-05:00
``

**Explanation:**

$1 → first column (usually date or timestamp)
Columns are separated by spaces by default
**Cybersecurity relevance:**

Extract timestamps for attack timeline analysis

1.3
   ``awk '{print $1, $2, $3}' /var/log/auth.log``
===>output:
``
┌──(kali㉿kali)-[~]
└─$ awk '{print $1, $2, $3}' /var/log/auth.log
2025-12-14T00:55:01.380879-05:00 kali CRON[10602]:
2025-12-14T00:55:01.393645-05:00 kali CRON[10602]:
2025-12-14T01:05:01.453393-05:00 kali CRON[10885]:
2025-12-14T01:05:01.464878-05:00 kali CRON[10885]:
2025-12-14T01:09:01.482048-05:00 kali CRON[10982]:
2025-12-14T01:09:01.485528-05:00 kali CRON[10982]:
2025-12-14T01:15:01.733799-05:00 kali CRON[11165]:
2025-12-14T01:15:01.753202-05:00 kali CRON[11165]:
2025-12-14T01:17:01.763535-05:00 kali CRON[11177]:
2025-12-14T01:17:01.770359-05:00 kali CRON[11177]:
2025-12-14T01:21:00.492256-05:00 kali xfce4-screensaver-dialog:
2025-12-14T01:21:00.494075-05:00 kali xfce4-screensaver-dialog:
``

**Explanation:**

Prints first three columns
Useful for structured data
**Cybersecurity relevance:**

Helps isolate IP addresses, users, and actions

1.4

   ``awk '/Failed/ {print}' /var/log/auth.log``
===> output:
``
┌──(kali㉿kali)-[~]
└─$ awk '/Failed/ {print}' /var/log/auth.log 
2025-12-14T02:09:55.026784-05:00 kali lightdm: pam_systemd(lightdm-greeter:session): Failed to release session: Transport endpoint is not connected
2025-12-14T03:21:08.649216-05:00 kali lightdm: pam_systemd(lightdm-greeter:session): Failed to release session: Transport endpoint is not connected
2025-12-15T03:54:38.244649-05:00 kali lightdm: pam_systemd(lightdm-greeter:session): Failed to release session: Transport endpoint is not connected
``


**Explanation:**

/Failed/ is the search pattern
Prints only matching lines
**Cybersecurity relevance:**

Detects failed login attempts
Useful for brute-force detection

1.5
 `` awk '/Failed/ {count++} END {print count}' /var/log/auth.log``

===> output:
``
┌──(kali㉿kali)-[~]
└─$ awk '/Failed/ {count++} END {print count}' /var/log/auth.log
4
``

**Explanation:**

Counts how many times “Failed” appears
**Cybersecurity relevance:**

Measures attack frequency
Helps identify suspicious activity levels

2.sed - Stream Editor
 sed is used to serach, replace,and modify text.

2.1

   ``sed '' /etc/passwd``

===> output:
``
──(kali㉿kali)-[~]
└─$ sed '' /etc/passwd         
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
``

**Explanation:**

Displays file without modification
Used mainly as a base for transformations


2.2

  
  ``sed 's/root/admin/' /etc/passwd``

===> output:
``┌──(kali㉿kali)-[~]
└─$ sed 's/root/admin/' /etc/passwd
admin:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
``


**Explanation:**

s → substitute
Replaces first occurrence per line
Does NOT modify file (output only)
**Cybersecurity relevance:**

Used to sanitize or anonymize data

2.3
  ``sed 's/root/admin/g' /etc/passwd``
===> output:
``┌──(kali㉿kali)-[~]
└─$ sed 's/root/admin/g' /etc/passwd
admin:x:0:0:admin:/admin:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
dhcpcd:x:100:65534:DHCP Client Daemon:/usr/lib/dhcpcd:/bin/false
''

**explanation:**

g → global replacement
**Cybersecurity relevance:**

Useful for cleaning logs or preparing reports


2.4 Replace and save to new file

    ``sed 's/Failed/FAILED_LOGIN/g' /var/log/auth.log > auth_modified.log``

===> output:
``
┌──(kali㉿kali)-[~/Downloads]
└─$ cat test1.txt 
2025-12-14T00:55:01.380879-05:00 kali CRON[10602]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-12-14T00:55:01.393645-05:00 kali CRON[10602]: pam_unix(cron:session): session closed for user root
2025-12-14T01:05:01.453393-05:00 kali CRON[10885]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-12-14T01:05:01.464878-05:00 kali CRON[10885]: pam_unix(cron:session): session closed for user root
2025-12-14T01:09:01.482048-05:00 kali CRON[10982]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-12-14T01:09:01.485528-05:00 kali CRON[10982]: pam_unix(cron:session): session closed for user root
2025-12-14T01:15:01.733799-05:00 kali CRON[11165]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
2025-12-14T01:15:01.753202-05:00 kali CRON[11165]: pam_unix(cron:session): session closed for user root
2025-12-14T01:17:01.763535-05:00 kali CRON[11177]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
''


**Explanation:**

 Redirects modified output to a new file
**Cybersecurity relevance:**

 Helps mark suspicious events clearly


2.5
  ``sed '/no login/d' /etc/passwd``

===>output:
``┌──(kali㉿kali)-[~]
└─$ sed '/no login/d' /etc/passwd                                          
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
``
**Explanation:**

/pattern/d deletes matching lines (output only)
**Cybersecurity relevance:**

Filters unnecessary noise from analysis output

2.6
 `` sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config``

===>output:
``
┌──(kali㉿kali)-[~]
└─$ sudo sed  's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config 


# This is the sshd server system-wide configuration file.  See
# sshd_config(5) for more information.

# This sshd was compiled with PATH=/usr/local/bin:/usr/bin:/bin:/usr/games

# The strategy used for options in the default sshd_config shipped with
# OpenSSH is to specify options with their default value where
# possible, but leave them commented.  Uncommented options override the
# default value.

Include /etc/ssh/sshd_config.d/*.conf

#Port 22
#AddressFamily any
#ListenAddress 0.0.0.0
``

**Explanation:**

-i modifies the file directly
**Cybersecurity relevance:**

Used for system hardening
Disables insecure configurations

====================================end of lab_12=========================================

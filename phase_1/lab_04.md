## phase_1, lab_04.md
**book**: Concepts from TLDP + man pages + Linux fundamentals
**objective**: Understand user accounts, group memberships, privilege separation, and commands to manage
## **1.**
     ```whoami: shows the current logged in user```
===> input:
```┌──(kali㉿kali)-[~]
   └─$ whoami```
  
===> output:
  ``kali``
## Cybersecurity Relevance:

* Helps confirm which account you are operating under.
* Prevents accidental execution of critical commands as the wrong user.


## **2.**
  ```groups : shows to which group the current user  belongs to```
===> input:
```┌──(kali㉿kali)-[~/cybersecurity_labs/phase_1]
   └─$ groups```
===> output
```kali adm dialout cdrom floppy sudo audio dip video plugdev users netdev scanner bluetooth lpadmin wireshark kaboxer vboxsf```
## Cybersecurity Relevance:

* Attackers often add themselves to groups like sudo or adm.
* Checking groups helps detect unauthorized privilege expansion.


## **3.**
   ```getent: to list all user registerd in the system```
===> input: 
```┌──(kali㉿kali)-[~]
   └─$ getent passwd```
===> output:
```root:x:0:0:root:/root:/usr/bin/zsh
   daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
   bin:x:2:2:bin:/bin:/usr/sbin/nologin.......```
## Cybersecurity Relevance:

* Helps identify suspicious or unauthorized accounts.
* Used during incident response to detect newly created attacker accounts.

## **4.**
  ```getent group : Lists all groups configured on the system.```
===> input:
```┌──(kali㉿kali)-[~]
   └─$ getent group```
===> output:
``` root:x:0:
    daemon:x:1:
    bin:x:2:
    sys:x:3:.......```
## **Cybersecurity Relevance:

* Helps identify dangerous groups such as sudo, adm, or docker.
* Important for auditing escalation paths.

## **5.**
  ```sudo adduser user1: create a new users, groups and passwords```
===> input:
```┌──(kali㉿kali)-[~]
   └─$ sudo adduser kapil```
====> output:
```New password: 
   Retype new password: 
   passwd: password updated successfully
   Changing the user information for kapil```
## Cybersecurity Relevance:

* Used to control file access for teams.
* Attackers try adding themselves into privileged groups.

## **6.**
   ```sudo usermod -aG devs user1: add user1 to devs group```
===> input:
```┌──(kali㉿kali)-[~]
   └─$ sudo usermod -aG sudo kapil```
===> output:
``` user kapil gets added to sudo group```
##Cybersecurity Relevance:

* Misconfigured group membership causes privilege escalation.
* Group permissions often determine access to logs, configs, and binaries.

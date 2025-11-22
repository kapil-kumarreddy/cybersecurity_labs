```## phase_1  lab_03##
**book**:The linux command line-- William shots
**permission**
### Access rights to files and directories are defined in terms of read access, write, access, and execution access. If we look at the output of the ls command, we can get some clue as to how this is implemented
  **Multiuser Capability (Linux/unix)**
## The core meaning is that Linux or  Unix supports multiuser capability, allowing more than one person to use the computer at the same time.

""" let's discuss about owners, groups members and everybody else"""
- **Ownership**: A user is designated as the owner of a file or directory, giving that user control over its access rights.
 
- **Groups**: Users can be organized into groups. A file owner can grant access rights to a specific group that consists of one or more users.

- **World**: Beyond the owner and the group, an owner can also grant a set of access rights to everybody else on the system. This category is referred to as the world in Unix terminology.
""" let's dive into commands"""

## **1**.
    ``id``: to display the userid, groupid and other groupids the current working system 

- input:
    ```┌──(kali㉿kali)-[~/cybersecurity_labs/phase_1]
       └─$ id```
- output:
  ```uid=1000(kali) gid=1000(kali) groups=1000(kali),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),101(netdev),103(scanner),107(bluetooth),125(lpadmin),133(wireshark),135(kaboxer),136(vboxsf)```
**output explanation**

- UID (User ID): uid=1000(kali) means the user has a unique identification number of 1000, and the associated login name is kali.
 
- GID (Group ID): gid=1000(kali) means the user's primary group is also identified by the number 1000, and the primary group name is kali.

- Groups: The long list that follows defines all the supplementary groups to which the user belongs. Membership in these groups grants the user specific permissions to access system devices and services.


##  Access rights to files and directories are defined in terms of read access, write access, and execution access. If we look at the output of the ls command, we can get some clue as to how this is implemented
  """let's run ls -l command in kali linux"""
===> input:
   ```┌──(kali㉿kali)-[~/cybersecurity_labs/phase_1]
      └─$ ls -l```
===> output:
   ```total 16
   -rw-rw-r-- 1 kali kali 6478 Nov 20 07:59 lab_01.md
   -rw-rw-r-- 1 kali kali 2996 Nov 20 08:06 lab_02.md
   -rw-rw-r-- 1 kali kali 2231 Nov 21 00:54 lab_03.md```
## The first 10 characters in the above output describe about the file's perimissons and type of file.
## The first character describe about the type of file.
## **type of file attributes**

- "-": Represents a regular file. This is the standard file type used for data, such as documents, images, scripts, or executable programs.

- "d": Represents a directory. This is essentially a container or folder used to organize other files and directories within the filesystem.

- "l": Represents a symbolic link. This is a special type of file that acts as a pointer or shortcut to another file or directory on the system. It's important to note that the permissions listed for a symbolic link are always dummy values (rwxrwxrwx); the true permissions are those of the file it points to.

- "c": Represents a character special file. This file type refers to a device that handles data as a stream of individual bytes, without buffering data into blocks. Examples include terminals or the /dev/null device.
 
- "b": Represents a block special file. This file type refers to a device that handles data in fixed-size blocks, making it suitable for devices that require random access to data, such as hard drives, SSDs, or DVD drives.

## **File Mode: Access Permissions**
##The nine characters that follow the file type attribute are known as the file mode, and they represent the read, write, and execute permissions for three distinct categories of users:

-  **File's Owner**: The first set of three characters controls the owner's access.

-  **File's Group Owner**: The second set of three characters controls the access for users belonging to the file's primary group.

-  **Everybody Else (World)**: The final set of three characters controls the access for all other users on the system.

## This structure is the foundation of the Unix security model, allowing the owner to precisely define who can:

* Read (r) the file.

* Write (w) to the file (modify or delete it).

* Execute (x) the file (run it as a program or script, or enter it if it's a directory).
**Cybersecurity Relevance**:
- Incorrect file permissions can expose sensitive data to all users.
- Weak permissions (e.g., world-writable files) are a common privilege escalation path.
- Attackers often modify file permissions to hide or execute malicious scripts.


## **2.**
   ``chmod``: to change file mode
## """ chomd is a command which is used to change the file mode of directories and files. It uses two to this"""
        --> Octal number representation
	--> Symbolic representation
## """ i morelly interseted in Octal number representation. So wil concerntrate on octal number representation"""
## let's discuss the format of the ``chmod`` command :
             ```chmod octalnumber filename```
* chmod: command
* octalnumber:
         **File Mode Octal Value Summary**
## The octal value determines the permissions granted for a single user category (Owner, Group, or World):

>> Octal 0, binary(000): Corresponds to the mode --- (No permissions: no read, no write, no execute).
 
>> Octal 1, binary(001): Corresponds to the mode --x (Execute only).

>> Octal 2, binary(010): Corresponds to the mode -w- (Write only).

>> Octal 3, binary(011): Corresponds to the mode -wx (Write and Execute).

>> Octal 4, binary(100): Corresponds to the mode r-- (Read only).

>> Octal 5, binary(101): Corresponds to the mode r-x (Read and Execute).

>> Octal 6, binary(110): Corresponds to the mode rw- (Read and Write).

>> Octal 7, binary(111): Corresponds to the mode rwx (Read, Write, and Execute).

**Example of Use**
## To set full permissions for the owner, read/execute for the group, and read only for others, you would combine the octal values:

---> Owner: rwx (7)

---> Group: r-x (5)

---> World: r-- (4)

"""The resulting complete file mode would be 754."""
"""performing chmod on lab_01.md file"""
    ##before chmod using
```┌──(kali㉿kali)-[~/cybersecurity_labs/phase_1]
   └─$ ls -l lab_01.md         
   -rw-rw-r-- 1 kali kali 6478 Nov 20 07:59 lab_01.md```

===> input:
```┌──(kali㉿kali)-[~/cybersecurity_labs/phase_1]
   └─$ chmod 777 lab_01.md```
===> output:
``` after performing chmod command on lab_01.md
    ┌──(kali㉿kali)-[~/cybersecurity_labs/phase_1]
    └─$ ls -l lab_01.md
    -rwxrwxrwx 1 kali kali 6478 Nov 20 07:59 lab_01.md```
"""The commands show the use of chmod 777 to change the permissions of the file lab_01.md from an initial limited state (-rw-rw-r--) to full access (-rwxrwxrwx) for the owner, group, and all others."""
**Cybersecurity Relevance**:
- Setting files to 777 is dangerous and allows anyone to modify or execute files.
- Secure configurations require controlled permission settings (e.g., 600 for private keys).
- Attackers use chmod to give executable permissions to malicious scripts.


## **3.**
    ``umask`` : to change or set the deflaut permissions.
## """ The umask command is used to control the deflaut permissions for a file when it is created."""
    """ let's discuss about the format of umask
    ````umask number```
## the number given to the command works differently by using a method
   """ let's discuss about the method by using a example"""
## by deflaut umask value is set to 022, so by deflaut the permissions are set to "_rw_r__r__"
  ""let's check""
 
===> input: 
```┌──(kali㉿kali)-[~/cybersecurity_labs/phase_1]
   └─$ touch lab                                                                                                                                                           
   ┌──(kali㉿kali)-[~/cybersecurity_labs/phase_1]
   └─$ ls -l lab```
===> output: 
  ```-rw-r--r-- 1 kali kali 0 Nov 21 13:36 lab```

## let's break down
* Default file permissions start as **666** → `rw-rw-rw-`
* The system applies the **umask value**, usually **022**
* Umask **022** removes the write bit from *group* and *others*


Default: 666
Umask :  022
----------------
Result: 644

--> 6 = rw- → owner has read + write
--> 4 = r-- → group has read-only
--> 4 = r-- → others have read-only

"""now let's change the umask value"""
===> input:
```┌──(kali㉿kali)-[~/cybersecurity_labs/phase_1]
   └─$ umask                                                                                                                                                     
   ┌──(kali㉿kali)-[~/cybersecurity_labs/phase_1]
   └─$ touch lab2                                                                                                                                                
   ┌──(kali㉿kali)-[~/cybersecurity_labs/phase_1]
   └─$ ls -l lab2```
===> output:
```--w--w--w- 1 kali kali 0 Nov 21 13:55 lab2```

## let's break down 
* Default file permissions start as 666 → rw-rw-rw-
* The system applies the umask 555
* Umask 555 removes the read and execute bits for owner, group, and others

Default: 666
Umask :  555
----------------
Result: 222

---> 2 = -w- → owner has write only
---→ 2 = -w- → group has write only
---→ 2 = -w- → others have write only

**Final permissions: --w--w--w-**
**Cybersecurity Relevance**:
- A weak umask (e.g., 000) causes files to be created with insecure permissions.
- Strong umask values prevent sensitive new files from being world-readable.
- System administrators use umask to enforce secure file creation policies.

## ** changing the identities **
>>> Changing identities in Linux means acting as another user**.
>>> You can switch users with su, or run specific commands as another user with sudo.
>>> This is mainly used to get admin/root privileges when needed.


## **4.**
   ``` su : run a shell as another subsitute user```
## let's discuss about the syntax of the shell
   ``` su [-[l]] [user]```
"""Using su -l starts a login shell for another user.
   This loads that user’s environment and moves you to their home directory.
   If no user is given, it switches to root by default.
   The -l option is often shortened to just - (e.g., su -)."""
===> input:
```┌──(kali㉿kali)-[~]
   └─$ su -             

   Password```
===> output: 
```┌──(root㉿kali)-[~]
   └─# pwd
   /root\
   ┌──(root㉿kali)-[~]
   └─# exit```
  **output explanation** 
"""Using su - switches you to the root user and loads the root user’s full login environment.
   Your working directory changes from /home/kali to /root because you became the root user.
   Typing exit logs you out of the root shell and returns you to your normal kali user.""" 
**Cybersecurity Relevance**:
- Attackers try to switch users after compromising a low-privilege account.
- su logs can reveal privilege escalation attempts in /var/log/auth.log.
- Proper password policies prevent unauthorized account switching.


## **5.**
  ```sudo : to run commands as a another user```
>>> sudo is similar to su, but it gives users controlled permission to run specific commands as another user (usually root).
>>> Admins can limit which commands each user is allowed to run through the /etc/sudoers file.
>>> Unlike su, sudo does not need the root password — it uses your own password for authentication.
>>> sudo asks for your own password, not the superuser’s.
>>> It runs the command without starting a new shell or changing the environment.
>>> So you type commands normally, exactly the same way you would without sudo.

===> input:
```┌──(kali㉿kali)-[~]
   └─$ sudo apt update```
===> output:
```[sudo] password for kali:```

**output explanation**
"""sudo asks for your password to confirm it’s really you, not someone else using your account.
After you authenticate, sudo runs the command with temporary admin (root) privileges.
It does not need the root password because sudo is designed to give controlled, secure access using your identity."""

**Cybersecurity Relevance**:
- Misconfigured sudo rules are a common privilege escalation vector.
- Monitoring sudo usage helps detect suspicious admin-level activity.
- Least-privilege principle requires restricting which commands users can run via sudo.

## **6.**
  ```chown : to change the owner and group of  file```
## """ let's see syntax of the of ``chown`` commands"""
   ``` chown owner:group filename```
---> owner : to user, whom i want to give ownership.
---> group : to group, whom i want to give group ownership.
---> filename : the desired file which needed to change it's owner and group owner.
""" let's see who this works"""
>>> bob → changes the file’s owner to bob.

>>> bob:users → changes owner to bob and group to users.

>>> :admins → only changes the group to admins (owner stays same).

>>> bob: → owner becomes bob, group becomes bob’s default login group.

===> input:
```┌──(kali㉿kali)-[~/Downloads]
   └─$ ls -l test1.txt
   -rw-rw-rw- 1 kali kali 257 Oct 25 06:27 test1.txt
                                                                                                                                                                                                                                                                                          
   ┌──(kali㉿kali)-[~/Downloads]
   └─$ sudo chown  raju: test1.txt```
===> output:
```┌──(kali㉿kali)-[~/Downloads]
   └─$ ls -l test1.txt
   -rw-rw-rw- 1 raju raju 257 Oct 25 06:27 test1.txt```
   **output  explanation**
"""Using chown changes the owner and group of a file. In the first command, I changed test1.txt ownership from kali to raju,
   so the file became owned by user raju. Then I used chown again to give ownership back to kali. This proves that only root
   (using sudo) can change file ownership, which is important for protecting files from unauthorized modification."""
**Cybersecurity Relevance**:
- Attackers may change file ownership to hide backdoors or prevent detection.
- Incorrect ownership on system files can break security controls.
- Ensuring correct ownership protects critical logs and configuration files.

## **7.**
   ``` passwd: to change your current login password```
## you need to call with sudo. after that is asks for current password, if you give it correct. then it asks for new password
""" let's see a example"""
===> input:
```┌──(kali㉿kali)-[~]
   └─$ sudo passwd```
===> output:
```current password:
   New password: 
   Retype new password: e
   passwd: password updated successfully```
 
**Cybersecurity Relevance**:
- Strong password policies reduce the success of brute-force attacks.
- Sudden password changes in logs may indicate account compromise.
- Proper use of passwd ensures only authorized users modify credentials.
   **We will continue with the next lab.**
```

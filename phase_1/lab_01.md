#phase_1 : what_is_the_shelL
**book**:The linux command line-- William shots
**Objective:** Understand what the shell is, how the terminal emulator works, the shell prompt, and basic Linux commands.

## what is the shell?
>>> A Shell is program that takes keyboards commands from user and gives them to the operating system to carry out the commands.

## what is terimnal emulator?
>>> A terminal emulator is used to interact with shell when using GUI. Simply it acts a translator between shell and GUI.

///let's start our lab in kali linux///
///when we open a terimnal emualator we can see, And there we can see a somethinh like 
                            ""┌──(kali㉿kali)-[~]
                              └─$""
which is called shell prompt.
This means:

- **kali** → username  
- **kali** → machine name  
- **~** → current working directory (home directory)///
///It tells us that (username㉿machinename)-[currentworkingdirectory]///
```let's try some commands```

##1.
   **date**: which displays current date and time
##input:
   date 
##output:
Tue Nov 18 03:13:05 AM EST 2025
### **Cybersecurity Relevance**
* Useful for timestamp correlation during incident analysis or log investigat

##2.
   **cal**: displays the calendar of the current monthw
##input:
   cal 
##output:
   November 2025      
Su Mo Tu We Th Fr Sa  
                   1  
 2  3  4  5  6  7  8  
 9 10 11 12 13 14 15  
16 17 18 19 20 21 22  
23 24 25 26 27 28 29  
30
### **Cybersecurity Relevance**
* Useful when writing forensic timelines or referencing event dates.                   

##3.
  **df**: to see the current amount free space in my disk drive///
##input:
   df  
##output:
Filesystem     1K-blocks     Used Available Use% Mounted on
udev              942560        0    942560   0% /dev
tmpfs             202104     1012    201092   1% /run
/dev/sda1       82083148 22103864  55763736  29% /
tmpfs            1010516        4   1010512   1% /dev/shm
tmpfs               5120        0      5120   0% /run/lock
tmpfs            1010520       12   1010508   1% /tmp
tmpfs               1024        0      1024   0% /run/credentials/getty@tty1.service
tmpfs             202100      124    201976   1% /run/user/1000
tmpfs               1024        0      1024   0% /run/credentials/systemd-journald.service
### **Cybersecurity Relevance**
* Low disk space can cause:
* log loss  
* service crashes  
* potential DoS conditions  

##4.
  **free**: to display the amount of free memory
##input:
   free
##output:
               total        used        free      shared  buff/cache   available
Mem:         2021036      977988      186088       31032     1099144     1043048
Swap:         976556           0      976556
### **Cybersecurity Relevance**
* Memory spikes may indicate:
* malicious processes  
* cryptominers  
* memory exhaustion attacks 

##5.
 **exit** or **ctrl+D**: to end the terminal session


##next, i am learning who to navigate to the desired file in linux systems
##like windows, a Unix based systems follows a hierarchical directory structure. This means  files are organized in tree like structure or pratterns which may have files, directories and subdirectories
##by deflaut every linux based system have a root directory which has flies and directories, which may have other files and subdirectories
##!!! note: unlike windows systems,  which have different tree system for each storage devices. but in linux systems, it has a only one tree which handles every storeage device that are connected to computer. the attacted storage devices are connected to the tree depending on the system administor, the person who is responsbile for the maintance of the systems!!!
##let"s talk about directoriee, let's assume that, we are at one directory in the middle of the tree, the directory which is above the current directory is called parent directory, and the current directory is called current working directory
```let's practice some commands```

##6.
  **pwd(print working directory)**: displays current working directory
##input:
┌──(kali㉿kali)-[~/cybersecurity_labs/phase_1]
└─$ pwd
##output: 
/home/kali/cybersecurity_labs/phase_1
## Cybersecurity Relevance
* Helps avoid mistakes during investigation.
* Knowing the exact directory prevents deleting or modifying the wrong file.
* Important when navigating compromised machines or checking logs.

##7.
  **ls**: listing the contents of a directory
##input:┌──(kali㉿kali)-[~]
└─$ ls
##output:
AutoPatchSQL  cybersecurity_labs  Desktop  Documents  Downloads  linux_funad_labs  linux_funadmentals  Music  Pictures  playground  Public  q  scanner-output.txt  Templates  test.py  Videos\
## Cybersecurity Relevance
* Attackers may hide files or scripts in directories.
* `ls` helps identify hidden files, weird filenames, or strange permissions.
* Useful for spotting unauthorized files or malware.
```i am familar  with windows, so i know about paths of each file mean.so linux also uses same file path rules to navigate to certain file with cd command```

##8.
  **cd**: to change the current working directory
##input:
┌──(kali㉿kali)-[~]
└─$ cd cybersecurity_labs/phase_1
##output:
┌──(kali㉿kali)-[~/cybersecurity_labs/phase_1]
└─$ pwd
/home/kali/cybersecurity_labs/phase_1
   ```we can see that the current working directory is changed into anotheir desired directory```
## Cybersecurity Relevance
* Needed to move into important locations like `/etc` and `/var/log`.
* Security analysis often requires checking logs, configs, and user home directories.
* Helps follow attacker activity across directories.

##9.
  **cd ..** : goes to the parent directory of a current working directory
##input:                                                                                                                                                                         
┌──(kali㉿kali)-[~/cybersecurity_labs]
└─$ cd .. 
##output:
┌──(kali㉿kali)-[~]
└─$ pwd
/home/kali
## Cybersecurity Relevance
* Allows moving back to system-level directories during forensic investigation.
* Helpful when retracing attacker movement from subdirectories upward.
* Useful for quickly navigating during incident response.

```that's it


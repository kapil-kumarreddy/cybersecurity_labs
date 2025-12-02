```

## phase_2 ## lab_09 
** book **: Occupytheweb - Linux Basics for Hackers
** chapter **: managing file sytems
**Objective**: Learn how to check disk usage, verify filesystem health, and mount storage devices in Linux.

""In this lab we are going to learn the commands which helps us in monioriing the state of filesystem ---- which helps ethical hackers and system administrator.""


## **1.**
  `` df : this command will provide us basic information on any hard disk or mounted devices``

===> input:
`` 
   ┌──(kali㉿kali)-[~]
   └─$ df  
``
===> output:
`` 
  Filesystem     1K-blocks     Used Available Use% Mounted on
  udev              942560        0    942560   0% /dev
  tmpfs             202104     1012    201092   1% /run
  /dev/sda1       82083148 22358444  55509156  29% /
  tmpfs            1010516        4   1010512   1% /dev/shm
  tmpfs               5120        0      5120   0% /run/lock
  tmpfs               1024        0      1024   0% /run/credentials/systemd-journald.service
  tmpfs            1010520        8   1010512   1% /tmp
  tmpfs               1024        0      1024   0% /run/credentials/getty@tty1.service
  tmpfs             202100      124    201976   1% /run/user/1000
``
"" the first lines shows catagory headers. here the disk space is given in 1KB blocks.""
"" the df command also tells us on which a current file is mounted""
"" for a example""
"" in secound line 1k-blocks tells us the disk sapce is 942560
 and nothing is used and the same 942560 is available to use.
 mounted column tells us that that the udev is mounted in /dev""

## **2.**

  `` unmount: unmounts a file ``
===> input:
``
  ┌──(kali㉿kali)-[~]
  └─$ sudo umount /mnt/usb
``
===> output:
``
  no output means command runed successfully
``

## checking the error 

## **3.**
  `` fsck: checks the filesystem for error and if possible, it will fix them ``
"" to use a fsck on filesystem we need to first umount a device from a filesystem ""
"" to run a fsck we need specify the device ""
""syntax of fsck"
  [ fsck device ]|
===> input:
``
┌──(kali㉿kali)-[/dev]
└─$ sudo fsck -n /               
``
===> output:
``
[sudo] password for kali: 
fsck from util-linux 2.41.2
e2fsck 1.47.2 (1-Jan-2025).
Warning: skipping journal recovery because doing a read-only filesystem check.
Pass 1: Checking inodes, blocks, and sizes
Pass 2: Checking directory structure
Pass 3: Checking directory connectivity
Pass 4: Checking reference counts
Pass 5: Checking group summary information
Free blocks count wrong (14931144, counted=14933197).
Fix? no

Free inodes count wrong (4662507, counted=4662509).
Fix? no

Feature orphan_present is set but orphan file is clean.
Clear? no

root: 588565/5251072 files (0.2% non-contiguous), 6064693/20995837 blocks

``
 ## !! as this may damage the existing filesystem i just scaned the filesystem !! ##

```

##phase_1  lab_02##
**boosk**:The linux command line-- William shots
**exploring the system**
**file system basics**
## the "ls" command we did in lab_01 is most frequently used command in linux systems
## which is used to list contents of current working directory
## we can ls in many other ways by adding some commands to it 

       ``let's practice them``


##1.
   **ls dir1 dir2**: we can specifiy the desired directory to be listed form a current working directory
   --dir1-- : name or path of the desired directory which is from current working director
   --dir2-- : we can list other desired directory at  a simultaneously with **dir1** directory which have to be form same current working directory 
##input:
 ┌──(kali㉿kali)-[~]
└─$ ls cybersecurity_labs/phase_1  cybersecurity_labs
##output
cybersecurity_labs:
phase_1  phase_2  phase_3

cybersecurity_labs/phase_1:
lab_01.md  lab_02.md

### Cybersecurity relevance:
* Helps understand the location when navigating logs or system files.
* Prevents accidental actions in the wrong directory.


##2.
   **ls -l** : to display other detials of the contents in current working directory
##input:
┌──(kali㉿kali)-[~]
└─$ ls -l cybersecurity_labs                

##output:
total 12
drwxrwxr-x 2 kali kali 4096 Nov 19 12:40 phase_1
drwxrwxr-x 2 kali kali 4096 Nov 17 09:32 phase_2
drwxrwxr-x 2 kali kali 4096 Nov 17 09:32 phase_3

##i learnt most important topics in this lab which are optinos and arguments
  ```let's discusse the fomrat and who are they used?```
  **command -options arguments**
##most of the commands in linux are used with options to modify the behaviour of commands 


##3.
   **ls -lt** :  which are the l option to produce long format output, and the t option to sort the result by the file’s modification time.
   **ls -lt --reverse** : We added the long option --reverse to reverse the order of the sort.
##input:
┌──(kali㉿kali)-[~/cybersecurity_labs]
└─$ ls -lt --reverse 
total 12

##output:a
drwxrwxr-x 2 kali kali 4096 Nov 17 09:32 phase_3
drwxrwxr-x 2 kali kali 4096 Nov 17 09:32 phase_2
drwxrwxr-x 2 kali kali 4096 Nov 19 12:40 phase_1
                                                 
  ``note`` : options are case sensetive
the ls command can be used with other possible options


##4.
   **file filename** : to determine the file type
   --filename-- : desired file name to be determined 
   ***note** : A unix based system linux treats every thing as a file
##input:
┌──(kali㉿kali)-[~/cybersecurity_labs/phase_1]
└─$ file lab_01.md

##output:
lab_01.md: Unicode text, UTF-8 text, with very long lines (365)


##5.
  **less filename** : to view content desired file
  --filename--: file name or file path which is determined to view the content
##input:
┌──(kali㉿kali)-[~/cybersecurity_labs/phase_1]
└─$ less lab_01.md   

##output:
   ```starts the contents of the file by open a tect editor```
   **note** : close by clicking ctrl+z

```

## phase_2 ## lab_07.md
** Process Management **
** Objective**: Learn how to view, control, and terminate running processes used in Linux systems.
## **1.**
   `` ps ``: to see what processes are active
===> input:
``
  ┌──(kali㉿kali)-[~]
  └─$ ps
``
===> output:
`` 
    PID TTY          TIME CMD
   1662 pts/0    00:00:04 zsh
   5808 pts/0    00:00:00 ps
``
## ps with options ##
## **2.**
   `` ps aux ``: will show all processes runing on the system for all users.
===> input:
``
   ┌──(kali㉿kali)-[~]
   └─$ ps aux
``
===> output:
``
  USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
  root           1  0.0  0.7  23984 14436 ?        Ss   Nov28   0:03 /sbin/init splash
  root           2  0.0  0.0      0     0 ?        S    Nov28   0:00 [kthreadd]
  root           3  0.0  0.0      0     0 ?        S    Nov28   0:00 [pool_workqueue_release]
  root           4  0.0  0.0      0     0 ?        I<   Nov28   0:00 [kworker/R-kvfree_rcu_reclaim]
  root           5  0.0  0.0      0     0 ?        I<   Nov28   0:00 [kworker/R-rcu_gp]
  root           6  0.0  0.0      0     0 ?        I<   Nov28   0:00 [kworker/R-sync_wq]
  root           7  0.0  0.0      0     0 ?        I<   Nov28   0:00 [kworker/R-slub_flushwq]
  root           8  0.0  0.0      0     0 ?        I<   Nov28   0:00 [kworker/R-netns]
  root          13  0.0  0.0      0     0 ?        I<   Nov28   0:00 [kworker/R-mm_percpu_wq]
  root          14  0.0  0.0      0     0 ?        I    Nov28   0:00 [rcu_tasks_kthread]
  root          15  0.0  0.0      0     0 ?        I    Nov28   0:00 [rcu_tasks_rude_kthread]
  root          16  0.0  0.0      0     0 ?        I    Nov28   0:00 [rcu_tasks_trace_kthread]
  root          17  0.0  0.0      0     0 ?        S    Nov28   0:00 [ksoftirqd/0] ....
``
## explanation of columns
**USER**: User who started the process
**PID**: Unique process ID
**%CPU**: CPU usage by the process
**%MEM**: Memory usage by the process
**COMMAND**: Command that started the process


## **3.**
  ``ps aux | grep "string": to Filter by Process Name ``
===> input:
``
 ┌──(kali㉿kali)-[~]
 └─$ ps aux | grep msfconsole
``
===> ouput:
``
  kali        6029 19.7 17.3 1325060 349964 pts/0  Sl+  05:13   0:18 ruby /usr/bin/msfconsole
  kali        6179  0.0  0.1   6528  2316 pts/3    S+   05:14   0:00 grep --color=auto msfconsole
``

## **4.**
  `` top: Finding the Greediest Processes with top ``
===> input:
``
  ┌──(kali㉿kali)-[~]
  └─$ top
`` 
===> output:
``
top - 05:33:58 up 16:24,  1 user,  load average: 0.17, 0.08, 0.02
Tasks: 178 total,   2 running, 176 sleeping,   0 stopped,   0 zombie
%Cpu(s):  1.4 us,  3.8 sy,  0.0 ni, 94.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st 
MiB Mem :   1973.7 total,    430.8 free,   1034.0 used,    727.0 buff/cache     
MiB Swap:    953.7 total,    943.6 free,     10.1 used.    939.6 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                                               
    731 root      20   0  495688 218980  82448 S   7.6  10.8   6:09.32 Xorg                                                                                  
   1626 kali      20   0  658528  69596  53580 S   4.3   3.4   0:25.93 qterminal                                                                             
   1293 kali      20   0  886912 123176  80724 R   1.0   6.1   2:07.79 xfwm4                                                                                 
   1215 kali      20   0  215384   2972   2676 S   0.7   0.1   2:12.26 VBoxClient                                                                            
   1351 kali      20   0  296496  50424  23220 S   0.7   2.5   1:32.89 wrapper-2.0 
``
 
"" top shows running processes sorted by resource usage and refreshes every 3 seconds,
   unlike ps which displays only a one-time snapshot.""

** managing Process **

## **5.**
  `` nice: the Priority When Starting a Process ``
## syntax of nice 
   [nice options options process]
  ""The nice command controls how much CPU priority a process gets from the system. 
    Every running process competes for system resources, and nice lets you tell the
    kernel how important a process should be. Nice values range from -20 (highest priority) to +19 (lowest priority),
    with 0 as the default. Regular users can only lower priority (make it “nicer”), while the root user can set any value.""
  ""You can set a process priority when starting it using nice, and you can change the priority of a running process using renice.
    The nice command adds or subtracts from the current priority value (incremental change), while renice sets an exact priority value.
    This difference in syntax often causes confusion for beginners.""
**example**:
``nice -n -10 ruby /usr/bin/msfconsole
   which increses the prioty level by -10``
`` nice -n 10 ruby /usr/bin/msfconsole
  which decrese teh prioty level by 10 ``


## **6.**
  `` renice: to Change the Priority of a Running Process.``
## syntax of renice
   [ renice number pid ]
 "" The renice command sets a process priority to an exact value between -20 and 19 instead of adjusting it incrementally.
    It requires the PID (not the process name) to target a running process. 
    For example, if slowprocess has PID 6996 and is using too many resources, increasing its nice value will lower its priority and free resources for other processes.""
 ** example **
`` renice 19 9082 ``

 ""Only the root user can set a negative nice value (increase priority) with renice, while any user can lower a process priority by giving it a higher nice value.""
 ""Using top, you can change a process priority by pressing R, then entering the PID and the new nice value while the utility is running.""

## **7.**
 `` kill: to kill the process ``
  ""A process that uses excessive resources, behaves abnormally, or causes the system to freeze is known as a rogue process.""
  ""Use the kill command to stop a problematic process by sending it a signal using its PID. It supports many kill signals (64 total),
    each with a different effect, and if no signal is specified, it defaults to SIGTERM.""
  ** 5 important signals**
| Signal Name | Number | Description                                                            |
| ----------- | ------ | ---------------------------------------------------------------------- |
| **SIGHUP**  | 1      | Stops the process and restarts it with the same PID.                   |
| **SIGINT**  | 2      | Interrupt signal; a soft kill that may not always stop the process.    |
| **SIGQUIT** | 3      | Terminates the process and creates a memory dump file named `core`.    |
| **SIGTERM** | 15     | Default kill signal; asks the process to terminate gracefully.         |
| **SIGKILL** | 9      | Forcefully kills the process and cannot be ignored, or blocked |
 
===> input:
``
  ┌──(kali㉿kali)-[~]
  └─$ kill -1 4116 
``
===> input: 
   ``                                                                                            
┌──(kali㉿kali)-[~]
└─$ kill -9 msfconsole
   ``
"" if we do not know the pid number of a process ""

** Running Processes in the Background **
## **8.**
  `` process &: run a process in the background``
===> input:
``
  ┌──(kali㉿kali)-[~]
  └─$ mousepad &                   
  [1] 4667
``

## **9.**
  `` fg pid: Moving a Process to the Foreground``
===> input: 
``
  ┌──(kali㉿kali)-[~]
  └─$ fg 4697 
``
===>
`` 
  ┌──(kali㉿kali)-[~]
  └─$ 
   [1]  + done       mousepad
""
## Scheduling Processes
"" In Linux, tasks can be scheduled using at and crond. The at command schedules a job to run once at a 
   specific time using the atd daemon, while crond is used to schedule recurring tasks daily, weekly, or monthly. ""
===> input:
`` 
   ┌──(kali㉿kali)-[~]
└─$ at 7.30
warning: commands will be executed using /bin/sh
at Sun Nov 30 07:30:00 2025
at> 
``
** some examples of at command **

| Time Format           | Meaning                    |
| --------------------- | -------------------------- |
| `at 7:20pm`           | Runs at 7:20 PM today      |
| `at 7:20pm June 25`   | Runs at 7:20 PM on June 25 |
| `at noon`             | Runs at noon today         |
| `at noon June 25`     | Runs at noon on June 25    |
| `at tomorrow`         | Runs tomorrow              |
| `at now + 20 minutes` | Runs 20 minutes from now   |
| `at now + 10 hours`   | Runs 10 hours from now     |

```

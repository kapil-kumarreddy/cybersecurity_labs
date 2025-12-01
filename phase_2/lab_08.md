
```
## phase_2 ## lab_08.md
** book **: ""Occupytheweb - Linux Basics for Hackers""
** objective **: Learn how to read, monitor, and analyze system logs to detect attacks, failures, and suspicious behavior.
** chapter **: ""the loggig system""
"" Linux records system events using the **syslog daemon**, and Kali Linux uses **rsyslog** by default since it is based on Debian;
   while other versions like **syslog-ng** exist, they work similarly with minor differences.""
  ** rsyslog logging deamon **
""the rsyslog logging software is deamon which runs in our computer to log the actions or events with in our computer.""
  === the rsyslog configration file ===
"" every linux application has rsyslog which manages and configures every action in the form of plaintext configuration file located grenrally in /etc directory ""
  ""let's see an example""
 /etc/rsyslog.conf configuration file for rsyslog
====================================================================
#
# For more information install rsyslog-doc and see
# /usr/share/doc/rsyslog-doc/html/configuration/index.html


#################
#### MODULES ####
#################

module(load="imuxsock") # provides support for local system logging
module(load="imklog")   # provides kernel logging support
#module(load="immark")  # provides --MARK-- message capability

# provides UDP syslog reception
#module(load="imudp")
#input(type="imudp" port="514")

# provides TCP syslog reception
#module(load="imtcp")
#input(type="imtcp" port="514")


###########################
#### GLOBAL DIRECTIVES ####
###########################

#
# Set the default permissions for all log files.
#
$FileOwner root
$FileGroup adm
$FileCreateMode 0640
$DirCreateMode 0755
$Umask 0022

#
# Where to place spool and state files
#
$WorkDirectory /var/spool/rsyslog

#
# Include all config files in /etc/rsyslog.d/
#
$IncludeConfig /etc/rsyslog.d/*.conf


###############
#### RULES ####
###############

#
# Log anything besides private authentication messages to a single log file
#
*.*;auth,authpriv.none		-/var/log/syslog

#
# Log commonly used facilities to their own log file
#
auth,authpriv.*			/var/log/auth.log
cron.*				-/var/log/cron.log
kern.*				-/var/log/kern.log
mail.*				-/var/log/mail.log
user.*				-/var/log/user.log

#
# Emergencies are sent to everybody logged in.
#
*.emerg				:omusrmsg:*

=======================================================================

""as we can see this rsyslog.conf file which has rule on how to manage and configure logs.""
""as we can also see comments which describes the use of this file."" 

## but we need to focus on rules ##

=======================================================================
#
*.*;auth,authpriv.none		-/var/log/syslog

#
# Log commonly used facilities to their own log file
#
auth,authpriv.*			/var/log/auth.log
cron.*				-/var/log/cron.log
kern.*				-/var/log/kern.log
mail.*				-/var/log/mail.log
user.*				-/var/log/user.log

#
# Emergencies are sent to everybody logged in.
#
*.emerg				:omusrmsg:*

======================================================================

""each line here say what type and where logs are managed and configured""
"" let's see the syntax of this rules""
----------------------------------------------------------------------
facility.priority        action
----------------------------------------------------------------------
==============================facility===============================
 **facility** here refers to program such as mail, kernel whose  actions needed to be logged.
 **priority** tells to the rsyslog what type of logs need to be logged from a particular program.
 **action**   tells to rsyslog where to store the logs

---------------------------------------------------------------------

The following is a list of valid codes that can be used in place of the
facility keyword in our configuration file rules:
**auth**, authpriv Security/authorization messages
**cron** Clock daemons
**daemon** Other daemons
**kern** Kernel messages
**lpr** Printing system
**mail** Mail system
**user** Generic user-level messages

---------------------------------------------------------------------
==========================priority==================================
"" An asterisk wildcoard "*" in the place of word refer to the all.
   for example *.priority meaning log every programming.""
""The priority level controls which messages are logged, ranging from debug (lowest) to panic (highest).
   Using * logs all messages, and selecting a specific level (like alert) logs that level and higher-severity messages only.""
-----------------------------------------------------------------------

Here’s the full list of valid codes for priority:
•	 **debug**
•	 **info**
•	 **notice**
•	 **warning**
•	 **warn**
•	 **error**
•	 **err**
•	 **crit**
•	 **alert**
•	 **emerg**
•	 **panic**

----------------------------------------------------------------------

===============================action================================
 ""action gernally a file name where the log are stored.""
 ""Log files are usually stored in the /var/log directory and named after the service or facility that 
   created them (for example, auth.log for authentication logs).""
""for example logs genrated by auth will be stored in file named ""var/log/auth.log""
""let's see a example for logging mail""
---------------------------------------------------------------------
  ``mail.*   var/log/mail 
----------------------------------------------------------------------


** cleaning up logs with logrotate **
""Log files can fill up your hard drive if they are not managed, but deleting them too often removes important history needed for troubleshooting. 
  The logrotate tool solves this by rotating logs—archiving old log files and creating new ones automatically. 
  Old logs are deleted after a set time to free space. Log rotation runs automatically through a cron job, and you can configure it in /etc/logrotate.conf.""

=============================================================================
# see "man logrotate" for details

# global options do not affect preceding include directives

# rotate log files weekly
weekly

# keep 4 weeks worth of backlogs
rotate 4

# create new (empty) log files after rotating old ones
create

# use date as a suffix of the rotated file
#dateext

# uncomment this if you want your log files compressed
#compress

# packages drop log rotation information into this directory
include /etc/logrotate.d

# system-specific logs may also be configured here.
==========================================================================


""Log rotation is controlled using a time unit, which is set to weekly by default, meaning all rotation numbers are in weeks. 
  By default, logs rotate every 4 weeks, but you can change this value—set rotate 1 for weekly cleanup, rotate 26 to keep logs for six months, or rotate 52 to keep logs for one year.
  When logs rotate, a new empty log file is created and old ones can be compressed.
  Each old file is renamed in sequence (e.g., auth.log → auth.log.1 → auth.log.2), and once the maximum number is reached, the oldest log is deleted automatically.""
""During log rotation, old log files are renamed in sequence (e.g., auth.log → auth.log.1 → auth.log.2), and once the maximum number is reached (like .4), 
  the oldest file is deleted instead of creating a new one.""
  **example**
--------------------------------------------------------------------------
kali >ls /var/log/auth.log*
/var/log/auth.log.1
/var/log/auth.log.2
/var/log/auth.log.3
/var/log/auth.log.4
--------------------------------------------------------------------------

** removing evidence **

## 1.
  `` shred: Overwrite the specified FILE(s) repeatedly in order to make it harder ``
## syntax of the shred:
 [ shred options options filename ]
## about shred command :
""The shred command permanently deletes a file by overwriting it multiple times (default is 4), making recovery difficult. 
""More overwrites increase security but also increase time for large files.
""The -f option forces permission changes if needed, and the -n option sets how many overwrite passes to use (for example, 10 times for strong deletion).
===> input
┌──(kali㉿kali)-[/etc]
└─$ shred -f -n 10 /var/log/kakka.log !!** warning when using this command**!!

""this command shred the file kakka.log by overwritting it by 10 times and -f takes care of perimisson while overwritting the file""

""Cybersecurity Relevance: shred helps defenders securely delete sensitive data. Attackers may misuse it to destroy evidence after compromise.""
**disable logging**

`` service rsyslog stop `` !!** warning when using this command **!!
""now the linux system stops the logging service until the service is restarted, making us to operate without any evidence""
```




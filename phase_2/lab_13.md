```
## **Phase 2 – Lab 13**
## Text Processing & Log Analysis (Foundations)

**Book:** Linux Basics for Hackers – OccupyTheWeb
**Objective:** Learn how to extract, filter, and analyze text and log files using core 
               linux commands.

1.
   ``cut -d" " -f1 /var/log/auth.log | head``

===> input:
``┌──(kali㉿kali)-[~]
└─$ cut -d" " -f1 /var/log/auth.log |  head |
``
===> output:
``     
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
``                                                                                            

**Explanation**

cut extracts parts of each line
-d" " → space is the delimiter
-f1 → extract the first field (column)
head → show only first few line

**Cybersecurity relevance**

Attack logs are large. cut helps extract timestamps, usernames, or IP fields quickly for analysis.

2.
  ``cut -d" " -f1 /var/log/auth.log | sort | head``

===> inpput:
``┌──(kali㉿kali)-[~]
└─$ cut -d" " -f1 /var/log/auth.log | sort | head
``
===> output:
``
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
``

**Explanation:**

sort arranges output alphabetically
Sorting is required before using **uniq**
**Cybersecurity relevance:**

Sorting logs is essential before counting events like login attempts or errors.


3.
 `` cut -d" " -f1 /var/log/auth.log |sort | uniq -c | head``
===> input:
``
┌──(kali㉿kali)-[~]
└─$ cut -d " " -f1 /var/log/auth.log | sort | uniq -c| head
``
===> output:
``
      1 2025-12-14T00:55:01.380879-05:00
      1 2025-12-14T00:55:01.393645-05:00
      1 2025-12-14T01:05:01.453393-05:00
      1 2025-12-14T01:05:01.464878-05:00
      1 2025-12-14T01:09:01.482048-05:00
      1 2025-12-14T01:09:01.485528-05:00
      1 2025-12-14T01:15:01.733799-05:00
      1 2025-12-14T01:15:01.753202-05:00
      1 2025-12-14T01:17:01.763535-05:00
      1 2025-12-14T01:17:01.770359-05:00
``
 
**Explanation:**

uniq -c counts repeated lines
Requires sorted input

**Cybersecurity relevance:**
Repeated events can indicate:
brute-force attacks
automated scripts
suspicious activity

4. 
   `` awk '{print $1, $2, $3}' /var/log/auth.log | head``
===> input:
``
┌──(kali㉿kali)-[~]
└─$ awk '{print $1, $2, $3}' /var/log/auth.log | head 
``
===> output:
``
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
``
**Explanation:**

awk works column-by-column
$1 $2 $3 → print first three fields (date/time)

*Cybersecurity relevance**

awk is heavily used in SOC log parsing and incident response to extract meaningful data.

5. 
  ``awk '/Failed/ {count++} END {print count} /var/log/auth.log``
===> input:
``
┌──(kali㉿kali)-[~]
└─$ awk '/Failed/ {count++} END {print count}' /var/log/auth.log
``
===> output:
``
7
``

**Explanation:**

/Failed/ → search lines containing “Failed”
{count++} → increment counter
END → print result after file ends

**Cybersecurity relevance:**

Directly useful for detecting failed authentication attempts and possible attacks.

6. 
   ``sed 's/Failed/FAILED_LOGIN/g' /var/log/auth.log``
===> input:
``┌──(kali㉿kali)-[~]
└─$ sed 's/Failed/FAILED_LOGIN/g' /var/log/auth.log | head 
``
===> output:
``
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
``
**Explanation**

s → substitute
Failed → word to replace
FAILED_LOGIN → replacement
g → replace all matches in line

**Cybersecurity relevance**

sed is used to sanitize logs, normalize data, or prepare evidence for reports.

=====================================end_of_lab_13======================================
```

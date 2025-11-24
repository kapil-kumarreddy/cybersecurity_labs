
```
## phase_2 lab_05
**book** : ""Occupytheweb - Linux Basics for Hackers""
**objective**:Learn basic Linux text-manipulation commands from Chapter 2 to view, search, and process text files for cybersecurity use.
**text maniplation**
"""we are runing our commands on ``/etc/snort/snort.lua``
   which is file from snort library."""
## **1.**
   `` cat: to display text files``
""" let's discuss about syntax of cat
   [ cat filename]
]
* filename : desired file or path 
===> input:
``┌──(kali㉿kali)-[/etc/snort]
   └─$ cat snort.lua
``
===> output:
``
   ---------------------------------------------------------------------------
   -- Snort++ configuration
   ---------------------------------------------------------------------------

   -- there are over 200 modules available to tune your policy.
   -- many can be used with defaults w/o any explicit configuration.
   -- use this conf as a template for your specific configuration.

   -- 1. configure defaults
   -- 2. configure inspection
   -- 3. configure bindings
``
** Cybersecurity Relevance**

* Used to quickly inspect log files, malware scripts, and config files during investigations.


## **2.**
    `` head : shows first 10 lines of desired file``
## let's discuss about the syntax of head
   [ head filename]
* filename : desired file or path 
====> input:
``┌──(kali㉿kali)-[/etc/snort]
   └─$ head snort.lua``
====> output:
``
---------------------------------------------------------------------------
-- Snort++ configuration
---------------------------------------------------------------------------

-- there are over 200 modules available to tune your policy.
-- many can be used with defaults w/o any explicit configuration.
-- use this conf as a template for your specific configuration.

-- 1. configure defaults
-- 2. configure inspection
-- 3. configure bindings
``
## if we want to see more lines, enter the  quantity you want with the dash (-) switch after the call to head and before the filename.
""" let's see an example"""
====> input:
 ``┌──(kali㉿kali)-[/etc/snort]
   └─$ head -20 snort.lua``
====> output"
``
   ---------------------------------------------------------------------------
   -- Snort++ configuration
   ---------------------------------------------------------------------------

   -- there are over 200 modules available to tune your policy.
   -- many can be used with defaults w/o any explicit configuration.
   -- use this conf as a template for your specific configuration.

   -- 1. configure defaults
   -- 2. configure inspection
   -- 3. configure bindings
   -- 4. configure performance
   -- 5. configure detection
   -- 6. configure filters
   -- 7. configure outputs
   -- 8. configure tweaks

   ---------------------------------------------------------------------------
   -- 1. configure defaults
   ---------------------------------------------------------------------------
``
**Cybersecurity Relevance**

* Helps check header sections of logs/configs which often contain important security settings.


## **3.**
  `` tail : to show last 10 lines of a file``
## let's discuss about the syntax of tail
    [ tail filename]
* filename : desired file or path 
====> input:
 ``┌──(kali㉿kali)-[/etc/snort]
   └─$ tail snort.lua``
====> output:
`` 
   --file_log = { }

   ---------------------------------------------------------------------------
   -- 8. configure tweaks
   ---------------------------------------------------------------------------
   x
   if ( tweaks ~= nil ) then
       include(tweaks .. '.lua')
   end
``
## As with head you can ask any number lines same with tail,  enter the quantity you want with the dash (-) switch after the call to tail and before the filename.

**Cybersecurity Relevance**

* Essential for monitoring live logs like /var/log/auth.log to detect brute-force or SSH attacks

## **4.**
   `` nl : To display a file with line numbers``
""" let's discuss about the syntax of nl"""
       [ nl filename]
====> input:
``┌──(kali㉿kali)-[/etc/snort]
   └─$ nl snort.lua
``
====> output"
``
     1  ---------------------------------------------------------------------------
     2  -- Snort++ configuration
     3  ---------------------------------------------------------------------------
       
     4  -- there are over 200 modules available to tune your policy.
     5  -- many can be used with defaults w/o any explicit configuration.
     6  -- use this conf as a template for your specific configuration.
       
     7  -- 1. configure defaults
     8  -- 2. configure inspection
     9  -- 3. configure bindings
    10  -- 4. configure performance
    11  -- 5. configure detection
    12  -- 6. configure filters
    13  -- 7. configure outputs
    14  -- 8. configure tweaks
       
    15  ---------------------------------------------------------------------------
    16  -- 1. configure defaults
    17  ---------------------------------------------------------------------------
       
    18  -- HOME_NET and EXTERNAL_NET must be set now
    19  -- setup the network addresses you are protecting
    20  HOME_NET = 'any'
``
**Cybersecurity Relevance**

* Line numbers help reference exact log entries during incident reports and attack timeline creati


## **5.**
`` grep : filters the content of file``
""" let's discuss about the syntax of grep"""
    [grep [OPTIONS] PATTERN [FILE...]]
""" A little bit about the grep"""

* Use `grep` with `cat` to filter and display only the lines in a file that contain a specific word.
* For example, `cat snort.conf | grep output` shows only lines containing "output."
* `grep` is a powerful Linux tool that helps quickly locate text within files, saving time during searches.
====> input:
``┌──(kali㉿kali)-[/etc/snort]
  └─$ cat snort.lua | grep output``
===> output:
``
-- 7. configure outputs
-- 7. configure outputs``
**Cybersecurity Relevance**

* Most important log analysis tool; used to find errors, suspicious IPs, malware signatures, and attack traces.

## **6.**
   ``sed : lets you search for occurrences of a word or a text pattern and then perform some action on it.``
""" let's discuss about syntax of sed"""
``sed s/[pattern1]/[pattern2]/g  filename > newfilename]``
====> input:
``
   ┌──(kali㉿kali)-[/etc/snort]
   └─$ sed s/configure/Configure/g snort.lua > /home/kali/Downloads/snort2.lua``
====> output:
``
   ┌──(kali㉿kali)-[~/Downloads]
   └─$ cat snort2.lua | grep Configure
   -- 1. Configure defaults
   -- 2. Configure inspection
   -- 3. Configure bindings
   -- 4. Configure performance
   -- 5. Configure detection
   -- 6. Configure filters
   -- 7. Configure outputs....
``
  **explanation**
* The s command in sed substitutes a search term (configure) with a new term (Configure), using slashes as separators.

* The g flag ensures the replacement is applied globally across the file.

* The updated output is saved to a new file, such as snort2.lua

* Using grep on snort2.lua will now show no results for “configure” but will show occurrences of “Configure.
## """If you wanted to replace only the first occurrence of the term configure, you would leave out the trailing g option."""
**exmaple:**
  ``sed s/configure/Configure/ snort2.lua > /home/kali/Downloads/snort2.lua``
## """Use sed with the occurrence number (e.g., 2) to replace only the second instance of a word instead of all occurrences."
  **example:**
  ``sed s/configure/Configure/2 snort2.lua > /home/kali/Downloads/snort2.lua``
** Cybersecurity Relevance**

* Useful for cleaning logs, extracting indicators, modifying configs, and automating forensic tasks.

## **7.**
  ``more:displays a page of a file at a time and lets you page down through it using the enter key``
""" let's discuss about syntax of more"""
  `` [ more filename] ``
### """more shows only the first page of a file and indicates the viewing progress; press Enter to scroll and q to quit."""
===> input:
``┌──(kali㉿kali)-[/etc/snort]
   └─$ more snort.lua
``
===> output:
``               
---------------------------------------------------------------------
-- Snort++ configuration
---------------------------------------------------------------------------


stream = { }
stream_ip = { }
stream_icmp = { }
stream_tcp = { }
stream_udp = { }
stream_user = { }
stream_file = { }
--More--(17%)
``
**Cybersecurity Relevance**

* Allows quickly scanning large config files (like IDS configs) without loading everything at once.

## **8.**
  `` less: less lets you scroll through a file freely and also search within it for specific terms.``
""" let's discuss about syntax of less """"
  ``[ less filename]``
**less highlights the file path and lets you search within the file using /, offering more features than more — hence the saying, “less is more.”**
===> input:
``
   ┌──(kali㉿kali)-[/etc/snort]
   └─$ less snort.lua
``
===> output:
"" it opened a page. let's serach a word "configure. """
``/configure
   -- 1. configure defaults
   -- 2. configure inspection
   -- 3. configure bindings
   -- 4. configure performance
   -- 5. configure detection
   -- 6. configure filters
   -- 7. configure outputs
   -- 8. configure tweaks

   ---------------------------------------------------------------------------
   -- 1. configure defaults
   ---------------------------------------------------------------------------

   -- HOME_NET and EXTERNAL_NET must be set now
   -- setup the network addresses you are protecting
   HOME_NET = 'any'

   -- set up the external network addresses.
   -- (leave as "any" in most situations)
   EXTERNAL_NET = 'any'
``
**Cybersecurity Relevance**

* Used constantly for searching inside huge security logs during threat hunting and IR (search with /).
""let's continue in next lab""
```

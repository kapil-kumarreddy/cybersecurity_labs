```

**phase_2** **lab_11.md**

**Service Management & System Logging**

**Book reference**:

**OccupyTheWeb** – Linux Basics for Hackers

Concepts align with Service Management and Logging (systemd-based systems)

**Objective**:
Learn how to manage system services and analyze system logs using systemctl and journalctl, which are essential for monitoring, troubleshooting, and incident response in Linux-based systems.

1. systemctl- Managing Service

1.1`systemctl status ssh`:shows us the status of ssh 

===>input:
``
┌──(kali㉿kali)-[~]
└─$ systemctl status ssh
``
===> output:
``      
○ ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/usr/lib/systemd/system/ssh.service; di>
     Active: inactive (dead)
       Docs: man:sshd(8)
             man:sshd_config(5)
lines 1-5/5 (END)
``

**Explanation:**

Loaded → service is installed
Active (running) → service is currently running
enabled → starts automatically at boot

**Cybersecurity relevance**:

Confirms whether remote access (SSH) is active
Attackers often enable or disable services to maintain access

1.2 `sudo systemctl start ssh`

===>output:
``systemctl status ssh    
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/usr/lib/systemd/system/ssh.service; di>
     Active: active (running) since Sun 2025-12-14 02:37:15 >
 Invocation: a4a74c48959f4b029ff586c5feceeefe
       Docs: man:sshd(8)
             man:sshd_config(5)
    Process: 2662 ExecStartPre=/usr/sbin/sshd -t (code=exite>
   Main PID: 2664 (sshd)
      Tasks: 1 (limit: 2208)
     Memory: 5.9M (peak: 6.4M)
        CPU: 34ms
     CGroup: /system.slice/ssh.service
             └─2664 "sshd: /usr/sbin/sshd -D [listener] 0 of>

Dec 14 02:37:15 kali systemd[1]: Starting ssh.service - Open>
Dec 14 02:37:15 kali sshd[2664]: Server listening on 0.0.0.0>
Dec 14 02:37:15 kali sshd[2664]: Server listening on :: port>
Dec 14 02:37:15 kali systemd[1]: Started ssh.service - OpenB>
``

**Explanation:**

Starts the SSH service immediately.
**Cybersecurity relevance:**
Required when enabling secure remote administration
Helps restore critical services during incident recovery

1.3 `sudo systemctl stop ssh`

===>output:
``
ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/usr/lib/systemd/system/ssh.service; di>
     Active: inactive (dead) since Sun 2025-12-14 02:38:31 E>
   Duration: 1min 15.930s
 Invocation: a4a74c48959f4b029ff586c5feceeefe
       Docs: man:sshd(8)
             man:sshd_config(5)
    Process: 2662 ExecStartPre=/usr/sbin/sshd -t (code=exite>
    Process: 2664 ExecStart=/usr/sbin/sshd -D $SSHD_OPTS (co>
   Main PID: 2664 (code=exited, status=0/SUCCESS)
   Mem peak: 6.4M
        CPU: 35ms
``

**Explanation:**
Stops the service until reboot or manual restart.
**Cybersecurity relevance:**
Used to shut down vulnerable or compromised services
Prevents attackers from using exposed services

1.4 `sudo systemctl enable ssh`
===> output:
``
┌──(kali㉿kali)-[~]
└─$ sudo systemctl enable ssh
Synchronizing state of ssh.service with SysV service script with /usr/lib/systemd/systemd-sysv-install.
Executing: /usr/lib/systemd/systemd-sysv-install enable ssh
Created symlink '/etc/systemd/system/sshd.service' → '/usr/lib/systemd/system/ssh.service'.
Created symlink '/etc/systemd/system/multi-user.target.wants/ssh.service' → '/usr/lib/systemd/system/ssh.service'.
``

**Explanation:**
Service starts automatically when the system boots.
**Cybersecurity relevance:**
Ensures security tools (firewall, logging, IDS) always start
Attackers may enable malicious persistence services

1.5 `sudo systemctl disable ssh`

===>output:
``
┌──(kali㉿kali)-[~]
└─$ sudo systemctl disable ssh
Synchronizing state of ssh.service with SysV service script with /usr/lib/systemd/systemd-sysv-install.
Executing: /usr/lib/systemd/systemd-sysv-install disable ssh
Removed '/etc/systemd/system/sshd.service'.
Removed '/etc/systemd/system/multi-user.target.wants/ssh.service'.
``

**Explanation:**

Prevents service from starting automatically.
**Cybersecurity relevance:**

Reduces attack surface
Used in system hardening

2.**journalctl** - system log analysis
journalctl allows querying logs stored by the system.

2.1 `journalctl`

===> output:
``
Nov 25 03:48:29 kali systemd[1042]: Queued start job for def>
Nov 25 03:48:29 kali systemd[1042]: Created slice app.slice >
Nov 25 03:48:29 kali systemd[1042]: Created slice session.sl>
Nov 25 03:48:29 kali systemd[1042]: Reached target paths.tar>
Nov 25 03:48:29 kali systemd[1042]: Reached target timers.ta>
Nov 25 03:48:29 kali systemd[1042]: Starting dbus.socket - D>
Nov 25 03:48:29 kali systemd[1042]: Listening on dirmngr.soc>
Nov 25 03:48:29 kali systemd[1042]: Listening on gnome-key
``

Explanation:

Displays all logs (oldest first).
**Cybersecurity relevance:**

Central place to inspect system activity
Helps trace attacks and system changes

2.2 `journalctl -xe`

===>output:
``Dec 14 03:05:47 kali kernel: 08:05:47.452307 dnd       No guest source window
Dec 14 03:05:47 kali kernel: 08:05:47.454549 dndHGCM   DnD: Received message HOST_DND_FN_GH_REQ_PENDING (0x258) from host
Dec 14 03:05:47 kali kernel: 08:05:47.455054 dnd       No guest source window
Dec 14 03:05:47 kali kernel: 08:05:47.458414 dndHGCM   DnD: Received message HOST_DND_FN_GH_REQ_PENDING (0x258) from host
Dec 14 03:05:47 kali kernel: 08:05:47.458916 dnd       No guest source window
Dec 14 03:05:47 kali kernel: 08:05:47.462380 dndHGCM   DnD: Received message HOST_DND_FN_GH_REQ_PENDING (0x258) from host
Dec 14 03:05:47 kali kernel: 08:05:47.462826 dnd       No guest source window
Dec 14 03:05:47 kali kernel: 08:05:47.466446 dndHGCM   DnD: Received message HOST_DND_FN_GH_REQ_PENDING (0x258) from host
Dec 14 03:05:47 kali kernel: 08:05:47.467067 dnd       No guest source window
Dec 14 03:05:47 kali kernel: 08:05:47.470420 dndHGCM   DnD: Received message HOST_DND_FN_GH_REQ_PENDING (0x258) from host
Dec 14 03:05:47 kali kernel: 08:05:47.471340 dnd       No guest source window
Dec 14 03:05:47 kali kernel: 08:05:47.474398 dndHGCM   DnD: Received message HOST_DND_FN_GH_REQ_PENDING (0x258) from host
Dec 14 03:05:47 kali kernel: 08:05:47.474941 dnd       No guest source window
Dec 14 03:05:47 kali kernel: 08:05:47.478588 dndHGCM   DnD: Received message HOST_DND_FN_GH_REQ_PENDING (0x258) from host
Dec 14 03:05:47 kali kernel: 08:05:47.479130 dnd       No guest source window
Dec 14 03:05:47 kali kernel: 08:05:47.482518 dndHGCM   DnD: Received message HOST_DND_FN_GH_REQ_PENDING (0x258) from h
``

**Explanation:**

-x → adds explanations
-e → jumps to the end (latest logs)

**Cybersecurity relevance:**

Used during incident response
Quickly identifies errors, crashes, or security issues

2.3 `Journalctl -u ssh`
===> output:
``
Dec 14 02:37:15 kali systemd[1]: Starting ssh.service - Open>
Dec 14 02:37:15 kali sshd[2664]: Server listening on 0.0.0.0>
Dec 14 02:37:15 kali sshd[2664]: Server listening on :: port>
Dec 14 02:37:15 kali systemd[1]: Started ssh.service - OpenB>
Dec 14 02:38:31 kali systemd[1]: Stopping ssh.service - Open>
Dec 14 02:38:31 kali sshd[2664]: Received signal 15; termina>
Dec 14 02:38:31 kali systemd[1]: ssh.service: Deactivated su>
Dec 14 02:38:31 kali systemd[1]: Stopped ssh.service - OpenB>
``
**Explanation:**

Shows logs related only to the SSH service.
**Cybersecurity relevance:**

Detects failed login attempts
Helps identify brute-force attacks

2.4 `journalctl` --since "10 minutes ago"

===>output:
`` Boot 870f7bcf071443869e6a9ec7ff3b375a --
Dec 14 03:19:40 kali systemd[1091]: Starting xfconfd.service - Xfce configuration service.>
-- Boot 74968f79df8b444186ec847bcf6e5a9a --
Dec 14 03:20:32 kali kernel: Command line: BOOT_IMAGE=/boot/vmlinuz-6.12.38+kali-amd64 roo>
-- Boot 870f7bcf071443869e6a9ec7ff3b375a --
Dec 14 03:19:40 kali dbus-daemon[1113]: [session uid=1000 pid=1113 pidfd=5] Successfully a>
-- Boot 74968f79df8b444186ec847bcf6e5a9a --
Dec 14 03:20:32 kali kernel: [Firmware Bug]: TSC doesn't count with P0 frequency!
-- Boot 870f7bcf071443869e6a9ec7ff3b375a --
Dec 14 03:19:40 kali systemd[1091]: Started xfconfd.service - Xfce configuration service.
-- Boot 74968f79df8b444186ec847bcf6e5a9a --
Dec 14 03:20:32 kali kernel: BIOS-provided physical RAM map:
Dec 14 03:20:32 kali kernel: BIOS-e820: [mem 0x0000000000000000-0x000000000009fbff] usable
Dec 14 03:20:32 kali kernel: BIOS-e820: [mem 0x000000000009fc00-0x000000000009ffff] reserv>
Dec 14 03:20:32 kali kernel: BIOS-e820: [mem 0x00000000000f0000-0x00000000000fffff] reserv>
Dec 14 03:20:32 kali kernel: BIOS-e820: [mem 0x0000000000100000-0x000000007ffeffff] usable
Dec 14 03:20:32 kali kernel: BIOS-e820: [mem 0x000000007fff0000-0x000000007fffffff] ACPI d>
Dec 14 03:20:32 kali kernel: BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserv>
Dec 14 03:20:32 kali kernel: BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserv>
Dec 14 03:20:32 kali kernel: BIOS-e820: [mem 0x00000000fffc0000-0x00000000ffffffff] reserv>
Dec 14 03:20:32 kali kernel: NX (Execute Disable) protection: active
Dec 14 03:20:32 kali kernel: APIC: Static calls initialized
Dec 14 03:20:32 kali kernel: SMBIOS 2.5 present.
Dec 14 03:20:32 kali kernel: DMI: innotek GmbH VirtualBox/VirtualBox, BIOS VirtualBox 12/0>
Dec 14 03:20:32 kali kernel: DMI: Memory slots populated: 0/0
Dec 14 03:20:32 kali kernel: Hypervisor detected: KVM
``
Explanation:

Filters logs based on time.
Cybersecurity relevance:

Useful during real-time investigations
Helps correlate events after alerts
2.5 `journalctl -b`

===>output:
``3:20:32 kali kernel: kvm-clock: using sched offset of 11752130753 cycles
Dec 14 03:20:32 kali kernel: clocksource: kvm-clock: mask: 0xffffffffffffffff max_cycles: >
Dec 14 03:20:32 kali kernel: tsc: Detected 3792.934 MHz processor
Dec 14 03:20:32 kali kernel: e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
Dec 14 03:20:32 kali kernel: e820: remove [mem 0x000a0000-0x000fffff] usable
Dec 14 03:20:32 kali kernel: last_pfn = 0x80000 max_arch_pfn = 0x400000000
Dec 14 03:20:32 kali kernel: MTRR map: 3 entries (3 fixed + 0 variable; max 19), built fro>
Dec 14 03:20:32 kali kernel: x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
Dec 14 03:20:32 kali kernel: CPU MTRRs all blank - virtualized system.
Dec 14 03:20:32 kali kernel: found SMP MP-table at [mem 0x0009fbf0-0x0009fbff]
Dec 14 03:20:32 kali kernel: RAMDISK: [mem 0x28385000-0x301b9fff]
Dec 14 03:20:32 kali kernel: ACPI: Early table checksum verification disabled
Dec 14 03:20:32 kali kernel: ACPI: RSDP 0x00000000000E0000 000024 (v02 VBOX  )
Dec 14 03:20:32 kali kernel: ACPI: XSDT 0x000000007FFF0030 00003C (v01 VBOX   VBOXXSDT 000>
Dec 14 03:20:32 kali kernel: ACPI: FACP 0x000000007FFF00F0 0000F4 (v04 VBOX   VBOXFACP 000>
Dec 14 03:20:32 kali kernel: ACPI: DSDT 0x000000007FFF02F0 002353 (v02 VBOX   VBOXBIOS 000>
Dec 14 03:20:32 kali kernel: ACPI: FACS 0x000000007FFF0200 000040
Dec 14 03:20:32 kali kernel: ACPI: FACS 0x000000007FFF0200 000040
Dec 14 03:20:32 kali kernel: ACPI: APIC 0x000000007FFF0240 00005C (v02 VBOX   VBOXAPIC 000>
lines 1-38
``

**Explanation**:

Shows logs since the last system boot.
**Cybersecurity relevance:**

Helps analyze what happened after reboot
Useful if compromise occurred recently

2.6 `journalctl -f`

**Explanation:**

Continuously displays new log entries (like tail -f).
**Cybersecurity relevance:**

Live monitoring during attacks or testing
Useful while starting/stopping services

```


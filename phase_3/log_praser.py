import re
AFLp = re.compile(r"authentication failure")
SFTPAp = re.compile(r"ftpd\[[0-9]+\]: connection from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
AFLlist =[]
SFTPAlist = []
suspicious_ip = {}
log_file = "/home/kali/cyberprojects/Linux_Log_Forensics_Tool/dataset/authreal.log"
with open(log_file, "r") as file:
    for line in file:
        if AFLp.search(line):
           AFLlist.append(line)
        if SFTPAp.search(line):
           SFTPAlist.append(line)
AFLc = len(AFLlist)
SFTPAc = len(SFTPAlist)                      
print("number of authentication failure logins:", AFLc) 
print("number of FTP connections buffering:", SFTPAc)
def extracting_ip_address_of_brute_force(AFLlist):
    pre_IP_address = None
    pre_Timestamp = None
    count = 0
    IP_address_list = []
    for line in AFLlist:
        timestamp = re.findall(r"[A-Za-z]+\s+\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}", line)
        IP_address = re.findall("rhost=([^ ]*)", line)
        if count == 1:
            time_at_which_attack_started = timestamp[0]
        if IP_address[0] == pre_IP_address:
            count = count + 1
        else:
  
            if count > 5:
                  IP_address_list.append(IP_address[0])
                  IP_address_count = IP_address_list.count(IP_address[0])
                  IP_address_count_number = IP_address_count , "time" , IP_address[0]
                  suspicious_ip[IP_address_count_number] = [IP_address[0], "attemted brute force attack " , count , "times at",  time_at_which_attack_started]
            count = 1
            pre_IP_address = IP_address[0]    
    print(suspicious_ip)
def extracting_ip_address_of_FTP_attack(SFTPAlist):
    pre_IP_address_of_FTP = None
    pre_Timestamp_of_FTP = None
    count = 0
    FTP_IP_address_list = []
    FTP_DICT = {}
    for line in SFTPAlist:
        IP_address_of_ftp = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        timestamp_of_ftp = re.findall(r"[A-Za-z]+\s+\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}", line)
        if count == 1:
            time_at_which_attack_started = timestamp_of_ftp[0]
        if IP_address_of_ftp[0] == pre_IP_address_of_FTP:
            count = count + 1
        else:
            if count > 5:
                 FTP_IP_address_list.append(IP_address_of_ftp[0])
                 FTP_IP_address_count = FTP_IP_address_list.count(IP_address_of_ftp[0])
                 FTP_IP_address_count_number = FTP_IP_address_count , "time",  IP_address_of_ftp[0]
                 FTP_DICT[FTP_IP_address_count_number , "time" , IP_address_of_ftp[0]] = [IP_address_of_ftp[0] , 'tried to hava a ftp connection', count ,'times at' , timestamp_of_ftp[0]]
            count = 1
            pre_IP_address_of_FTP = IP_address_of_ftp[0]
    print(FTP_DICT)
    
def main():         
     extracting_ip_address_of_brute_force(AFLlist) 
     extracting_ip_address_of_FTP_attack(SFTPAlist) 

print(main())
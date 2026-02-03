## TCP_client
import socket

target_host = "0.0.0.0"
for target_port in range(1, 1025):
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client.settimeout(1)
   try:
       client.connect((target_host, target_port))
       print(f"[+] {target_port} OPEN")
   except socket.timeout:
       print(f"[?] port {target_port} FILTERED (timeout)") 
   except ConnectionRefusedError: 
      print(f"[-] port {target_port} CLOSED")
   except Exception as e:
       print(f"[!] port {target_port} error : {e}")      
   finally:
       client.close()    
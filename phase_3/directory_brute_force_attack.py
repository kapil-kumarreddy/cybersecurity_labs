
import sys
import os
import threading
import contextlib
import queue
import time
import requests
## GET request

import urllib.parse
import urllib.request
url = "https://httpbin.org/html"
with urllib.request.urlopen(url) as response:
    content = response.read()
print(content)

# POST request
info ={"usename" : "mani", "userid":"2"}
data = urllib.parse.urlencode(info).encode()
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    content = response.read()
print(response)    

# using request library to reqwuest
import requests
url = "https://httpbin.org/html"
response = requests.get(url)
print(response.text)
info ={"usename" : "mani", "userid":"2"}
response = requests.POST(url, data=data)
print(response.text)

#Directory_brute_force_attack

FILTERED = [".jpg", ".css", ".png", ".gif"]
url = "https://juice-shop.herokuapp.com/"
Threads = 10
Answered = queue.Queue()
Web_paths = queue.Queue()
def gather_paths():
    for root, _, files in os.wall("."):
        for fname in files:
            if os.path.splitext(fname)[1] in FILTERED:
                continue
            path = os.path.join(root, fname)
            if path.startwith("."):
                path = path[1:]
            print(path) 
            Web_paths.put(path) 
def chdir(path):
    """
    On enter, change directory to specified path.
    On exit, change directory back to original.
    """       
    this_dir = os.getcwd()    
    os.chdir(path)  
    try:
        yield
    finally:
        os.chdir(this_dir)    
if __name__ == "__main__":
   with chdir(""):
       gather_paths()
   input("please return to contiune")    
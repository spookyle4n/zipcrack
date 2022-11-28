from random import seed
from random import randint
import time, random, string, maskpass
print('''
\033[36m
.▄▄ · ▄▄· ▄ .▄         ▄▄▌       ▄▄ • ▄· ▄▌    ▄ •▄▪ ▄▄▌ ▄▄▌ ▄▄▄ ▄▄▄  
▐█ ▀.▐█ ▌██▪▐▪    ▪    ██• ▪    ▐█ ▀ ▐█▪██▌    █▌▄▌████• ██• ▀▄.▀▀▄ █·
▄▀▀▀███ ▄██▀▐█▄█▀▄ ▄█▀▄██▪  ▄█▀▄▄█ ▀█▐█▌▐█▪    ▐▀▀▄▐███▪ ██▪ ▐▀▀▪▐▀▀▄ 
▐█▄▪▐▐█████▌▐▐█▌.▐▐█▌.▐▐█▌▐▐█▌.▐▐█▄▪▐█▐█▀·.    ▐█.█▐█▐█▌▐▐█▌▐▐█▄▄▐█•█▌
 \033[37m▀▀▀▀·▀▀▀▀▀▀ ·▀█▄▀▪▀█▄▀.▀▀▀ ▀█▄▀·▀▀▀▀  ▀ •     ·▀  ▀▀.▀▀▀.▀▀▀ ▀▀▀.▀  ▀

               coded by wyatt g
               \033[36m
               
''')
z = random.randint(0, 8)
e = input("[?] Your schoology email: ")
pwd = maskpass.askpass("[?] Your schoology password: ", mask="") 
print("[*] attempting to log into schoology with... " + e)
time.sleep(z)
print("\033[32m\t> successfully logged in as " + e + " [\u2713]")

c = input("\033[36m[?] Victims schoology email?: ")
b = int(input("[?] How many passwords would you like to try?: "))
a = input("[?] Start Attack? [y/n]: ")
if a == 'y':
    print("\033[31m[!] Starting bruteforce on " + c)
    time.sleep(z)
    for i in range(b):
        randomnumber = chr(random.randint(ord('0'), ord('9')))
        randomnumber2 = chr(random.randint(ord('0'), ord('9')))
        randomnumber3 = chr(random.randint(ord('0'), ord('9')))
        randomnumber4 = chr(random.randint(ord('0'), ord('9')))
        randomnumber5 = chr(random.randint(ord('0'), ord('9')))
        randomnumber6 = chr(random.randint(ord('0'), ord('9')))
        randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
        randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
        if randomnumber + randomnumber2 + randomUpperLetter + randomLowerLetter == '39Qh':
            print("\033[32m[+] password 39Qh\nsuccess! [\u2713] ")
            print("schoology email: " + c)
            print("schoology password: 39Qh")
            time.sleep(100000000)
            
        print("\033[31m[+] bruting: " + randomnumber + randomnumber2 + randomUpperLetter + randomLowerLetter, flush=True)
        time.sleep(0.000001)

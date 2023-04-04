from subprocess import call
from pyfiglet import print_figlet
from colorama import Fore

colors = "139;0;139"
color = "186;85;211"

print_figlet(" W V S      ", font="banner3-D", colors=colors)
print_figlet(" website vulnerability scanner ", font="digital", colors=color)

print(Fore.YELLOW + "1)XSS")
print(Fore.YELLOW + "2)SQLi")
print(Fore.YELLOW + "3)IP FINDER")
print(Fore.YELLOW + "4)PORT SCANNER")
# print(Fore.CYAN + "\n                              (-h) for help ")

i = input(Fore.BLUE + "\n select options:")
if i == "1":
    call(["python", "xss.py"])
elif i == "2":
    call(["python", "scan.py"])
elif i == "3":
    call(["python", "ip.py"])
elif i == "4":
    call(["python", "port_scanner.py"])
# elif i == "-h":
# call(["python", "help.py"])
else:
    print(Fore.RED + "\nINVALID OPTION")

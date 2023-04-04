from subprocess import call
from colorama import Fore

url_ip = input(Fore.GREEN+"Enter the ip / domain name: \n ")


def nmap():
    call(["nmap", "-F", url_ip])
    pass


nmap()

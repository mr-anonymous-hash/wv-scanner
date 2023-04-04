from subprocess import call
from colorama import Fore

url: str = input(Fore.GREEN + "Enter the url:")
print(Fore.LIGHTGREEN_EX + "\nip address for the given url :")


def ip_address():
    call(["host", url])
    pass


ip_address()

#!/usr/bin/env python
import subprocess as sub
import optparse
import re


# changing mac address
def mac_changer(interface, mac_address):
    sub.call(["ifconfig", interface, "down"])
    sub.call(["ifconfig", interface, "hw", "ether", mac_address])
    sub.call(["ifconfig", interface, "up"])

    print("[+] Changing MAC address for " + interface + " to " + mac_address)


# To use external functions before executing the code
def parsing_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Enter interface name")
    parser.add_option("-m", "--mac", dest="mac_address", help="Enter mac address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Interface device is missing, use --help for more info")
    elif not options.mac_address:
        parser.error("[-] Mac address is missing, use --help for more info")

    return options


def get_current_mac(interface):
    ifconfig_result = sub.check_output(["ifconfig", interface])
    mac_pattern_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_pattern_search:
        return mac_pattern_search.group(0)
    else:
        print("[-] Could not read MAC address")


options = parsing_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
mac_changer(options.interface, options.mac_address)

current_mac = get_current_mac(options.interface)

if current_mac == options.mac_address:
    print("[+] MAC address successfully changed to " + current_mac)
else:
    print("[-] MAC address was not changed")

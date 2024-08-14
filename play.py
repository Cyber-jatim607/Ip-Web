#!/bin/usr/python

# color
blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'

# module
import os,sys,time
import socket

# tampilan
time.sleep(1)
os.system("clear")
time.sleep(1)
print("\033[34;1m")
os.system("figlet ip-web")
time.sleep(1)
print()
print("\033[31;1m ==========================================")
print("\033[32;1m (•) Author : MR TEKNO VRS")
print("\033[32;1m (•) Team   : Preman Cyber I")
print("\033[31;1m ==========================================")
print()
time.sleep(1)
print("\033[32;1m enter a domain name")
time.sleep(1)
print("\033[34;1m")
hostname = input(" ==> ")
ip_address = socket.gethostbyname(hostname)
print("\033[31;1m")

print(f' Domain Name: {hostname}')
print(f'\033[34;1m IP Address: {ip_address}')
print("\033[32;1m =============================")

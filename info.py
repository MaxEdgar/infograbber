import socket
import platform
import os
import requests
import glob
import geocoder
from scapy.all import *

def get_host_info():
    # Hostname
    hostname = socket.gethostname()
    print("Hostname:", hostname)
    
    # Operating System
    os_info = platform.system() + " " + platform.release()
    print("Operating System:", os_info)
    
    # Local IP
    local_ip = socket.gethostbyname(hostname)
    print("Local IP Address:", local_ip)
    
    # Public IP
    try:
        public_ip = requests.get('https://api.ipify.org').text
        print("Public IP Address:", public_ip)
    except requests.RequestException:
        print("Public IP Address: Unable to retrieve")

def get_wifi_ssid():
    try:
        # Scan for Wi-Fi SSID using scapy
        def PacketHandler(pkt):
            if pkt.haslayer(Dot11Beacon):
                ssid = pkt[Dot11Elt].info.decode()
                print("Connected Wi-Fi SSID:", ssid)
        
        sniff(iface="wlan0", prn=PacketHandler, timeout=5)
    except Exception as e:
        print("Wi-Fi SSID: Unable to retrieve")

def get_gps_location():
    try:
        # Retrieve GPS coordinates
        g = geocoder.ip('me')
        print("Latitude:", g.latlng[0])
        print("Longitude:", g.latlng[1])
    except:
        print("GPS Coordinates: Unable to retrieve")

def list_directories(path):
    print("\nDirectory Listing for", path)
    files = glob.glob(path + '/**', recursive=True)
    for file in files:
        print(file)

# Run all functions
print("=== Host Information ===")
get_host_info()
print("\n=== Wi-Fi SSID ===")
get_wifi_ssid()
print("\n=== GPS Location ===")
get_gps_location()
print("\n=== Directory Listing ===")
list_directories("/")  # Change "/" to specific directory if needed

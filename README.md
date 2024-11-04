<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python System Information Script Tutorial</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #333;
        }
        pre {
            background-color: #e2e2e2;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>

<h1>Python System Information Script Tutorial</h1>

<p>This tutorial will guide you through the process of creating and running a Python script that collects various system information, including the hostname, operating system, local and public IP addresses, Wi-Fi SSID, GPS location, and a directory listing.</p>

<h2>Prerequisites</h2>
<ul>
    <li>A computer running <strong>Kali Linux</strong> or any Debian-based system.</li>
    <li>Basic knowledge of using the terminal.</li>
    <li>Python 3 installed.</li>
</ul>

<h2>Step 1: Update Your System</h2>
<p>Before starting, ensure your system packages are up to date. Open your terminal and run:</p>
<pre><code>sudo apt update && sudo apt upgrade</code></pre>

<h2>Step 2: Install Required Packages</h2>
<ol>
    <li><strong>Install Python3 and pip</strong> if they aren't already installed:
        <pre><code>sudo apt install python3 python3-pip</code></pre>
    </li>
    <li><strong>Install the <code>python3-venv</code> package</strong> to create virtual environments:
        <pre><code>sudo apt install python3-venv</code></pre>
    </li>
    <li><strong>Create a virtual environment</strong>:
        <pre><code>python3 -m venv myenv</code></pre>
    </li>
    <li><strong>Activate the virtual environment</strong>:
        <pre><code>source myenv/bin/activate</code></pre>
    </li>
    <li><strong>Install the necessary Python packages</strong>:
        <pre><code>pip install requests geocoder scapy wifi</code></pre>
    </li>
</ol>

<h2>Step 3: Create the Python Script</h2>
<ol>
    <li><strong>Open a text editor</strong> (like <code>nano</code> or <code>vim</code>) and create a new Python file:
        <pre><code>nano info.py</code></pre>
    </li>
    <li><strong>Copy and paste the following code</strong> into your <code>info.py</code> file:
        <pre><code>import socket
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
list_directories("/")  # Change "/" to specific directory if needed</code></pre>
    </li>
    <li><strong>Save and exit</strong> the editor (for <code>nano</code>, press <code>CTRL + X</code>, then <code>Y</code>, then <code>Enter</code>).</li>
</ol>

<h2>Step 4: Run the Script</h2>
<ol>
    <li><strong>Ensure your virtual environment is activated</strong>. If it’s not activated, run:
        <pre><code>source myenv/bin/activate</code></pre>
    </li>
    <li><strong>Run the script</strong>:
        <pre><code>python3 info.py</code></pre>
    </li>
    <li><strong>View the output</strong>. The script will display your hostname, operating system, local and public IP addresses, Wi-Fi SSID, GPS location, and a directory listing.</li>
</ol>

<h2>Step 5: Deactivate the Virtual Environment (optional)</h2>
<p>When you are finished, you can deactivate the virtual environment by running:</p>
<pre><code>deactivate</code></pre>

<h2>Conclusion</h2>
<p>You have successfully created and run a Python script to gather system information on Kali Linux! Feel free to modify the script as needed and share it with others on GitHub. If you have any questions or issues, don’t hesitate to ask for help!</p>

</body>
</html>

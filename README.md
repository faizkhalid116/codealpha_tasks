# CodeAlpha_BasicNetworkSniffer

Basic Network Sniffer

Project Overview

The Basic Network Sniffer is a Python-based cybersecurity project developed as part of the CodeAlpha Internship.

This tool captures network packets and analyzes basic network traffic to help understand how data travels through a network.

Project Objectives

* Capture network packets.
* Identify source and destination IP addresses.
* Detect network protocols.
* Display source and destination port numbers.
* Display available packet payload data.

Technologies Used

* Python 3
* Scapy Library
* Npcap
* Visual Studio Code

Supported Protocols

* TCP (Transmission Control Protocol)
* UDP (User Datagram Protocol)
* ICMP (Internet Control Message Protocol)

Installation

Install Python and Scapy.

Run this command:

pip install scapy

For Windows, install Npcap:

https://npcap.com/

How to Run

1. Open the project in Visual Studio Code.
2. Open the terminal.
3. Run the following command:

python sniffer.py

4. The program will start capturing network packets.
5. Browse the internet to generate network traffic.
6. Press Ctrl + C to stop capturing.

Run with administrator privileges when required.

Sample Output

Source IP        : 192.168.1.10
Destination IP   : 142.xxx.xxx.xxx
Protocol         : TCP
Source Port      : 52341
Destination Port : 443
Payload          : Packet data

Note: This is an example. Actual output depends on network traffic.

Learning Outcomes

Through this project, I learned:

* Network packet capturing.
* IP address analysis.
* TCP, UDP, and ICMP protocols.
* Network ports.
* Basic network traffic analysis using Python.

Conclusion

This project provided practical experience in Python programming and basic network security concepts.

Ethical Use

This tool should only be used on personal networks or networks where permission has been granted.

Internship: CodeAlpha
Domain: Cyber Security
Task: Basic Network Sniffer
Developer: Faiz Khalid
# xmas-scan-detector  
## Table of content  
* [About the project](#about-the-project)  
* [The Xmas Scan](#the-xmas-scan)  
* [Technologies](#technologies)  
* [Features](#features)  
* [Setup](#setup)  
## About the project  
>Sniff the network to detect XMAS scan .   
## The Xmas scan  
The packets **FIN**, **PSH** and **URG** are relevant for the Xmas because packets without SYN, RST or ACK derivatives in a connection reset __(RST)__ if the port is closed and no response if the port is open. Before the absence of such packets combinations of FIN, PSH and URG are enough to carry out the scan.  
## Technologies  
* **python3**  
* **scapy**  
## Features  
*  ***cli***  

## Setup  
```shell  
#setup shell cmd  
$git clone https://github.com/0script/xmas-scan-detector  
$cd xmas-scan-detector/
$sudo python3 smax-scan-detector.py <IP>
```

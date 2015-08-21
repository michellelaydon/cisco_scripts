# Cisco Scripts

Authored Aug 20, 2015 by Ken Lemoine

### Summary

This repo contains a set of Python, Expect and BASH scripts designed to 'blackhole' an IP address on multiple Cisco routers.  This will effectively send all traffic from this IP to the 'bitbucket'.  The use case for us is to blackhole any IP that is involved in a DDos attack. 

### Requirements

* Access to some Cisco routers, with privelege level high enough to run 'enable' and 'conf t'.
* A file (not included) called 'device-list.txt' with a list of router hostnames or IP's, in the same directory as these scripts.
* Python, Expect and BASH obviously.
* Optionally, but recommeded, is PIP, makes for installing some little requirements much easier, such as -
* Python library 'netaddr'.  Just do a "pip install netaddr"

### Installation Instructions

* Install Git
  * sudo apt-get install git
  * git config --global user.name "yourusername"
  * git config --global user.email "your@emailaddy"

* Checkout this repository
  * git@github.com:KeyInfo/cisco_scripts.git

* Create a device-list.txt file with a list of your routers, one per line.

* Install (optional) Pip. Here's the Ubuntu steps -
  * sudo apt-get update
  * sudo apt-get -y install python-pip
  * pip -v  (verify's successful install)

* Ensure 'netaddr' Python library is installed. Just do a 'pip show netaddr'

### Script Execution

* Run the blackhole.py file
  * python blackhole.py


# cisco_scripts

Authored Aug 20, 2015 by Ken Lemoine

### Summary

This repo contains a set of Python, Expect and BASH scripts designed to 'blackhole' an IP address on multiple Cisco routers.  This will effectively send all traffic from this IP to the 'bitbucket'.  The use case for us is to blackhole any IP that is involved in a DDos attack.  The next step will be to add a set of similiar scripts to remove any blackholed IP's after the attack is over.

### Requirements

You'll need access to some Cisco routers, with privelege level high enough to run 'enable' and 'conf t'.
A file called 'device-list.txt' with a list of routers, either hostnames or IP addresses, in the same directory as these scripts.
Python, Expect and BASH obviously.  See notes below for help installing these.
Optionally, but recommeded, is PIP, makes for installing some little requirements much easier.
Python library 'netaddr'.  Just do a "pip install netaddr"
That's it!

### Installation Instructions

### Script Execution


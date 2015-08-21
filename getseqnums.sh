#!/bin/bash
# Vars passed in are:  device ($1), username ($2), password ($3)
# This script is called by blackholeip.py and gets the last sequence number and writes it to out.txt

./vty_runcmd.exp -h $1 -u $2 -p $3 -e enablepass, method = ssh < commands.txt > outfiles/out.txt


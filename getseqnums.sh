#!/bin/bash

# echo out vars for troubleshooting
#echo 'getseqnums device is ' $1
#echo 'user is ' $2
#echo 'passwd is ' $3

./vty_runcmd.exp -h $1 -u $2 -p $3 -e enablepass, method = ssh < commands.txt > outfiles/out.txt


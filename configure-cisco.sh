#!/bin/bash
device=$1
password=$2
seqnum=$3
ipaddy=$4

 ./configure-cisco.exp $device $password $seqnum $ipaddy;

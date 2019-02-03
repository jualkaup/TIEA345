#!/bin/sh
sudo /etc/init.d/motion stop 
sleep 1 
python ../dev/demo3/t5_cron_picture.py
sudo /etc/init.d/motion start
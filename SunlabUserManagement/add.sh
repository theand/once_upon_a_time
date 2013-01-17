#!/bin/bash

~/ua.py user.dat
cd /var/yp
make
cd ~
mv user.dat user.dat.bak
touch user.dat

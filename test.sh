#!/bin/sh
echo "one" > test.log
echo "two" >> test.log
echo "three" >> test.log

if [ ! -n "$1" ]
then
	tail test.log | ./gntp-tee.py
else
	tail test.log | ./gntp-tee.py -P "$1"
fi
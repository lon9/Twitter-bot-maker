#!/bin/sh

POS=`dirname $0`
find "$POS/lock/*" -mmin +60 | xargs rm -r 

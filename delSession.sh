#!/bin/sh

POS=`dirname $0`
find "$POS/lock" -mtime +3 -exec rm {} \;

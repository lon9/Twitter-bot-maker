#!/bin/sh

POS=`dirname $0`
find "$POS/app/controller/tmp" -mtime +3 -exec rm {} \;

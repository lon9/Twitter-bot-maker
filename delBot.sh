#!/bin/sh

POS=`dirname $0`
find "$POS/app/controllers/tmp" -mtime +3 -exec rm {} \;

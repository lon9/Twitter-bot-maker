#!/bin/sh

POS=`dirname $0`
find "$POS/app/controllers/tmp/*" -mmin +60 | xargs rm -r

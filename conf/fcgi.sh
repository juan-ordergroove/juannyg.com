#!/bin/bash

# Replace these three settings.
PROJDIR="/var/run/juannyg.com"
PIDFILE="$PROJDIR/juanngy.com.pid"
#SOCKET="$PROJDIR/juannyg.com.sock"

cd $PROJDIR
if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi

/opt/pythonenv/juannyg.com-env/bin/python /opt/pythonenv/juannyg.com-env/juannyg.com/manage.py runfcgi pidfile=$PIDFILE method=threaded host=127.0.0.1 port=8080

#!/bin/bash

if [ "$1" == "" ]
    then echo "Usage: $0 + URL"
    exit 0
else
    HOST=`echo $1 | sed 's/http\:\/\///' | sed -r 's/([^/])\/(.*)/\1/'`
    echo "1/5 Cut full URL and leaves one host... Done! HOST = $HOST"
fi
echo "2/5 Check the validity of the host..."
if ping -c1 -W1 -q $HOST &> /dev/null
    then echo -en "\033[32mSuccessful:\033[0m HOST valid!\n"
else 
    echo -en "\033[0;31mError:\033[0m HOST not valid!\n"; exit 0
fi
FILENAME=`echo "$1" | sed -r 's/(.*)\/(.*)/\2/'`
echo "3/5 Get filename... FILENAME = $FILENAME"
PATH=`echo "$1" | sed 's/http\:\/\///' | sed -r "s/$HOST//" | sed "s/$FILENAME//"`
echo "4/5 Check file path... PATH = $PATH"
PORT=80
HEADERS="HTTP/1.1\r\nHost: $HOST\r\nConnection: close\r\nContent-Length: 0\r\n\r\n"
TEMP="/tmp/dlfile"
exec 3<>/dev/tcp/$HOST/$PORT
echo -e "GET $PATH$FILENAME $HEADERS" >&3 
/bin/cat <&3 > $TEMP
/usr/bin/tail $TEMP -n +$((`/bin/sed $TEMP -e '/^\r$/q' | /usr/bin/wc -l`+1)) > $FILENAME
echo "5/5 File $FILENAME downloaded."
/bin/rm $TEMP
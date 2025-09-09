#!/bin/bash

#pointing the scripts
~/linux/script.sh
~/linux/error_count.sh

#capturing output to report file
result=$(./script.sh)
echo "Backed up completed: $result " >> report.txt
result=$(./error_count.sh)
echo "File has: $result  errors" >> report.txt



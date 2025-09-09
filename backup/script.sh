#!/bin/bash
for file in ~/linux/*; do
 echo "found files: $file "
cp  $file ~/linux/backup;
 echo "copying files..."
done

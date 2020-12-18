#!/bin/bash
filearg=""
for arg in $@
do
  filearg="$filearg -F files[]=@$arg "
done
ret=$(curl -sf $filearg $uploadurl)
result=$(echo $ret | egrep -o '$urlfragment/[a-z0-9]{12}(\.[a-z]+)?' | sort | uniq)
for url in $result
do
  echo "https://$url"
done

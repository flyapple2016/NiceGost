#!/bin/bash

sudo apt-get update && sudo apt-get install curl mmdb-bin

map_file="ISO2"

while read -r line; do
    ip=$(echo $line | cut -d ' ' -f 1 | cut -d '/' -f 1)
    result=$(mmdblookup --file GeoLite2-Country.mmdb --ip $ip country iso_code)
    country_code=$(echo $result | awk -F '"' '{print $2}')
    chinese_name=$(grep "^${country_code}-" "$map_file" | cut -d '-' -f 2)
    echo $ip $chinese_name >> "IP4-AS209242-ISO"
done < IP4-AS209242-CIDR

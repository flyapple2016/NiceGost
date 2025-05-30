#!/bin/bash

sudo apt-get update && sudo apt-get install curl mmdb-bin

curl -L -o GeoLite2-Country.mmdb https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-Country.mmdb > /dev/null 2>&1
sleep 3

asns=("13335" "209242")
map_file="ISO2"
rm -f IP4-AS13335-CIDR IP6-AS13335-CIDR IP4-AS209242-CIDR IP6-AS209242-CIDR IP4-AS209242-ISO IP4-AS13335-ISO

for asn in "${asns[@]}"; do
    curl -A 'CompanyName BGP Tool - contact@yourcompany.com' "https://bgp.tools/table.txt" -s | grep "$asn" > "tmp-$asn.txt"

    while IFS= read -r line || [[ -n "$line" ]]; do
        prefix=$(echo "$line" | awk '{print $1}')
        asn=$(echo "$line" | awk '{print $2}')

        if [[ "$prefix" == *":"* ]]; then
            echo "$prefix" >> "IP6-AS$asn-CIDR"
        else
            echo "$prefix" >> "IP4-AS$asn-CIDR"
        fi
    done < "tmp-$asn.txt"

    rm "tmp-$asn.txt"
done

sleep 3

while read -r line; do
    ip=$(echo $line | cut -d ' ' -f 1 | cut -d '/' -f 1)
    result=$(mmdblookup --file GeoLite2-Country.mmdb --ip $ip country iso_code)
    country_code=$(echo $result | awk -F '"' '{print $2}')
    chinese_name=$(grep "^${country_code}-" "$map_file" | cut -d '-' -f 2)
    echo $line $chinese_name >> "IP4-AS209242-ISO"
done < IP4-AS209242-CIDR

while read -r line; do
    ip=$(echo $line | cut -d ' ' -f 1 | cut -d '/' -f 1)
    result=$(mmdblookup --file GeoLite2-Country.mmdb --ip $ip country iso_code)
    country_code=$(echo $result | awk -F '"' '{print $2}')
    chinese_name=$(grep "^${country_code}-" "$map_file" | cut -d '-' -f 2)
    echo $line $chinese_name >> "IP4-AS13335-ISO"
done < IP4-AS13335-CIDR

#!/bin/bash

set -e
sni_host="zimbabwe-prefers-discounted-oldest.trycloudflare.com"
template1="vless://3a9667dc-a684-1c1f-bdf0-c3098e8456ff@{{ip}}:{{port}}?encryption=none&security=xtls&flow=xtls-rprx-vision&sni=$sni_host&type=ws&host=$sni_host&path=/TerrariaSkeletron002?ed=2048#{{comment}}"
template2="vless://3a9667dc-a684-1c1f-bdf0-c3098e8456ff@{{ip}}:{{port}}?encryption=none&security=xtls&flow=xtls-rprx-vision&sni=$sni_host&type=ws&host=$sni_host&path=/TerrariaSkeletron002?ed=2048#BR-{{comment}}"
template3="{\"add\":\"{{ip}}\",\"aid\":\"0\",\"alpn\":\"\",\"host\":\"$sni_host\",\"id\":\"3a9667dc-a684-1c1f-bdf0-c3098e8456ff\",\"net\":\"ws\",\"path\":\"/TerrariaSkeletron003?ed=2048\",\"port\":\"{{port}}\",\"ps\":\"BR-CMCC\",\"scy\":\"auto\",\"sni\":\"\",\"tls\":\"\",\"type\":\"\",\"v\":\"2\"}"

curl_output=$(curl https://sub.cfno1.eu.org/sub | base64 -d | sed '2,3d')
output_file="base64.txt"
header=$(echo "$curl_output" | sed -n '1p')
content=$(echo "$curl_output" | sed '1d')
> "$output_file"
echo "$header" >> "$output_file"
while IFS= read -r text; do
    ip_port=$(echo "$text" | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+')
    ip=$(echo "$ip_port" | cut -d ':' -f 1)
    port=$(echo "$ip_port" | cut -d ':' -f 2)
    comment=$(echo "$text" | cut -d '#' -f 2)
    result=$(echo "$template1" | sed "s/{{ip}}/$ip/g; s/{{port}}/$port/g; s/{{comment}}/$comment/g")
    echo "$result" >> "$output_file"
done <<< "$content"

addresses=$(curl -s https://addressesapi.090227.xyz/cmcc)
ports1=(443 2053 2083 2087 2096 8443)
ports2=(80 8080 8880 2052 2082 2086 2095)

append_to_file() {
    while IFS='#' read -r address comment; do
        ip=$(echo "$address" | cut -d':' -f1)
        port1=${ports1[$RANDOM % ${#ports1[@]}]}
        port2=${ports2[$RANDOM % ${#ports2[@]}]}
        new_template2=$(echo "$template2" | sed "s/{{ip}}/$ip/g; s/{{port}}/$port1/g; s/{{comment}}/$comment/g")
        echo "$new_template2" >> "$output_file"
    done <<< "$addresses"
    while IFS='#' read -r address comment; do
        ip=$(echo "$address" | cut -d':' -f1)
        port2=${ports2[$RANDOM % ${#ports2[@]}]}
        new_template3_json=$(echo "$template3" | sed "s/{{ip}}/$ip/g; s/{{port}}/$port2/g; s/{{comment}}/$comment/g")
        new_template3_base64=$(echo -n "$new_template3_json" | base64)
        echo -n "vmess://$new_template3_base64" | tr -d '\n' >> "$output_file"
        echo >> "$output_file"
    done <<< "$addresses"
}

append_to_file

#!/bin/bash

sni_host="zimbabwe-prefers-discounted-oldest.trycloudflare.com"
template="vless://3a9667dc-a684-1c1f-bdf0-c3098e8456ff@{{ip}}:{{port}}?encryption=none&security=xtls&flow=xtls-rprx-vision&sni=$sni_host&type=ws&host=$sni_host&path=/TerrariaSkeletron002?ed=2048#{{comment}}"
curl_output=$(curl https://sub.cfno1.eu.org/sub | base64 -d | sed '2,3d')
output_file="modified_info.txt"
header=$(echo "$curl_output" | sed -n '1p')
content=$(echo "$curl_output" | sed '1d')
> "$output_file"
echo "$header" >> "$output_file"
while IFS= read -r text; do
    ip_port=$(echo "$text" | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+')
    ip=$(echo "$ip_port" | cut -d ':' -f 1)
    port=$(echo "$ip_port" | cut -d ':' -f 2)
    comment=$(echo "$text" | cut -d '#' -f 2)
    result=$(echo "$template" | sed "s/{{ip}}/$ip/g; s/{{port}}/$port/g; s/{{comment}}/$comment/g")
    echo "$result" >> "$output_file"
done <<< "$content"

addresses=$(curl -s https://addressesapi.090227.xyz/cmcc)
ports=(443 2053 2083 2087 2096 8443)

append_to_file() {
    while IFS='#' read -r address comment; do
        ip=$(echo "$address" | cut -d':' -f1)
        port=${ports[$RANDOM % ${#ports[@]}]}
        sni_host=$(echo "$comment" | cut -d'#' -f1)
        new_template=$(echo "$template" | sed "s/{{ip}}/$ip/g; s/{{port}}/$port/g; s/{{comment}}/$comment/g")
        echo "$new_template" >> "$output_file"
    done <<< "$addresses"
}

append_to_file

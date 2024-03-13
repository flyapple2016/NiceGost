#!/bin/bash

sni_host="zimbabwe-prefers-discounted-oldest.trycloudflare.com"

template="vless://3a9667dc-a684-1c1f-bdf0-c3098e8456ff@{{ip_port}}?encryption=none&security=xtls&flow=xtls-rprx-vision&sni=$sni_host&type=ws&host=$sni_host&path=/TerrariaSkeletron002?ed=2048#{{comment}}"
curl_output=$(curl https://sub.cfno1.eu.org/sub | base64 -d | sed '2,3d')
output_file="modified_info.txt"
> "$output_file"
while IFS= read -r text; do
    ip_port=$(echo "$text" | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+')
    comment=$(echo "$text" | grep -oE '#[^#]+$' | sed 's/#//')
    result=$(echo "$template" | sed "s/{{ip_port}}/$ip_port/g; s/{{comment}}/$comment/g")
    echo "$result" >> "$output_file"
done <<< "$curl_output"
echo "处理完成，结果已写入 $output_file 文件。"

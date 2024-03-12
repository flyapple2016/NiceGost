#!/bin/bash

curl https://sub.cfno1.eu.org/sub | base64 -d > text.txt
sed '2,3d' text.txt > temp.txt
sed 's/de44b044-8f90-4e18-b742-16591667ff96/3a9667dc-a684-1c1f-bdf0-c3098e8456ff/g; s/edgetunnel-free.pages.dev/zimbabwe-prefers-discounted-oldest.trycloudflare.com/g' temp.txt > text.txt
# base64 text.txt > encoded.txt
rm temp.txt

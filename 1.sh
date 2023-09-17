#!/bin/bash

MESSAGE="NiceGost 测速."
URL="https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage"
curl -s -X POST $URL -d chat_id=$TELEGRAM_CHAT_ID -d text="$MESSAGE" > /dev/null

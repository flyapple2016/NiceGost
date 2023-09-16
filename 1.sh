#!/usr/bin/env bash

TELEGRAM_TOKEN=${TELEGRAM_BOT_TOKEN}
TELEGRAM_ID=${TELEGRAM_CHAT_ID}

if [ -z "$TELEGRAM_TOKEN" ] || [ -z "$TELEGRAM_ID" ]; then
  echo "Telegram机器人令牌或聊天ID未设置。请确保设置了这些环境变量。"
fi

MESSAGE="这是一条来自GitHub Actions的测试消息。"
URL="https://api.telegram.org/bot$TELEGRAM_TOKEN/sendMessage"
curl -s -X POST "$URL" -d "chat_id=$TELEGRAM_ID" -d "text=$MESSAGE"

if [ $? -eq 0 ]; then
  echo "消息已成功发送到Telegram！"
else
  echo "发送消息到Telegram失败。"
fi

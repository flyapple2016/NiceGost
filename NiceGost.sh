#!/usr/bin/env bash

GO_VERSION="1.20.8"
TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
TELEGRAM_CHAT_ID=${TELEGRAM_CHAT_ID}

sendMessage() {

if [ -z "$TELEGRAM_BOT_TOKEN" ] || [ -z "$TELEGRAM_CHAT_ID" ]; then
  echo "Telegram机器人令牌或聊天ID未设置。请确保设置了这些环境变量。"
  exit 1
fi

MESSAGE="这是一条来自GitHub Actions的测试消息。"
URL="https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage"
curl -s -X POST "$URL" -d "chat_id=$TELEGRAM_CHAT_ID" -d "text=$MESSAGE"

if [ $? -eq 0 ]; then
  echo "消息已成功发送到Telegram！"
else
  echo "发送消息到Telegram失败。"
fi

  #MESSAGE="NiceGost has been updated to version $latest_version."
  #URL="https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage"
  #curl -s -X POST "$URL" -d "chat_id=$TELEGRAM_CHAT_ID" -d "text=$MESSAGE"
}

updateNiceGost() {
  if [ "$latest_version" != "$current_version" ]; then
    echo "Remote Cloudflared version ($current_version) is different from latest version ($latest_version). Updating..."
    cat <<EOL > README.md
Latest Version: $latest_version
EOL
    wget "https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz"
    sudo rm -rf /usr/local/go
    sudo tar -C /usr/local -xzf "go${GO_VERSION}.linux-amd64.tar.gz"
    export PATH=$PATH:/usr/local/go/bin

    download_url="https://github.com/cloudflare/cloudflared/archive/$latest_version.zip"
    curl -LO "$download_url"
    unzip "$latest_version.zip"
    cd "cloudflared-$latest_version"

    go build -o cloudflared-amd -trimpath -ldflags "-s -w -buildid=" ./cmd/cloudflared
    GOOS=linux GOARCH=arm64 CGO_ENABLED=0 go build -o cloudflared-arm -trimpath -ldflags "-s -w -buildid=" ./cmd/cloudflared

    sudo chmod a+x cloudflared-amd cloudflared-arm
    upx -o nicegost cloudflared-amd
    sudo chmod a+x nicegost

    mv cloudflared-amd cloudflared-arm nicegost ..
    cd ..

    PACKAGE_NAME="NiceGost"
    PACKAGE_VERSION="$latest_version"
    PACKAGE_ARCH="amd64"
    MAINTAINER="NiceGost <NiceGost@email.com>"
    DESCRIPTION="NiceGost 2023"

    PACKAGE_DIR="$PACKAGE_NAME-$PACKAGE_VERSION"
    DEBIAN_DIR="$PACKAGE_DIR/DEBIAN"
    INSTALL_DIR="$PACKAGE_DIR/usr/bin"

    mkdir -p "$DEBIAN_DIR"
    chmod 0755 "$DEBIAN_DIR"

    mkdir -p "$INSTALL_DIR"
    cp nicegost "$INSTALL_DIR"

    cat > "$DEBIAN_DIR/control" <<EOF
Package: $PACKAGE_NAME
Version: $PACKAGE_VERSION
Architecture: $PACKAGE_ARCH
Maintainer: $MAINTAINER
Description: $DESCRIPTION
EOF

    dpkg-deb --build "$PACKAGE_DIR" "$PACKAGE_NAME.deb"
    rm -rf "$PACKAGE_DIR"

    echo "Package $PACKAGE_NAME.deb created successfully."
    sendMessage
  else
    echo "Remote Cloudflared version is up to date. No need to download and compile NiceGost."
  fi
}

latest_release_info=$(curl -s https://api.github.com/repos/cloudflare/cloudflared/releases/latest)
latest_version=$(echo "$latest_release_info" | grep '"tag_name":' | cut -d '"' -f 4)

current_version=$(curl -s "https://raw.githubusercontent.com/flyapple2016/NiceGost/main/README.md" | grep 'Latest Version:' | awk '{print $NF}')

updateNiceGost

#!/bin/bash

GO_VERSION="1.21.6"

update_readme() {
  cat <<EOL > README.md
Latest Version: $latest_version
EOL
}

download_compile_upload() {
  wget https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz
  sudo rm -rf /usr/local/go
  sudo tar -C /usr/local -xzf go${GO_VERSION}.linux-amd64.tar.gz
  export PATH=$PATH:/usr/local/go/bin

  download_url="https://github.com/cloudflare/cloudflared/archive/$latest_version.zip"
  curl -LO "$download_url"
  unzip "$latest_version.zip"
  cd "cloudflared-$latest_version"

  go build -o nicegost -trimpath -ldflags "-s -w -buildid=" ./cmd/cloudflared
  GOOS=linux GOARCH=arm64 CGO_ENABLED=0 go build -o nicegost-arm -trimpath -ldflags "-s -w -buildid=" ./cmd/cloudflared

  sudo chmod a+x nicegost nicegost-arm
  upx nicegost nicegost-arm
  sudo chmod a+x nicegost nicegost-arm

  mv nicegost nicegost-arm ..
  cd ..
}

build_deb_package() {
  PACKAGE_NAME="NiceGost"
  PACKAGE_VERSION="$latest_version"
  MAINTAINER="NiceGost <NiceGost@email.com>"
  DESCRIPTION="NiceGost 2023"

  PACKAGE_ARCH="amd64"
  PACKAGE_DIR="$PACKAGE_NAME-$PACKAGE_VERSION-$PACKAGE_ARCH"
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

  dpkg-deb --build "$PACKAGE_DIR" "$PACKAGE_NAME-$PACKAGE_ARCH.deb"
  rm -rf "$PACKAGE_DIR"
  rm -rf nicegost
  echo "Package $PACKAGE_NAME-$PACKAGE_VERSION-$PACKAGE_ARCH.deb created successfully."

  mv nicegost-arm nicegost

  PACKAGE_ARCH="arm64"
  PACKAGE_DIR="$PACKAGE_NAME-$PACKAGE_VERSION-$PACKAGE_ARCH"
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

  dpkg-deb --build "$PACKAGE_DIR" "$PACKAGE_NAME-$PACKAGE_ARCH.deb"
  rm -rf "$PACKAGE_DIR"
  echo "Package $PACKAGE_NAME-$PACKAGE_VERSION-$PACKAGE_ARCH.deb created successfully."
}

latest_version=$(curl -s https://api.github.com/repos/cloudflare/cloudflared/releases/latest | grep '"tag_name":' | cut -d '"' -f 4)
current_version=$(curl -s "https://raw.githubusercontent.com/flyapple2016/NiceGost/main/README.md" | grep 'Latest Version:' | awk '{print $NF}')

if [ "$latest_version" != "$current_version" ]; then
  sudo apt-get update
  sudo apt-get install -y upx-ucl curl unzip gcc-aarch64-linux-gnu devscripts build-essential debhelper
  update_readme
  download_compile_upload
  build_deb_package
  MESSAGE="NiceGost has been updated to version $latest_version."
else
  MESSAGE="NiceGost doesn't need an update."
fi

URL="https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage"
curl -s -X POST $URL -d chat_id=$TELEGRAM_CHAT_ID -d text="$MESSAGE" > /dev/null

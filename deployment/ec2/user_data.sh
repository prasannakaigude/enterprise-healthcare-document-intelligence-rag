#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="/opt/rag-healthcare"

sudo apt-get update -y
sudo apt-get install -y ca-certificates curl git

sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update -y
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl enable docker
sudo systemctl start docker

sudo mkdir -p "${PROJECT_DIR}"
sudo chown ubuntu:ubuntu "${PROJECT_DIR}"

cat <<'MESSAGE'
EC2 bootstrap finished.

Next manual steps:
1. Copy or clone the project into /opt/rag-healthcare.
2. Create /opt/rag-healthcare/.env with real runtime values.
3. Run:
   docker compose -f docker-compose.yml -f docker-compose.ec2.yml up -d --build

Do not place real API keys in this user_data.sh file.
MESSAGE

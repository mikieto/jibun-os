# .devcontainer/Dockerfile
FROM python:3.11-slim-bullseye

# git と yamllint を追加
RUN apt-get update \
  && apt-get install -y --no-install-recommends git \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
  && rm /tmp/requirements.txt

 RUN groupadd -g 1000 vscode \
  && useradd -m -u 1000 -g vscode vscode

WORKDIR /workspaces/jibun-os

USER vscode



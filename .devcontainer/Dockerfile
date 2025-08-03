# .devcontainer/Dockerfile
FROM python:3.11-slim-bullseye

RUN apt-get update -y \
  && apt-get install -y --no-install-recommends git curl jq ca-certificates \
  && curl -L "https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64" -o /usr/local/bin/yq \
  && chmod +x /usr/local/bin/yq \
  && curl -L -o /usr/local/bin/opa https://openpolicyagent.org/downloads/latest/opa_linux_amd64 \
  && chmod +x /usr/local/bin/opa \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt

COPY requirements-dev.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements-dev.txt && rm /tmp/requirements-dev.txt

RUN groupadd -g 1000 vscode \
  && useradd -m -u 1000 -g vscode vscode

RUN git config --system pull.rebase true \
 && git config --system rerere.enabled true \
 && git config --system merge.conflictStyle diff3

USER vscode
WORKDIR /workspaces/jibun-os

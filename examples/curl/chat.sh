#!/usr/bin/env bash
set -euo pipefail

: "${GENVIS_API_KEY:?Set GENVIS_API_KEY}"
BASE_URL="${GENVIS_BASE_URL:-https://genvis.xyz/v1}"
MODEL="${GENVIS_TEXT_MODEL:-YOUR_TEXT_MODEL}"

curl "$BASE_URL/chat/completions" \
  -H "Authorization: Bearer $GENVIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"$MODEL\",
    \"messages\": [
      { \"role\": \"user\", \"content\": \"用一句话介绍 Genvis AI 的 API 能力。\" }
    ]
  }"

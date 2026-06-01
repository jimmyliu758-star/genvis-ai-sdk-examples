#!/usr/bin/env bash
set -euo pipefail

: "${GENVIS_API_KEY:?Set GENVIS_API_KEY}"
BASE_URL="${GENVIS_BASE_URL:-https://genvis.xyz/v1}"
MODEL="${GENVIS_IMAGE_MODEL:-gpt-image-2-vip}"

curl "$BASE_URL/images/generations" \
  -H "Authorization: Bearer $GENVIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"$MODEL\",
    \"prompt\": \"Premium product photography for a scented candle gift box, warm cozy lighting, clean commercial background, 4:5\",
    \"n\": 1,
    \"size\": \"1024x1280\",
    \"quality\": \"high\"
  }"

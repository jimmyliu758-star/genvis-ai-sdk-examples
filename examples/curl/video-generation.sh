#!/usr/bin/env bash
set -euo pipefail

: "${GENVIS_API_KEY:?Set GENVIS_API_KEY}"
BASE_URL="${GENVIS_BASE_URL:-https://genvis.xyz/v1}"
MODEL="${GENVIS_VIDEO_MODEL:-video_vidu}"
IMAGE="${GENVIS_REFERENCE_IMAGE:-https://example.com/product.png}"

curl "$BASE_URL/video/generations" \
  -H "Authorization: Bearer $GENVIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"$MODEL\",
    \"prompt\": \"让画面中的产品缓慢旋转，背景有柔和光影，商业广告质感\",
    \"image\": \"$IMAGE\",
    \"duration\": 5,
    \"size\": \"1080p\",
    \"metadata\": {
      \"aspectRatio\": \"16:9\",
      \"resolution\": \"1080p\",
      \"movement_amplitude\": \"auto\",
      \"bgm\": false
    }
  }"

# Genvis AI SDK Examples

Genvis AI provides an OpenAI-compatible API for text, multimodal chat, image generation, image editing, and async video generation.

Default API base URL:

```text
https://genvis.xyz/v1
```

Fallback API base URL:

```text
https://apitoken.fun/v1
```

## Quick Start

```bash
cp .env.example .env
```

Edit `.env` and set your API key:

```bash
GENVIS_API_KEY=sk-your-api-key
GENVIS_BASE_URL=https://genvis.xyz/v1
```

## Node.js Examples

Install dependencies:

```bash
npm install
```

Run examples:

```bash
npm run chat
npm run image
npm run video
```

## Python Examples

Create an environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run examples:

```bash
python examples/python/chat.py
python examples/python/image_generation.py
python examples/python/video_generation.py
```

## API Endpoints

| Capability | Method | Endpoint |
| --- | --- | --- |
| Models | GET | `/v1/models` |
| Chat completions | POST | `/v1/chat/completions` |
| Responses | POST | `/v1/responses` |
| Image generation | POST | `/v1/images/generations` |
| Image editing | POST | `/v1/images/edits` |
| Video generation | POST | `/v1/videos` |
| Video task detail | GET | `/v1/videos/{task_id}` |
| Video content | GET | `/v1/videos/{task_id}/content` |
| JSON video generation | POST | `/v1/video/generations` |
| JSON video task detail | GET | `/v1/video/generations/{task_id}` |
| Embeddings | POST | `/v1/embeddings` |
| Rerank | POST | `/v1/rerank` |
| Audio speech | POST | `/v1/audio/speech` |
| Audio transcription | POST | `/v1/audio/transcriptions` |

## cURL

### Chat

```bash
curl "$GENVIS_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $GENVIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "YOUR_TEXT_MODEL",
    "messages": [
      { "role": "user", "content": "用一句话介绍 Genvis AI 的 API 能力" }
    ]
  }'
```

### Image Generation

```bash
curl "$GENVIS_BASE_URL/images/generations" \
  -H "Authorization: Bearer $GENVIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2-vip",
    "prompt": "Premium product photography for a scented candle gift box, warm cozy lighting, clean commercial background, 4:5",
    "n": 1,
    "size": "1024x1280",
    "quality": "high"
  }'
```

### Video Generation

```bash
curl "$GENVIS_BASE_URL/video/generations" \
  -H "Authorization: Bearer $GENVIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "video_vidu",
    "prompt": "让画面中的产品缓慢旋转，背景有柔和光影",
    "image": "https://example.com/product.png",
    "duration": 5,
    "size": "1080p",
    "metadata": {
      "aspectRatio": "16:9",
      "resolution": "1080p",
      "movement_amplitude": "auto",
      "bgm": false
    }
  }'
```

## Model Names

Use `GET /v1/models` to list models available to your API key:

```bash
curl "$GENVIS_BASE_URL/models" \
  -H "Authorization: Bearer $GENVIS_API_KEY"
```

Then set:

```bash
GENVIS_TEXT_MODEL=your-text-model
GENVIS_IMAGE_MODEL=your-image-model
GENVIS_VIDEO_MODEL=your-video-model
```

## Security

Never expose `GENVIS_API_KEY` in frontend code, mobile apps, screenshots, or public repositories. Call Genvis AI from your backend or a trusted server-side environment.

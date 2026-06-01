# Genvis AI API 示例项目 / SDK Examples

面向中文开发者的 Genvis AI API 接入示例，支持 OpenAI 兼容调用，可用于文本对话、多模态、AI 图片生成、AI 图片编辑和 AI 视频异步生成。

Genvis AI 支持微信、支付宝充值，适合国内开发者、AI 工具站、自媒体工具、电商素材系统和自动化工作流接入。

> English: OpenAI-compatible SDK examples for Genvis AI text, image, and video APIs. Chinese documentation is the primary version because most users pay with WeChat Pay or Alipay.

## 官网与控制台

- 官网 / 控制台：[https://genvis.xyz](https://genvis.xyz)
- 备用域名：[https://apitoken.fun](https://apitoken.fun)
- API Base URL：`https://genvis.xyz/v1`
- 备用 API Base URL：`https://apitoken.fun/v1`

## 你可以用它做什么

- 用一个 API Key 调用文本、图片、视频模型
- 用 OpenAI SDK 快速接入现有项目
- 给 AI 工具站、Dify、Coze、n8n、FastGPT 等工作流提供统一模型接口
- 批量生成商品图、广告图、小红书封面、短视频素材
- 查询视频生成任务状态，并获取最终视频结果

## API 地址

默认地址：

```text
https://genvis.xyz/v1
```

备用地址：

```text
https://apitoken.fun/v1
```

## 接入前准备

1. 注册并登录 Genvis AI。
2. 使用微信或支付宝完成充值。
3. 在控制台创建 API Key。
4. 在模型列表或 API 文档中确认你的账号可用模型。
5. 复制本项目 `.env.example` 为 `.env`，填入 API Key 和模型名称。

```bash
cp .env.example .env
```

编辑 `.env`：

```bash
GENVIS_API_KEY=sk-your-api-key
GENVIS_BASE_URL=https://genvis.xyz/v1

GENVIS_TEXT_MODEL=你的文本模型
GENVIS_IMAGE_MODEL=gpt-image-2-vip
GENVIS_VIDEO_MODEL=video_vidu
```

## Node.js 快速开始

安装依赖：

```bash
npm install
```

运行示例：

```bash
npm run chat
npm run image
npm run video
```

对应文件：

- `examples/node/chat.mjs`：文本对话
- `examples/node/image-generation.mjs`：AI 图片生成
- `examples/node/video-generation.mjs`：AI 视频任务提交和轮询
- `sdk/node/genvis-client.mjs`：简单封装的视频任务 SDK

## Python 快速开始

创建环境并安装依赖：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

运行示例：

```bash
python examples/python/chat.py
python examples/python/image_generation.py
python examples/python/video_generation.py
```

对应文件：

- `examples/python/chat.py`：文本对话
- `examples/python/image_generation.py`：AI 图片生成
- `examples/python/video_generation.py`：AI 视频任务提交和轮询
- `sdk/python/genvis_client.py`：简单封装的视频任务 SDK

## cURL 示例

### 文本对话

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

### AI 图片生成

```bash
curl "$GENVIS_BASE_URL/images/generations" \
  -H "Authorization: Bearer $GENVIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2-vip",
    "prompt": "高级香薰蜡烛礼盒商品摄影，温暖室内光，干净商业背景，小红书封面风格，4:5",
    "n": 1,
    "size": "1024x1280",
    "quality": "high"
  }'
```

### AI 视频生成

```bash
curl "$GENVIS_BASE_URL/video/generations" \
  -H "Authorization: Bearer $GENVIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "video_vidu",
    "prompt": "让画面中的产品缓慢旋转，背景有柔和光影，商业广告质感",
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

## 常用接口

| 能力 | Method | Endpoint | 说明 |
| --- | --- | --- | --- |
| 模型列表 | GET | `/v1/models` | 查询当前 API Key 可用模型 |
| 文本对话 | POST | `/v1/chat/completions` | OpenAI 兼容 Chat Completions |
| Responses | POST | `/v1/responses` | OpenAI 兼容 Responses |
| 图片生成 | POST | `/v1/images/generations` | 文生图 |
| 图片编辑 | POST | `/v1/images/edits` | 图生图、参考图生成 |
| 视频生成 | POST | `/v1/videos` | OpenAI 兼容视频任务 |
| 视频任务详情 | GET | `/v1/videos/{task_id}` | 查询视频任务状态 |
| 视频内容 | GET | `/v1/videos/{task_id}/content` | 获取已完成视频 |
| JSON 视频生成 | POST | `/v1/video/generations` | JSON 格式提交视频任务 |
| JSON 视频任务详情 | GET | `/v1/video/generations/{task_id}` | 查询 JSON 视频任务 |
| 向量 | POST | `/v1/embeddings` | 文本向量化 |
| 重排序 | POST | `/v1/rerank` | 文档重排序 |
| 文本转语音 | POST | `/v1/audio/speech` | 生成音频 |
| 音频转文字 | POST | `/v1/audio/transcriptions` | 语音转文字 |

## 如何查看可用模型

不同账号、用户组、余额和模型权限可能不同。接入前建议先查模型列表：

```bash
curl "$GENVIS_BASE_URL/models" \
  -H "Authorization: Bearer $GENVIS_API_KEY"
```

然后把可用模型填入 `.env`：

```bash
GENVIS_TEXT_MODEL=your-text-model
GENVIS_IMAGE_MODEL=your-image-model
GENVIS_VIDEO_MODEL=your-video-model
```

## 适合的用户

- AI 工具站开发者
- 需要低成本调用图片、视频模型的创业团队
- 自媒体和短视频工具开发者
- 跨境电商素材系统
- Dify、Coze、n8n、FastGPT 工作流用户
- 需要微信、支付宝充值的国内团队

## 安全提醒

不要把 `GENVIS_API_KEY` 写进前端页面、移动端 App、公开 GitHub 仓库、浏览器脚本或截图里。建议只在后端服务、云函数、服务器环境变量中使用。

## English Summary

This repository provides OpenAI-compatible Genvis AI examples for Node.js, Python, and cURL. It covers chat completions, image generation, and async video generation with polling. The primary documentation is written in Chinese for domestic users who prefer WeChat Pay and Alipay.

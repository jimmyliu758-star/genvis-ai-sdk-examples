# Genvis AI Frontend Showcase / API Examples

面向开发者、AI 工具站和 AIGC 团队的 Genvis AI 对外展示与轻量接入示例仓库。这里仅展示部分前端使用场景、公开 API 调用样例和官网试用入口，帮助访客快速了解 Genvis AI 的图文视频能力。

本仓库不是完整产品开源仓库，不包含平台后端、模型路由、计费系统、用户系统、管理后台、生产配置、商业策略或任何密钥信息。

新用户注册 Genvis AI 即享 **2 美元免费试用额度**，可以零成本体验大模型文本、图片、视频能力。价格非常低，例如 **gpt-image 2 低至 ¥0.2**，适合先验证效果，再按需放量。

> English: Frontend showcase and OpenAI-compatible public API examples for Genvis AI text reasoning, image generation, and video generation. Chinese documentation is the primary version because most users pay with WeChat Pay or Alipay.

## 官网入口

- 官网 / 控制台：[https://genvis.xyz](https://genvis.xyz)
- 备用域名：[https://apitoken.fun](https://apitoken.fun)
- API Base URL：`https://genvis.xyz/v1`
- 备用 API Base URL：`https://apitoken.fun/v1`
- 公开 API 文档：[docs/api/README.md](./docs/api/README.md)
- 中文快速接入：[docs/quickstart-zh.md](./docs/quickstart-zh.md)
- 产品能力全景：[docs/product-capabilities-zh.md](./docs/product-capabilities-zh.md)
- 前端界面展示建议：[docs/frontend-showcase-zh.md](./docs/frontend-showcase-zh.md)

## 公开展示边界

这个仓库的目标是让浏览 GitHub 的开发者和 AIGC 从业者理解官网能做什么，并引导他们去官网试用，而不是开放完整平台实现。

可以公开展示：

- 官网首页、模型能力页、可视化生图页、可视化生视频页等部分前端界面
- 公开 API 的最小调用示例和参数说明
- Node.js、Python、cURL 的轻量接入样例
- 新用户福利、价格示例、官网入口和控制台入口

不公开展示：

- 后端服务源码、模型调度策略、供应商路由逻辑
- 用户、订单、计费、风控、权限、管理后台等核心业务实现
- 生产环境配置、接口密钥、内部账号、真实用户数据
- 完整商业运营方案、成本模型和供应商账号信息

## 全量支持旗舰 AI 模型

Genvis AI 聚合主流大模型能力，开发者可以用一个 API Key 调用图文视频多模态能力。模型权限、价格和可用状态以控制台模型列表为准。

| 能力方向 | 支持模型示例 | 典型用途 |
| --- | --- | --- |
| 文本推理 | Claude4.8、GPT5.5、Gemini3.5 等 | 智能问答、内容生成、Agent、知识库、工作流编排 |
| 图像生成 | gpt-Image2、Nano Banao 2 等 | 商品图、海报、封面、广告素材、角色图、风格化创作 |
| 视频生成 | Veo、sora2、GrokVideo 等 | 文生视频、图生视频、短视频素材、广告片段、影视级动态画面 |

## 三大核心使用模式

### 1. 标准化 API 调用

本仓库只展示公开 API 的轻量接入路径：使用 OpenAI 兼容 SDK 或 HTTP 请求调用 Genvis AI。示例用于帮助开发者理解调用方式，不代表完整平台实现。

- 全模型统一 API 入口，减少多供应商适配成本
- 支持文本、图像、视频等多模态任务
- 支持批量任务、异步生成、任务轮询和结构化素材返回
- 适合 AI 工具站、SaaS 后台、自动化脚本、Dify、Coze、n8n、FastGPT 等工作流

### 2. 前端可视化界面生图

不写代码也可以直接在 Genvis AI 官网使用可视化生图能力。适合设计师、运营、自媒体和电商团队快速试稿、比稿、批量产出素材。

- 可视化参数调节，无需代码
- 支持高清图像生成、风格自定义和批量出图
- 适合小红书封面、商品主图、广告图、品牌视觉、社媒配图
- 可先用 2 美元免费额度体验，再把稳定工作流接入 API

### 3. 前端可视化界面生视频

Genvis AI 官网也提供可视化视频生成入口，覆盖文生视频、图生视频和长短视频渲染。适合内容团队先验证创意，再沉淀为 API 自动化生产流程。

- 支持文生视频、图生视频、长短视频渲染
- 输出影视级画面效果和流畅动态画面
- 适合广告分镜、产品动态展示、短视频素材、AIGC 影视预览
- 可通过 API 查询异步视频任务状态并获取最终视频文件

## 你可以用它做什么

- 用一个 API Key 调用文本、图片、视频模型
- 用 OpenAI SDK 快速接入现有项目，只需替换 `baseURL` 和 API Key
- 给 AI 工具站、Dify、Coze、n8n、FastGPT 等工作流提供统一模型接口
- 批量生成商品图、广告图、小红书封面、短视频素材
- 提交异步视频生成任务，轮询任务状态并获取最终视频结果
- 先在官网可视化界面验证效果，再把稳定参数迁移到自己的业务系统中

## 接入前准备

1. 注册并登录 [Genvis AI](https://genvis.xyz)，新用户可领取 2 美元免费试用额度。
2. 在控制台创建 API Key。
3. 在模型列表或 API 文档中确认你的账号可用模型。
4. 复制本项目 `.env.example` 为 `.env`，填入 API Key 和模型名称。
5. 如需放量使用，可通过微信或支付宝充值。

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
- 希望先用可视化界面试效果，再用 API 批量生产的 AIGC 团队

## 安全提醒

不要把 `GENVIS_API_KEY` 写进前端页面、移动端 App、公开 GitHub 仓库、浏览器脚本或截图里。建议只在后端服务、云函数、服务器环境变量中使用。

## English Summary

This repository provides OpenAI-compatible Genvis AI examples for Node.js, Python, and cURL. It covers chat completions, image generation, and async video generation with polling. New users can start with a 2 USD free trial credit, try web-based visual image or video generation, and then integrate the same model capabilities through standardized APIs.

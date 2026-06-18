# Genvis AI API 中文快速接入

这篇文档给中文开发者一个最短路径：注册领取免费额度、创建 API Key、查询可用模型，然后用 Node.js、Python 或 cURL 调用文本、图片和视频模型。

如果你还不确定提示词、风格或视频参数，可以先在 Genvis AI 官网用可视化界面生成图片或视频，确认效果后再把稳定参数迁移到 API。

本仓库只提供公开 API 的轻量接入示例和部分前端体验说明，不开放完整平台源码、后端实现、计费系统或模型路由逻辑。

## 1. 注册并领取免费额度

- 官网 / 控制台：[https://genvis.xyz](https://genvis.xyz)
- 备用域名：[https://apitoken.fun](https://apitoken.fun)

新用户注册即享 **2 美元免费试用额度**，可以零成本体验文本推理、图像生成、视频生成等能力。价格非常低，例如 **gpt-image 2 低至 ¥0.2**。如需继续放量使用，可在控制台通过微信或支付宝充值。

## 2. 选择你的使用方式

| 使用方式 | 适合人群 | 说明 |
| --- | --- | --- |
| 标准化 API 调用 | 开发者、AI 工具站、自动化工作流 | 使用本仓库 Node.js、Python、cURL 示例，全模型统一接口，支持批量任务、异步生成、结构化素材返回 |
| 前端可视化界面生图 | 设计师、运营、电商、自媒体 | 无需代码，可视化参数调节，支持高清图像生成、风格自定义、批量出图 |
| 前端可视化界面生视频 | 内容团队、短视频团队、AIGC 影视创作者 | 支持文生视频、图生视频、长短视频渲染，输出影视级画面效果和流畅动态 |

## 3. 创建 API Key

进入控制台的令牌管理，创建一个新的 API Key。建议按项目或环境分别创建，例如：

- `prod-api`
- `dev-test`
- `dify-workflow`
- `image-video-batch`

不要把 API Key 放到前端代码、公开 GitHub 仓库、截图或浏览器脚本里。

## 4. 设置环境变量

复制示例配置：

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

如果主域名访问不稳定，可以切换备用 API 地址：

```bash
GENVIS_BASE_URL=https://apitoken.fun/v1
```

## 5. 查询可用模型

Genvis AI 支持 Claude4.8、GPT5.5、Gemini3.5、gpt-Image2、Nano Banao 2、Veo、sora2、GrokVideo 等旗舰模型。不同账号、余额、用户组和模型权限可能不同，接入前先查模型列表：

```bash
curl "$GENVIS_BASE_URL/models" \
  -H "Authorization: Bearer $GENVIS_API_KEY"
```

把返回的模型 ID 填到 `.env`。模型权限、价格和可用状态以控制台模型列表为准。

## 6. Node.js 调用

安装依赖：

```bash
npm install
```

运行文本对话：

```bash
npm run chat
```

运行图片生成：

```bash
npm run image
```

运行视频生成：

```bash
npm run video
```

## 7. Python 调用

安装依赖：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

运行文本对话：

```bash
python examples/python/chat.py
```

运行图片生成：

```bash
python examples/python/image_generation.py
```

运行视频生成：

```bash
python examples/python/video_generation.py
```

## 8. cURL 最小示例

文本对话：

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

图片生成：

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

视频生成：

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

## 9. 常见问题

### 401 鉴权失败

检查 API Key 是否正确，Header 是否是：

```text
Authorization: Bearer YOUR_API_KEY
```

### 403 无权限

检查余额、模型权限、令牌分组和用户组。

### 模型不存在

先请求 `/v1/models`，不要直接使用旧文档里的模型名。

### 视频没有立即返回结果

视频是异步任务。提交后保存任务 ID，轮询任务详情直到状态变成完成或失败。

## 10. 下一步

- 想了解完整产品能力：阅读 [产品能力全景](./product-capabilities-zh.md)
- 想规范对外截图范围：阅读 [前端界面展示建议](./frontend-showcase-zh.md)
- 想直接试用可视化生图/生视频：打开 [Genvis AI 官网](https://genvis.xyz)
- 想把示例放进自己的项目：从 `sdk/node/genvis-client.mjs` 或 `sdk/python/genvis_client.py` 开始改造

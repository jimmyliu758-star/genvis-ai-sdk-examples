# Genvis AI API 中文快速接入

这篇文档给中文开发者一个最短路径：注册、充值、创建 API Key，然后用 Node.js、Python 或 curl 调用文本、图片和视频模型。

## 1. 注册和充值

- 官网 / 控制台：[https://genvis.xyz](https://genvis.xyz)
- 备用域名：[https://apitoken.fun](https://apitoken.fun)

注册后进入控制台，使用微信或支付宝充值。充值完成后再创建 API Key。

## 2. 创建 API Key

进入控制台的令牌管理，创建一个新的 API Key。建议按项目或环境分别创建，例如：

- `prod-api`
- `dev-test`
- `dify-workflow`
- `image-video-batch`

不要把 API Key 放到前端代码、公开 GitHub 仓库、截图或浏览器脚本里。

## 3. 设置环境变量

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

## 4. 先查询可用模型

不同账号、余额、用户组和模型权限可能不同，接入前先查模型列表：

```bash
curl "$GENVIS_BASE_URL/models" \
  -H "Authorization: Bearer $GENVIS_API_KEY"
```

把返回的模型 ID 填到 `.env`。

## 5. Node.js 调用

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

## 6. Python 调用

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

## 7. cURL 最小示例

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

## 8. 常见问题

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

# API 快速开始

本页用于完成第一次 Genvis AI API 调用。推荐先用新用户 2 美元免费试用额度在官网验证效果，再使用 API Key 接入自己的业务系统。

## 1. 注册并创建 API Key

1. 打开 [https://genvis.xyz](https://genvis.xyz) 注册或登录。
2. 进入控制台的令牌管理。
3. 创建一个新的 API Key。
4. 复制 Key，并保存到本地 `.env` 或服务器环境变量。

示例 `.env`：

```bash
GENVIS_API_KEY=sk-your-api-key
GENVIS_BASE_URL=https://genvis.xyz/v1
```

## 2. 查询可用模型

第一次调用前，先确认当前 Key 可以使用哪些模型：

```bash
curl "$GENVIS_BASE_URL/models" \
  -H "Authorization: Bearer $GENVIS_API_KEY"
```

返回里的 `id` 就是后续请求使用的模型 ID。

## 3. 发送文本请求

```bash
curl "$GENVIS_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $GENVIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "YOUR_TEXT_MODEL",
    "messages": [
      { "role": "user", "content": "用一句话介绍 Genvis AI" }
    ]
  }'
```

## 4. 生成图片

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

## 5. 提交视频任务

```bash
curl "$GENVIS_BASE_URL/video/generations" \
  -H "Authorization: Bearer $GENVIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "YOUR_VIDEO_MODEL",
    "prompt": "让画面中的产品缓慢旋转，背景有柔和光影，商业广告质感",
    "image": "https://example.com/product.png",
    "duration": 5,
    "size": "1080p"
  }'
```

视频通常是异步任务。提交后保存返回的 `task_id` 或 `id`，再查询任务状态。

## 下一步

- [查询模型列表](./models.md)
- [文本与 Responses](./text.md)
- [图像生成与编辑](./images.md)
- [视频任务](./videos.md)
- [错误码与排查](./errors.md)

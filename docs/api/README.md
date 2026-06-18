# Genvis AI 公开 API 文档

本目录用于同步官网 `/docs/api` 的公开调用说明，方便 GitHub 访客在不进入完整产品后台的情况下理解 Genvis AI 的 API 接入方式。

这里仅包含对外可公开的接口入口、请求示例和排查建议，不包含后端源码、模型路由、计费实现、供应商配置、生产环境变量或内部管理系统。

## API Base URL

默认地址：

```text
https://genvis.xyz/v1
```

备用地址：

```text
https://apitoken.fun/v1
```

请求头：

```http
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

## 推荐阅读顺序

1. [快速开始](./quickstart.md)
2. [查询模型列表](./models.md)
3. [文本与 Responses](./text.md)
4. [图像生成与编辑](./images.md)
5. [视频任务](./videos.md)
6. [错误码与排查](./errors.md)

## 常用公开接口

| 能力 | Method | Endpoint | 说明 |
| --- | --- | --- | --- |
| 模型列表 | GET | `/v1/models` | 查询当前 API Key 可用模型 |
| 模型详情 | GET | `/v1/models/{model}` | 查询单个模型信息 |
| 文本对话 | POST | `/v1/chat/completions` | OpenAI 兼容 Chat Completions |
| Responses | POST | `/v1/responses` | OpenAI 兼容 Responses |
| Responses 压缩 | POST | `/v1/responses/compact` | 上下文压缩类请求 |
| 图像生成 | POST | `/v1/images/generations` | 文生图 |
| 图像编辑 | POST | `/v1/images/edits` | 图生图、参考图生成 |
| 视频生成 | POST | `/v1/videos` | OpenAI 兼容视频任务 |
| 视频任务详情 | GET | `/v1/videos/{task_id}` | 查询视频任务状态 |
| 视频内容 | GET | `/v1/videos/{task_id}/content` | 获取完成后的视频内容 |
| JSON 视频生成 | POST | `/v1/video/generations` | JSON 格式提交视频任务 |
| JSON 视频详情 | GET | `/v1/video/generations/{task_id}` | 查询 JSON 视频任务 |
| Embeddings | POST | `/v1/embeddings` | 文本向量化 |
| Rerank | POST | `/v1/rerank` | 文档重排序 |
| 语音转文字 | POST | `/v1/audio/transcriptions` | 音频转写 |
| 文本转语音 | POST | `/v1/audio/speech` | 语音合成 |

## 模型能力示例

实际可用模型以控制台和 `/v1/models` 返回为准。对外文档可展示以下能力方向：

- 文本推理：Claude4.8、GPT5.5、Gemini3.5 等
- 图像生成：gpt-Image2、Nano Banao 2 等
- 视频生成：Veo、sora2、GrokVideo 等

## 接入提醒

- `baseURL` 填到 `/v1` 为止，不要把 `/chat/completions` 也写进 SDK 的 `baseURL`
- API Key 只放在后端、云函数或服务器环境变量中
- 不要在公开仓库、前端页面、浏览器脚本、截图中暴露完整 Key
- 图片和视频任务建议在业务系统中做队列、轮询和失败重试
- 价格、模型权限和可用状态以控制台展示为准

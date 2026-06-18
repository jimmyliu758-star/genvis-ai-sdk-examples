# 文本与 Responses 接口

Genvis AI 支持 OpenAI 兼容的文本对话接口，也支持 Responses 格式。适合聊天助手、内容生成、代码辅助、知识库问答、Agent 推理和工作流编排。

## Chat Completions

请求地址：

```text
POST https://genvis.xyz/v1/chat/completions
```

请求头：

```http
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

常用参数：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `model` | string | 是 | 模型 ID，建议来自 `/v1/models` |
| `messages` | array | 是 | 对话消息 |
| `stream` | boolean | 否 | 是否流式输出 |
| `temperature` | number | 否 | 采样温度 |

请求示例：

```bash
curl "$GENVIS_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $GENVIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "YOUR_TEXT_MODEL",
    "messages": [
      { "role": "user", "content": "写一句适合 AI API 平台首页的标语" }
    ]
  }'
```

流式请求：

```bash
curl "$GENVIS_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $GENVIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "YOUR_TEXT_MODEL",
    "stream": true,
    "messages": [
      { "role": "user", "content": "用三句话介绍 Genvis AI" }
    ]
  }'
```

## Responses

请求地址：

```text
POST https://genvis.xyz/v1/responses
```

压缩接口：

```text
POST https://genvis.xyz/v1/responses/compact
```

请求示例：

```bash
curl "$GENVIS_BASE_URL/responses" \
  -H "Authorization: Bearer $GENVIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "YOUR_TEXT_MODEL",
    "input": "列出 Genvis AI 的三个特点"
  }'
```

## 模型示例

文本推理能力可覆盖 Claude4.8、GPT5.5、Gemini3.5 等模型。实际模型 ID、权限和价格以控制台及 `/v1/models` 返回为准。

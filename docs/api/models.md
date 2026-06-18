# 查询模型列表

第一次调用前，建议先查询模型列表，确认当前 API Key 可以使用哪些模型。

## 请求地址

```text
GET https://genvis.xyz/v1/models
```

备用地址：

```text
GET https://apitoken.fun/v1/models
```

## 请求头

```http
Authorization: Bearer YOUR_API_KEY
```

## 请求示例

```bash
curl "$GENVIS_BASE_URL/models" \
  -H "Authorization: Bearer $GENVIS_API_KEY"
```

## 返回示例

```json
{
  "object": "list",
  "data": [
    {
      "id": "gpt-image-2-vip",
      "object": "model"
    }
  ]
}
```

## 说明

返回结果可能受以下因素影响：

- 当前用户组和账号权限
- 令牌模型限制
- 余额或试用额度
- 模型当前可用状态
- 平台模型配置和维护状态

## 常见问题

### 返回空列表

可能是账号没有可用模型，或令牌限制了模型。请检查余额、用户组、令牌配置和控制台模型权限。

### 文档里的模型调用不了

文档里的模型只作为能力示例。实际调用时，请优先使用 `/v1/models` 返回的模型 ID。

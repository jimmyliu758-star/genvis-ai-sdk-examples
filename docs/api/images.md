# 图像生成与编辑接口

图像接口适用于海报、封面、产品图、广告图、插画、角色图和素材图生成。也可以先在官网可视化生图界面调参，确认效果后再迁移到 API。

## 图像生成

请求地址：

```text
POST https://genvis.xyz/v1/images/generations
```

请求头：

```http
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

请求示例：

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

## 图像编辑

请求地址：

```text
POST https://genvis.xyz/v1/images/edits
```

图像编辑通常用于图生图、参考图生成和局部改图。具体上传方式、文件大小限制和参数支持以控制台文档为准。

## 模型与价格

图像生成能力可覆盖 gpt-Image2、Nano Banao 2 等模型。新用户注册可用 2 美元免费试用额度体验，价格非常低，例如 gpt-image 2 低至 ¥0.2。实际模型 ID、规格、价格和权限以控制台展示为准。

## 常见问题

### 模型不可用

请先请求 `/v1/models`，确认当前用户组、令牌和余额是否可调用该图像模型。

### 请求体过大

如果是图像编辑或参考图生成，请检查图片尺寸、文件大小和站点上传限制。

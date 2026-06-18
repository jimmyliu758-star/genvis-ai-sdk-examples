# 视频任务接口

视频接口用于提交视频生成任务、查询任务状态和获取生成结果。视频通常是异步任务，不一定立即返回最终视频文件。

也可以先在官网可视化视频界面体验文生视频、图生视频和长短视频渲染，确认提示词、图片素材、时长和比例后再接入 API。

## OpenAI 兼容视频接口

提交任务：

```text
POST https://genvis.xyz/v1/videos
```

查询任务：

```text
GET https://genvis.xyz/v1/videos/{task_id}
```

获取内容：

```text
GET https://genvis.xyz/v1/videos/{task_id}/content
```

请求示例：

```bash
curl "$GENVIS_BASE_URL/videos" \
  -H "Authorization: Bearer $GENVIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "YOUR_VIDEO_MODEL",
    "prompt": "城市夜景，镜头缓慢推进，电影感光影"
  }'
```

## JSON 视频任务接口

提交任务：

```text
POST https://genvis.xyz/v1/video/generations
```

查询任务：

```text
GET https://genvis.xyz/v1/video/generations/{task_id}
```

请求示例：

```bash
curl "$GENVIS_BASE_URL/video/generations" \
  -H "Authorization: Bearer $GENVIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "YOUR_VIDEO_MODEL",
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

## 状态处理建议

1. 提交任务后保存返回的 `task_id` 或 `id`。
2. 后端定时查询任务状态，避免前端长时间阻塞。
3. 任务完成后保存视频 URL、原始提示词、模型 ID、尺寸、时长和成本信息。
4. 任务失败时展示可读错误，并允许用户重试或更换模型。

## 模型示例

视频生成能力可覆盖 Veo、sora2、GrokVideo 等模型。实际模型 ID、时长、分辨率、价格和权限以控制台及 `/v1/models` 返回为准。

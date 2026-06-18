# GitHub 发布和推广说明

这个仓库已经按中文用户优先的方式组织，适合放到官网 API 文档、开发者入口、社群推广内容和 AIGC 从业者试用链路里。定位是“部分前端体验展示 + 公开 API 轻量示例”，不是完整产品开源仓库。
官网 `/docs/api` 对应的公开调用说明，也会同步放在仓库的 `docs/api/` 目录里，方便访客从 GitHub 直接跳到接口文档。

## 推荐仓库信息

仓库名：

```text
genvis-ai-sdk-examples
```

中文描述：

```text
Genvis AI 前端体验展示与 API 中文示例：支持 Claude4.8、GPT5.5、Gemini3.5、gpt-Image2、Veo、sora2 等图文视频模型，新用户送 2 美元试用额度。
```

英文描述：

```text
Frontend showcase and OpenAI-compatible API examples for Genvis AI text, image, and video generation, with a 2 USD trial credit for new users.
```

## 推荐 Topics

```text
genvis-ai
openai-compatible
ai-api
ai-gateway
aigc
image-generation
video-generation
text-generation
openai-sdk
claude
gemini
gpt-image
sora
veo
wechat-pay
alipay
中文文档
```

## 官网入口文案

按钮文案：

```text
查看 GitHub 示例项目
```

或：

```text
5 分钟接入 Genvis AI API
```

说明文案：

```text
展示 Genvis AI 的部分前端体验和 Node.js、Python、cURL 公开 API 示例，覆盖文本推理、AI 图片生成和 AI 视频异步任务。Genvis AI 支持 Claude4.8、GPT5.5、Gemini3.5、gpt-Image2、Nano Banao 2、Veo、sora2、GrokVideo 等旗舰模型，新用户注册即享 2 美元免费试用额度，适合国内开发者和 AIGC 团队快速体验与接入。
```

## 社群推广文案

```text
我们整理了 Genvis AI 的 GitHub 展示项目，主要展示部分前端体验和公开 API 轻量示例，支持 Node.js、Python 和 cURL，覆盖文本推理、AI 图片生成、AI 视频生成。

Genvis AI 支持 Claude4.8、GPT5.5、Gemini3.5、gpt-Image2、Nano Banao 2、Veo、sora2、GrokVideo 等旗舰模型。接口兼容 OpenAI SDK，只需要替换 baseURL 和 API Key 即可接入，也可以先在官网用可视化界面无代码生图、生视频。

新用户注册即享 2 美元免费试用额度，价格非常低，例如 gpt-image 2 低至 ¥0.2。适合国内开发者、AI 工具站、AIGC 从业者、自媒体工具和电商素材系统快速验证效果。

GitHub:
https://github.com/jimmyliu758-star/genvis-ai-sdk-examples

官网:
https://genvis.xyz
```

## README 首屏必须覆盖

- 官网和控制台入口：[https://genvis.xyz](https://genvis.xyz)
- 仓库定位：只展示部分前端体验和公开 API 示例，不开源完整平台实现
- 新用户 2 美元免费试用额度
- gpt-image 2 低至 ¥0.2 的价格优势示例
- 文本推理模型：Claude4.8、GPT5.5、Gemini3.5 等
- 图像生成模型：gpt-Image2、Nano Banao 2 等
- 视频生成模型：Veo、sora2、GrokVideo 等
- 三种使用模式：标准化 API、可视化生图、可视化生视频
- 不公开后端源码、模型路由、计费系统、用户系统、管理后台和生产配置

## 后续维护

- 保持 README 中文优先，英文作为辅助说明。
- `/docs/api`、README、quickstart 和产品能力页要保持同步更新。
- 所有对外文案必须避免“完整开源平台源码”这类误导表述。
- 每次新增模型能力时，同步更新 README、`docs/product-capabilities-zh.md`、`.env.example` 和示例代码。
- 视频模型参数变化时，优先更新 `video-generation` 示例。
- 如果官网价格、免费额度、充值方式或可视化产品能力变化，及时更新 README 和推广文案。

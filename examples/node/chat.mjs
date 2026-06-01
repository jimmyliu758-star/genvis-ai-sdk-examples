import 'dotenv/config';
import { createOpenAIClient } from '../../sdk/node/genvis-client.mjs';

const client = createOpenAIClient();
const model = process.env.GENVIS_TEXT_MODEL || 'YOUR_TEXT_MODEL';

const completion = await client.chat.completions.create({
  model,
  messages: [
    {
      role: 'user',
      content: '用一句话介绍 Genvis AI 的 API 能力。',
    },
  ],
});

console.log(completion.choices?.[0]?.message?.content || completion);

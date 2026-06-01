import 'dotenv/config';
import { createOpenAIClient } from '../../sdk/node/genvis-client.mjs';

const client = createOpenAIClient();
const model = process.env.GENVIS_IMAGE_MODEL || 'gpt-image-2-vip';

const result = await client.images.generate({
  model,
  prompt:
    'Premium product photography for a scented candle gift box, warm cozy lighting, clean commercial background, 4:5',
  n: 1,
  size: '1024x1280',
  quality: 'high',
});

console.log(JSON.stringify(result, null, 2));

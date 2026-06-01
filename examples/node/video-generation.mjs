import 'dotenv/config';
import {
  pollVideoTask,
  submitJsonVideoTask,
} from '../../sdk/node/genvis-client.mjs';

const model = process.env.GENVIS_VIDEO_MODEL || 'video_vidu';
const image = process.env.GENVIS_REFERENCE_IMAGE || 'https://example.com/product.png';

const task = await submitJsonVideoTask({
  model,
  prompt: '让画面中的产品缓慢旋转，背景有柔和光影，商业广告质感',
  image,
  duration: 5,
  size: '1080p',
  metadata: {
    aspectRatio: '16:9',
    resolution: '1080p',
    movement_amplitude: 'auto',
    bgm: false,
  },
});

console.log('submitted:', JSON.stringify(task, null, 2));

const taskId = task.id || task.data?.id || task.task_id || task.data?.task_id;
if (!taskId) {
  throw new Error(`Unable to find task id in response: ${JSON.stringify(task)}`);
}

const completed = await pollVideoTask(taskId);
console.log('completed:', JSON.stringify(completed, null, 2));

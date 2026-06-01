import OpenAI from 'openai';

export function getConfig() {
  const apiKey = process.env.GENVIS_API_KEY;
  const baseURL = process.env.GENVIS_BASE_URL || 'https://genvis.xyz/v1';

  if (!apiKey || apiKey === 'sk-your-api-key') {
    throw new Error('Set GENVIS_API_KEY in your environment or .env file.');
  }

  return { apiKey, baseURL };
}

export function createOpenAIClient() {
  return new OpenAI(getConfig());
}

export async function submitJsonVideoTask(payload) {
  const { apiKey, baseURL } = getConfig();
  const response = await fetch(`${baseURL}/video/generations`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });

  return readJsonResponse(response);
}

export async function getJsonVideoTask(taskId) {
  const { apiKey, baseURL } = getConfig();
  const response = await fetch(`${baseURL}/video/generations/${taskId}`, {
    headers: {
      Authorization: `Bearer ${apiKey}`,
    },
  });

  return readJsonResponse(response);
}

export async function pollVideoTask(taskId, options = {}) {
  const intervalMs = options.intervalMs || 5000;
  const timeoutMs = options.timeoutMs || 10 * 60 * 1000;
  const startedAt = Date.now();

  while (Date.now() - startedAt < timeoutMs) {
    const task = await getJsonVideoTask(taskId);
    const status = task.status || task.data?.status;

    if (status === 'completed' || status === 'succeeded' || status === 'success') {
      return task;
    }

    if (status === 'failed' || status === 'cancelled' || status === 'canceled') {
      throw new Error(`Video task failed: ${JSON.stringify(task)}`);
    }

    await new Promise((resolve) => setTimeout(resolve, intervalMs));
  }

  throw new Error(`Video task timed out after ${timeoutMs} ms: ${taskId}`);
}

async function readJsonResponse(response) {
  const text = await response.text();
  let data;

  try {
    data = text ? JSON.parse(text) : {};
  } catch {
    data = { raw: text };
  }

  if (!response.ok) {
    const message = data.error?.message || data.message || response.statusText;
    throw new Error(`Genvis API error ${response.status}: ${message}`);
  }

  return data;
}

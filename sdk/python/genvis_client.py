import os
import time
from typing import Any, Dict, Optional

import requests
from openai import OpenAI


def get_config() -> Dict[str, str]:
    api_key = os.getenv("GENVIS_API_KEY")
    base_url = os.getenv("GENVIS_BASE_URL", "https://genvis.xyz/v1")

    if not api_key or api_key == "sk-your-api-key":
        raise RuntimeError("Set GENVIS_API_KEY in your environment or .env file.")

    return {"api_key": api_key, "base_url": base_url.rstrip("/")}


def create_openai_client() -> OpenAI:
    config = get_config()
    return OpenAI(api_key=config["api_key"], base_url=config["base_url"])


def submit_json_video_task(payload: Dict[str, Any]) -> Dict[str, Any]:
    config = get_config()
    response = requests.post(
        f"{config['base_url']}/video/generations",
        headers={
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=60,
    )
    return _read_json_response(response)


def get_json_video_task(task_id: str) -> Dict[str, Any]:
    config = get_config()
    response = requests.get(
        f"{config['base_url']}/video/generations/{task_id}",
        headers={"Authorization": f"Bearer {config['api_key']}"},
        timeout=60,
    )
    return _read_json_response(response)


def poll_video_task(
    task_id: str,
    interval_seconds: int = 5,
    timeout_seconds: int = 600,
) -> Dict[str, Any]:
    started_at = time.time()

    while time.time() - started_at < timeout_seconds:
        task = get_json_video_task(task_id)
        status = task.get("status") or task.get("data", {}).get("status")

        if status in {"completed", "succeeded", "success"}:
            return task

        if status in {"failed", "cancelled", "canceled"}:
            raise RuntimeError(f"Video task failed: {task}")

        time.sleep(interval_seconds)

    raise TimeoutError(f"Video task timed out after {timeout_seconds} seconds: {task_id}")


def _read_json_response(response: requests.Response) -> Dict[str, Any]:
    try:
        data: Dict[str, Any] = response.json()
    except ValueError:
        data = {"raw": response.text}

    if not response.ok:
        error = data.get("error") or {}
        message = error.get("message") or data.get("message") or response.reason
        raise RuntimeError(f"Genvis API error {response.status_code}: {message}")

    return data

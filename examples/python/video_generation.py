import os
import sys
from pathlib import Path

from dotenv import load_dotenv

sys.path.append(str(Path(__file__).resolve().parents[2] / "sdk" / "python"))
from genvis_client import poll_video_task, submit_json_video_task  # noqa: E402


load_dotenv()

model = os.getenv("GENVIS_VIDEO_MODEL", "video_vidu")
image = os.getenv("GENVIS_REFERENCE_IMAGE", "https://example.com/product.png")

task = submit_json_video_task(
    {
        "model": model,
        "prompt": "让画面中的产品缓慢旋转，背景有柔和光影，商业广告质感",
        "image": image,
        "duration": 5,
        "size": "1080p",
        "metadata": {
            "aspectRatio": "16:9",
            "resolution": "1080p",
            "movement_amplitude": "auto",
            "bgm": False,
        },
    }
)

print("submitted:", task)

task_id = (
    task.get("id")
    or task.get("task_id")
    or task.get("data", {}).get("id")
    or task.get("data", {}).get("task_id")
)

if not task_id:
    raise RuntimeError(f"Unable to find task id in response: {task}")

completed = poll_video_task(task_id)
print("completed:", completed)

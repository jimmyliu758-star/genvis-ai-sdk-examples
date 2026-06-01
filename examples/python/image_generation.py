import os
import sys
from pathlib import Path

from dotenv import load_dotenv

sys.path.append(str(Path(__file__).resolve().parents[2] / "sdk" / "python"))
from genvis_client import create_openai_client  # noqa: E402


load_dotenv()

client = create_openai_client()
model = os.getenv("GENVIS_IMAGE_MODEL", "gpt-image-2-vip")

result = client.images.generate(
    model=model,
    prompt=(
        "Premium product photography for a scented candle gift box, warm cozy "
        "lighting, clean commercial background, 4:5"
    ),
    n=1,
    size="1024x1280",
    quality="high",
)

print(result.model_dump_json(indent=2))

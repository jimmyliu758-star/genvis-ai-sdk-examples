import os
import sys
from pathlib import Path

from dotenv import load_dotenv

sys.path.append(str(Path(__file__).resolve().parents[2] / "sdk" / "python"))
from genvis_client import create_openai_client  # noqa: E402


load_dotenv()

client = create_openai_client()
model = os.getenv("GENVIS_TEXT_MODEL", "YOUR_TEXT_MODEL")

completion = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "用一句话介绍 Genvis AI 的 API 能力。",
        }
    ],
)

print(completion.choices[0].message.content)

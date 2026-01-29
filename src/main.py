import json
from pathlib import Path

# 将python数据对象转换为json
data = {
    "tasks": [
        {"id": 1, "content": "buy milk", "done": False, "created_data": "2026-1-1"},
        {
            "id": 2,
            "content": "go to supermarket",
            "done": True,
            "created_data": "2026-1-3",
        },
    ]
}
with open("task.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

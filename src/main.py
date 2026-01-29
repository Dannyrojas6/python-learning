import json
from pathlib import Path

# 将python数据对象转换为json
# data = {
#     "tasks": [
#         {"id": 1, "content": "buy milk", "done": False, "created_date": "2026-1-1"},
#         {
#             "id": 2,
#             "content": "go to supermarket",
#             "done": True,
#             "created_date": "2026-1-3",
#         },
#     ]
# }

# data_format = {"id": id, "content": content, "done": done, "created_date": created_date}
#
# with open("src/task.json", "a", encoding="utf-8") as f:
#     json.dump(data_format, f)

if Path("src/task.json").exists():
    id = int(input("Task id: "))
    content = input("content: ")
    done = input("done: ").strip().lower() == "true"
    created_date = str(input("created_date: "))

    with open("src/task.json") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"文件读取错误,原因：{e}")

        new_task = {
            "id": id,
            "content": content,
            "done": done,
            "created_date": created_date,
        }
        data["tasks"].append(new_task)
        with open("src/task.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

else:
    data_origin = {
        "tasks": [
            {
                "id": 1,
                "content": "buy milk",
                "done": False,
                "created_date": "2000-01-01",
            },
            {
                "id": 2,
                "content": "play minecraft",
                "done": True,
                "created_date": "2001-01-01",
            },
        ]
    }
    with open("src/task.json", "w") as f:
        json.dump(data_origin, f, indent=4, ensure_ascii=False)
        print("初始化成功！请再次运行脚本。")

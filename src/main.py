import json
from pathlib import Path
from rich.console import Console
from rich.table import Table
import typer
from typing import Optional
from datetime import date


app = typer.Typer()
console = Console()


def init():
    data_origin = {
        "tasks": [
            {
                "id": 1,
                "content": "buy milk",
                "done": False,
                "date": "2000-01-01",
            },
            {
                "id": 2,
                "content": "play minecraft",
                "done": False,
                "date": "2001-01-01",
            },
            {
                "id": 3,
                "content": "listen to music",
                "done": True,
                "date": "1999-09-09",
            },
        ]
    }
    with open("src/task.json", "w") as f:
        json.dump(data_origin, f, indent=4, ensure_ascii=False)
        console.print("初始化成功！")


def load_tasks():
    if not Path("src/task.json").exists():
        console.print("文件不存在！将自动生成文件。")
        init()
    try:
        with open("src/task.json", "r") as f:
            return json.load(f)
    except Exception as e:
        console.print(f"文件读取错误！原因：{e}")
        return None


def save_tasks(data):
    with open("src/task.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


@app.command()
def add(
    content: str,
    done: bool = False,
    date: Optional[str] = date.today().isoformat(),
):
    data = load_tasks()
    if data is None:
        console.print("读取文件失败！文件为空。")
        return
    id = max([task["id"] for task in data["tasks"]], default=0) + 1
    new_task = {
        "id": id,
        "content": content,
        "done": done,
        "date": date,
    }
    data["tasks"].append(new_task)
    save_tasks(data)


@app.command()
def list():
    data = load_tasks()
    if data is None:
        console.print("读取文件失败！文件为空。")
        return

    table = Table()
    table.add_column("ID")
    table.add_column("内容")
    table.add_column("完成状态")
    table.add_column("创建日期")

    for task in data["tasks"]:
        status = "✅" if task["done"] else "❌"
        table.add_row(str(task["id"]), task["content"], status, task["date"])
    console.print(table)


@app.command()
def clear():
    data = load_tasks()
    if data is None:
        console.print("读取文件失败！文件为空。")
        return
    data["tasks"] = []
    save_tasks(data)


@app.command()
def done(task_id: int):
    data = load_tasks()
    if data is None:
        console.print("读取文件失败！文件为空。")
        return

    tasks = data["tasks"]
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
    save_tasks(data)


@app.command()
def remove(task_id: int):
    data = load_tasks()
    if data is None:
        console.print("读取文件失败！文件为空。")
        return
    data["tasks"] = [task for task in data["tasks"] if task["id"] != task_id]
    save_tasks(data)


@app.command()
def search(keyword: str):
    data = load_tasks()
    if data is None:
        return
    resaults = [
        task for task in data["tasks"] if keyword.lower() in task["content"].lower()
    ]

    table = Table()
    table.add_column("ID")
    table.add_column("内容")
    table.add_column("完成状态")
    table.add_column("创建日期")

    for task in resaults:
        status = "✅" if task["done"] else "❌"
        table.add_row(str(task["id"]), task["content"], status, task["date"])
    console.print(table)


@app.command()
def edit(
    id: int,
    content: Optional[str] = None,
    done: Optional[str] = None,
    date: Optional[str] = None,
):
    data = load_tasks()
    if data is None:
        console.print("读取文件失败！文件为空。")
        return
    for task in data["tasks"]:
        if task["id"] == id:
            if content is not None:
                task["content"] = content
            if done is not None:
                if done.lower() in "true":
                    task["done"] = True
                elif done.lower() in "false":
                    task["done"] = False
                else:
                    console.print("完成状态输入有误！请重试。")
                    return
            if date is not None:
                task["date"] = date
    save_tasks(data)


@app.command()
def test():
    init()


if __name__ == "__main__":
    app()

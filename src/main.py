import json
from pathlib import Path
from rich.console import Console
from rich.table import Table


def add_func():
    data: dict = {"tasks": []}
    if Path("src/task.json").exists():
        id = int(input("Task id: "))
        content = input("content: ")
        done = input("done: ").strip().lower() == "true"
        created_date = input("created_date: ")

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
                    "done": False,
                    "created_date": "2001-01-01",
                },
                {
                    "id": 3,
                    "content": "listen to music",
                    "done": False,
                    "created_date": "1999-09-09",
                },
            ]
        }
        with open("src/task.json", "w") as f:
            json.dump(data_origin, f, indent=4, ensure_ascii=False)
            print("初始化成功！请再次运行脚本。")


def list_func():
    with open("src/task.json", encoding="utf-8") as f:
        data = json.load(f)
        # for i in data["tasks"]:
        #     tem_list = []
        #     for j in i.values():
        #         tem_list.append(j)
        #     print(
        #         f"id:{tem_list[0]},content:{tem_list[1]},done:{tem_list[2]},created_date:{tem_list[3]}"
        #     )
        table = Table()
        console = Console()
        table.add_column("ID")
        table.add_column("内容")
        table.add_column("完成状态")
        table.add_column("创建日期")

        for task in data["tasks"]:
            status = "✅" if task["done"] else "❌"
            table.add_row(
                str(task["id"]), task["content"], status, task["created_date"]
            )
        console.print(table)


# def display_func():
#     with open("src/task.json", encoding="utf-8") as f:
#         data = json.load(f)
#         print(data)
#


def done_func(arg):
    with open("src/task.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        # for value in enumerate(data["tasks"][arg]):
        #     if value["done"][arg]=="False":
        #         data["tasks"][arg]=="True"
        # data_dict = data["tasks"]

        # try:
        #     data["tasks"][arg]["done"] = True
        # except Exception as e:
        #     print(f"Error!reason:({e})")

        tasks = data["tasks"]
        for task in tasks:
            if int(task["id"]) == arg:
                task["done"] = not task["done"]

    with open("src/task.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def remove_func(arg):
    with open("src/task.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        data["tasks"] = [task for task in data["tasks"] if int(task["id"]) != arg]
    with open("src/task.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def main():
    while True:
        print("\n")
        print("1.添加任务")
        print("2.删除任务")
        print("3.列出所有任务")
        print("4.切换任务完成状态")
        print("0.退出")
        arg = int(input("请输入功能编号："))
        match arg:
            case 1:
                add_func()
            case 2:
                remove_index = int(input("请输入任务编号："))
                remove_func(remove_index)
            case 3:
                list_func()
            case 4:
                done_index = int(input("请输入任务编号："))
                done_func(done_index)
            case 0:
                break
            case _:
                print("无效输入！请重试。")


if __name__ == "__main__":
    main()

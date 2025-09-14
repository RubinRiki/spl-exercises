# Riki Rubin 326380359
# Hadas Donat 325950954

def task_manager():
    tasks = {}

    def add_task(task, status="incomplete"):
        tasks[task] = status

    def get_tasks():
        return tasks

    def complete_task(task):
        if task in tasks:
            tasks[task] = "complete"

    return {
        "add_task": add_task,
        "get_tasks": get_tasks,
        "complete_task": complete_task
    }


if __name__ == "__main__":
    tm = task_manager()
    tm["add_task"]("Homework")
    tm["add_task"]("Shopping", "in progress")
    print("Tasks:", tm["get_tasks"]())
    tm["complete_task"]("Homework")
    print("Tasks after complete:", tm["get_tasks"]())
